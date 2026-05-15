package scaffold

import (
	"bytes"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"text/template"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/config"
)

// InitOpts configures `leet init`. Zero values are sensible defaults.
type InitOpts struct {
	Target           string         // directory to init (must exist)
	Layout           string         // "legacy" | "structured"; empty → cfg.DefaultLayout
	Name             string         // README + AGENTS.md title; empty → basename(Target)
	Categories       []string       // empty → cfg.Categories (12 by default)
	InitGit          bool           // run `git init` if not already a repo
	WithAgents       bool           // create .agents/ + AGENTS.md + symlinks
	WithSocratic     bool           // copy socratic-tutor skill (or symlink from $HOME)
	WithPyproject    bool           // create pyproject.toml for the new repo
	Force            bool           // proceed even if .leet/ already exists
}

// InitVars is the template substitution context for init_templates.go.
type initVars struct {
	Name        string
	Layout      string
	PackageName string
}

// InitRepo bootstraps a fresh practice repo at opts.Target. Idempotent:
// existing files are NOT overwritten unless Force is set on the same file
// (currently no callers pass Force per-file — Force only short-circuits
// the .leet/config.toml safety check).
//
// Returns the list of newly created paths (relative to opts.Target).
func InitRepo(cfg config.Config, opts InitOpts) ([]string, error) {
	if opts.Target == "" {
		return nil, fmt.Errorf("init: Target is required")
	}
	if err := os.MkdirAll(opts.Target, 0o755); err != nil {
		return nil, err
	}

	// Resolve layout.
	layout := opts.Layout
	if layout == "" {
		layout = cfg.DefaultLayout
	}
	if layout == "" {
		layout = "structured"
	}
	if layout != "legacy" && layout != "structured" {
		return nil, fmt.Errorf("init: unknown layout %q (use legacy|structured)", layout)
	}

	// Refuse to overwrite an existing .leet/ unless --force.
	leetDir := filepath.Join(opts.Target, ".leet")
	if exists(leetDir) && !opts.Force {
		return nil, fmt.Errorf("init: %s already exists (use --force to overlay)", leetDir)
	}

	name := opts.Name
	if name == "" {
		name = filepath.Base(opts.Target)
	}
	pkg := strings.ReplaceAll(strings.ToLower(name), " ", "-")

	vars := initVars{Name: name, Layout: layout, PackageName: pkg}
	created := []string{}

	// Resolve the layout spec to know category casing.
	spec := cfg.Layouts.Get(layout)

	// 1. .leet/config.toml
	if err := writeTemplated(filepath.Join(leetDir, "config.toml"), initLeetConfigTmpl, vars); err != nil {
		return created, err
	}
	created = append(created, ".leet/config.toml")

	// 2. Top-level docs.
	for _, f := range []struct{ rel, tmpl string }{
		{"README.md", initREADMETmpl},
		{".gitignore", initGitignoreTmpl},
	} {
		path := filepath.Join(opts.Target, f.rel)
		if exists(path) {
			continue
		}
		if err := writeTemplated(path, f.tmpl, vars); err != nil {
			return created, err
		}
		created = append(created, f.rel)
	}

	// 3. Optional pyproject.toml.
	if opts.WithPyproject {
		path := filepath.Join(opts.Target, "pyproject.toml")
		if !exists(path) {
			if err := writeTemplated(path, initPyprojectTmpl, vars); err != nil {
				return created, err
			}
			created = append(created, "pyproject.toml")
		}
	}

	// 4. AGENTS.md (+ CLAUDE.md symlink) when WithAgents.
	if opts.WithAgents {
		agents := filepath.Join(opts.Target, "AGENTS.md")
		if !exists(agents) {
			if err := writeTemplated(agents, initAGENTSTmpl, vars); err != nil {
				return created, err
			}
			created = append(created, "AGENTS.md")
		}
		// .agents/ + .claude/ + symlinks
		if err := os.MkdirAll(filepath.Join(opts.Target, ".agents/skills"), 0o755); err != nil {
			return created, err
		}
		if err := os.MkdirAll(filepath.Join(opts.Target, ".claude"), 0o755); err != nil {
			return created, err
		}
		// .claude/skills → ../.agents/skills (only if not already a symlink)
		linkPath := filepath.Join(opts.Target, ".claude/skills")
		if !exists(linkPath) {
			if err := os.Symlink("../.agents/skills", linkPath); err != nil {
				return created, err
			}
			created = append(created, ".claude/skills")
		}
		// .claude/settings.json (real file, Claude-specific)
		settingsPath := filepath.Join(opts.Target, ".claude/settings.json")
		if !exists(settingsPath) {
			if err := writeTemplated(settingsPath, initClaudeSettingsTmpl, vars); err != nil {
				return created, err
			}
			created = append(created, ".claude/settings.json")
		}
		// CLAUDE.md → AGENTS.md
		claudeLink := filepath.Join(opts.Target, "CLAUDE.md")
		if !exists(claudeLink) {
			if err := os.Symlink("AGENTS.md", claudeLink); err != nil {
				return created, err
			}
			created = append(created, "CLAUDE.md")
		}
	}

	// 5. Category folders with .gitkeep — names follow the layout's case rule.
	cats := opts.Categories
	if cats == nil {
		cats = cfg.Categories
	}
	pythonRoot := cfg.Paths.Python
	if pythonRoot == "" {
		pythonRoot = "Python3"
	}
	for _, c := range cats {
		dirName := config.ApplyCategoryCase(c, spec.CategoryCase)
		dir := filepath.Join(opts.Target, pythonRoot, dirName)
		if err := os.MkdirAll(dir, 0o755); err != nil {
			return created, err
		}
		gk := filepath.Join(dir, ".gitkeep")
		if !exists(gk) {
			if err := os.WriteFile(gk, nil, 0o644); err != nil {
				return created, err
			}
			created = append(created, filepath.Join(pythonRoot, dirName, ".gitkeep"))
		}
	}

	// 6. Contest dir.
	contestRoot := cfg.Paths.Contest
	if contestRoot == "" {
		contestRoot = "Contest/LeetCodeWeeklyContest"
	}
	contestDir := filepath.Join(opts.Target, contestRoot)
	if err := os.MkdirAll(contestDir, 0o755); err != nil {
		return created, err
	}
	gk := filepath.Join(contestDir, ".gitkeep")
	if !exists(gk) {
		if err := os.WriteFile(gk, nil, 0o644); err != nil {
			return created, err
		}
		created = append(created, filepath.Join(contestRoot, ".gitkeep"))
	}

	// 7. git init (last, so the initial commit captures the scaffolding).
	if opts.InitGit && !exists(filepath.Join(opts.Target, ".git")) {
		cmd := exec.Command("git", "init", "-q")
		cmd.Dir = opts.Target
		if err := cmd.Run(); err != nil {
			return created, fmt.Errorf("git init: %w", err)
		}
		created = append(created, ".git/")
	}

	return created, nil
}

func writeTemplated(path, tmpl string, data any) error {
	if err := os.MkdirAll(filepath.Dir(path), 0o755); err != nil {
		return err
	}
	t, err := template.New(filepath.Base(path)).Parse(tmpl)
	if err != nil {
		return err
	}
	var buf bytes.Buffer
	if err := t.Execute(&buf, data); err != nil {
		return err
	}
	return os.WriteFile(path, buf.Bytes(), 0o644)
}
