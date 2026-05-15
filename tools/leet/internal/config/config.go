// Package config drives every layout decision in `leet`: where to place a
// new problem folder, what to name solution / test / note files, which 12
// category folders to use, and how the LeetCode tag → folder priority list
// looks. Resolution order (highest precedence first):
//
//  1. CLI flag (applied by callers, not here)
//  2. Per-repo .leet/config.toml
//  3. Per-user ~/.config/leet/config.toml
//  4. Built-in defaults (defaults.go — preserves this repo's 2018 conventions)
//
// The two named layouts are:
//
//   - "legacy"      — Naive{ID}.py / test_{ID}.py / Note{ID}.md, PascalCase
//                     folders. What this repo has used since 2018.
//   - "structured"  — naive.py / test.py / README.md / meta.json,
//                     kebab-case folder + snake_case file. New design.
//
// See the plan doc at .agents/plans/ or .claude/plans/ for full design notes.
package config

import (
	"errors"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"

	toml "github.com/pelletier/go-toml/v2"
)

// Config is the merged view of all config sources for a given Load() call.
type Config struct {
	// DefaultLayout is used by `leet init` when no --layout flag is passed.
	DefaultLayout string `toml:"default_layout"`

	// Layout names the active layout for the resolved repo (or "" if Load
	// didn't see a per-repo override and the user didn't set one — callers
	// must then fall back to DefaultLayout themselves).
	Layout string `toml:"layout"`

	AuthFile         string         `toml:"auth_file"`
	Categories       []string       `toml:"categories"`
	FallbackCategory string         `toml:"fallback_category"`
	CategoryPriority []TagDirEntry  `toml:"category_priority"`
	Layouts          LayoutMap      `toml:"layouts"`
	Paths            PathsConfig    `toml:"paths"`
}

// TagDirEntry is one row of the LeetCode-tag → category-folder priority
// table. PickCategory walks this in order and returns the first matching
// tag (case-insensitive substring match).
type TagDirEntry struct {
	Tag string `toml:"tag"`
	Dir string `toml:"dir"`
}

// LayoutMap is keyed by layout name ("legacy", "structured"). We use a
// concrete type rather than map[string]LayoutSpec so TOML unmarshalling
// hits the named-subtable form (`[layouts.legacy]`, `[layouts.structured]`).
type LayoutMap struct {
	Legacy     LayoutSpec `toml:"legacy"`
	Structured LayoutSpec `toml:"structured"`
}

// Get returns the layout spec for `name`, falling back to Legacy if the
// name doesn't match — caller-side defaults handle empty/invalid input.
func (l LayoutMap) Get(name string) LayoutSpec {
	switch name {
	case "structured":
		return l.Structured
	default:
		return l.Legacy
	}
}

// LayoutSpec describes one layout's naming rules. Pattern strings use the
// tokens described in expand.go (e.g. "{title_pascal}", "{strategy_snake}",
// "{id}"). Empty fields after merge inherit from the built-in defaults.
type LayoutSpec struct {
	FolderPattern   string   `toml:"folder_pattern"`
	CategoryCase    string   `toml:"category_case"` // "" (preserve) | "lower"
	SolutionPattern string   `toml:"solution_pattern"`
	TestPattern     string   `toml:"test_pattern"`
	NotePattern     string   `toml:"note_pattern"`
	TestImport      string   `toml:"test_import"`
	TestStyle       string   `toml:"test_style"` // "per_strategy" | "parametrize"
	MetaFile        string   `toml:"meta_file"`  // "" (no meta) | "meta.json"
	StrategyKinds   []string `toml:"strategy_kinds"`
}

// PathsConfig points at the top-level language folders relative to repo root.
type PathsConfig struct {
	Python     string `toml:"python"`
	Contest    string `toml:"contest"`
	JavaScript string `toml:"javascript"`
	Cpp        string `toml:"cpp"`
}

// PerRepoFile is the filename leet looks for under repoRoot when resolving
// per-repo overrides.
const PerRepoFile = ".leet/config.toml"

// UserConfigSubpath is the relative path under os.UserConfigDir() where the
// user-level config lives (e.g. macOS:
// ~/Library/Application Support/leet/config.toml).
const UserConfigSubpath = "leet/config.toml"

// Load merges defaults → user-level → per-repo. If repoRoot is "" the
// per-repo overlay is skipped. The returned Config is guaranteed to have
// non-empty Layouts and Paths (filled from defaults if user/repo didn't
// supply them).
func Load(repoRoot string) (Config, error) {
	cfg := Defaults()

	// User-level overlay.
	if userPath, err := userConfigPath(); err == nil {
		if user, ok, err := readIfExists(userPath); err != nil {
			return cfg, fmt.Errorf("read user config %s: %w", userPath, err)
		} else if ok {
			Merge(&cfg, user)
		}
	}

	// Per-repo overlay.
	if repoRoot != "" {
		repoPath := filepath.Join(repoRoot, PerRepoFile)
		if repo, ok, err := readIfExists(repoPath); err != nil {
			return cfg, fmt.Errorf("read repo config %s: %w", repoPath, err)
		} else if ok {
			Merge(&cfg, repo)
		}
	}

	// If neither user nor repo set a Layout, fall back to DefaultLayout.
	if cfg.Layout == "" {
		cfg.Layout = cfg.DefaultLayout
	}
	return cfg, nil
}

// readIfExists returns (parsed, true, nil) if the file is found and parses,
// (zero, false, nil) if not found, and (zero, false, err) for other errors.
func readIfExists(path string) (Config, bool, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		if errors.Is(err, fs.ErrNotExist) {
			return Config{}, false, nil
		}
		return Config{}, false, err
	}
	var c Config
	if err := toml.Unmarshal(data, &c); err != nil {
		return Config{}, false, fmt.Errorf("parse: %w", err)
	}
	return c, true, nil
}

// userConfigPath returns the absolute path to the user-level config file.
var userConfigPath = func() (string, error) {
	dir, err := os.UserConfigDir()
	if err != nil {
		return "", err
	}
	return filepath.Join(dir, UserConfigSubpath), nil
}
