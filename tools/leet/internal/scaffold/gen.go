// Package scaffold generates the per-problem files (solution / test / note
// or README + meta.json) following whichever layout the resolved config
// names. The two named layouts are:
//
//   - "legacy"     — Naive{ID}.py / test_{ID}.py / Note{ID}.md
//   - "structured" — naive.py / test.py / README.md / meta.json
//
// All scaffolding is idempotent: existing files are left alone (don't
// overwrite user work). Returns the list of *newly* created files.
package scaffold

import (
	"errors"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
	"strings"
	"time"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/config"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/leetcode"
)

// Inputs collects everything Daily needs to scaffold a problem folder.
type Inputs struct {
	Folder     string   // absolute path to the per-problem folder
	ID         string   // questionFrontendId, e.g. "1572"
	Title      string   // "Matrix Diagonal Sum"
	Difficulty string   // "Easy" | "Medium" | "Hard"
	URL        string   // canonical leetcode URL
	TitleSlug  string   // LeetCode title slug, e.g. "matrix-diagonal-sum"
	ContentMD  string   // problem description (best-effort markdown)
	Samples    []string // raw sample testcase lines from LeetCode
	Tags       []string // LeetCode topic tags (for meta.json)
	Strategy   string   // initial strategy label; "" → "Naive"
	WithNote   bool     // also create Note{ID}.md / README.md
}

// ProblemFolder returns the absolute path for a problem under
// repoRoot/<python>/<category>/<folder>. Folder + category casing are
// layout-dependent.
func ProblemFolder(cfg config.Config, repoRoot, category, title string) string {
	spec := cfg.Layouts.Get(cfg.Layout)
	catName := config.ApplyCategoryCase(category, spec.CategoryCase)
	folder := config.Expand(spec.FolderPattern, config.PatternVars{Title: title})
	return filepath.Join(repoRoot, cfg.Paths.Python, catName, folder)
}

// EntryPath returns the path of the initial solution file (the one
// `leet daily` opens in $EDITOR). Layout-dependent.
func EntryPath(cfg config.Config, folder, id string) string {
	spec := cfg.Layouts.Get(cfg.Layout)
	strategy := "Naive"
	fname := config.Expand(spec.SolutionPattern, config.PatternVars{Strategy: strategy, ID: id})
	return filepath.Join(folder, fname)
}

// Daily creates the standard files for a new problem.
func Daily(cfg config.Config, in Inputs) ([]string, error) {
	if err := os.MkdirAll(in.Folder, 0o755); err != nil {
		return nil, err
	}
	spec := cfg.Layouts.Get(cfg.Layout)
	if in.Strategy == "" {
		in.Strategy = "Naive"
	}

	ctx := tmplCtx{
		ID:         in.ID,
		Title:      in.Title,
		Difficulty: in.Difficulty,
		URL:        in.URL,
		Starter:    minimalSolutionStub(),
		Content:    in.ContentMD,
		Samples:    in.Samples,
		Strategy:   in.Strategy,
	}

	// File paths derived from layout patterns.
	pv := config.PatternVars{Strategy: in.Strategy, ID: in.ID, Title: in.Title}
	solPath := filepath.Join(in.Folder, config.Expand(spec.SolutionPattern, pv))
	testPath := filepath.Join(in.Folder, config.Expand(spec.TestPattern, pv))
	notePath := filepath.Join(in.Folder, config.Expand(spec.NotePattern, pv))

	created := []string{}
	files := []struct {
		path   string
		render func() (string, error)
	}{
		{solPath, func() (string, error) { return renderSolution(spec, ctx) }},
		{testPath, func() (string, error) { return renderTest(spec, ctx) }},
	}
	if in.WithNote {
		files = append(files, struct {
			path   string
			render func() (string, error)
		}{notePath, func() (string, error) { return renderNote(spec, ctx) }})
	}

	for _, f := range files {
		if exists(f.path) {
			continue
		}
		body, err := f.render()
		if err != nil {
			return created, err
		}
		if err := os.WriteFile(f.path, []byte(body), 0o644); err != nil {
			return created, err
		}
		created = append(created, f.path)
	}

	// Write meta.json for structured layout (legacy keeps MetaFile == "").
	if spec.MetaFile != "" {
		metaPath := filepath.Join(in.Folder, spec.MetaFile)
		if !exists(metaPath) {
			m := Meta{
				ID:                 in.ID,
				Title:              in.Title,
				TitleSlug:          in.TitleSlug,
				Difficulty:         in.Difficulty,
				Tags:               in.Tags,
				URL:                in.URL,
				DateAdded:          time.Now().Format("2006-01-02"),
				LeetCodeQuestionID: in.ID,
				Strategies: []Strategy{
					{
						File:    filepath.Base(solPath),
						Name:    in.Strategy,
						Kind:    "own",
						Created: time.Now().Format("2006-01-02"),
					},
				},
			}
			if err := WriteMeta(metaPath, m); err != nil {
				return created, err
			}
			created = append(created, metaPath)
		}
	}

	return created, nil
}

// DailyFromQuestion is a convenience wrapper that pulls starter code,
// description, and samples directly from a leetcode.Question.
func DailyFromQuestion(cfg config.Config, folder string, q leetcode.Question, withNote bool) ([]string, error) {
	in := Inputs{
		Folder:     folder,
		ID:         q.QuestionFrontendID,
		Title:      q.Title,
		Difficulty: q.Difficulty,
		URL:        q.URL(),
		TitleSlug:  q.TitleSlug,
		ContentMD:  q.ContentMarkdown(),
		Samples:    q.Samples(),
		Tags:       q.TopicTagNames(),
		Strategy:   "Naive",
		WithNote:   withNote,
	}
	created, err := Daily(cfg, in)
	if err != nil {
		return created, err
	}
	// Overwrite the just-created solution file with the LeetCode python3
	// starter (so the user sees the real method signature, not a stub).
	entry := EntryPath(cfg, folder, q.QuestionFrontendID)
	for _, c := range created {
		if c == entry {
			body := fmt.Sprintf(
				"# %s. %s (%s)\n# %s\n%s\n%s",
				q.QuestionFrontendID, q.Title, q.Difficulty, q.URL(),
				typingImportFor(q.PythonStarter()),
				q.PythonStarter(),
			)
			if err := os.WriteFile(entry, []byte(body), 0o644); err != nil {
				return created, err
			}
		}
	}
	return created, nil
}

// Contest scaffolds the four sub-folders for a weekly/biweekly contest.
// Contest layout doesn't (yet) honor the legacy/structured switch — kept
// simple per the user's "先維持現狀後續再結構化" guidance.
func Contest(cfg config.Config, repoRoot string, c leetcode.Contest) ([]string, error) {
	dir := c.LocalDir(repoRoot)
	if err := os.MkdirAll(dir, 0o755); err != nil {
		return nil, err
	}
	spec := cfg.Layouts.Get("legacy") // contests stay legacy-styled for now
	created := []string{}
	for _, p := range c.Problems {
		sub := filepath.Join(dir, fmt.Sprintf("%d", p.Index))
		if err := os.MkdirAll(sub, 0o755); err != nil {
			return created, err
		}

		problemMD := filepath.Join(sub, "problem.md")
		md := fmt.Sprintf("# %s. %s\n\n%s\n\n%s\n",
			firstNonEmpty(p.Question.QuestionFrontendID, fmt.Sprintf("%d", p.Index)),
			p.Title,
			p.Question.URL(),
			p.Question.ContentMarkdown(),
		)
		if !exists(problemMD) {
			if err := os.WriteFile(problemMD, []byte(md), 0o644); err != nil {
				return created, err
			}
			created = append(created, problemMD)
		}

		solPath := filepath.Join(sub, "Solution.py")
		if !exists(solPath) {
			body := minimalSolutionStub()
			if p.Question.PythonStarter() != "" {
				body = p.Question.PythonStarter()
			}
			if err := os.WriteFile(solPath, []byte(body), 0o644); err != nil {
				return created, err
			}
			created = append(created, solPath)
		}

		samples := p.Question.Samples()
		if len(samples) > 0 {
			tpath := filepath.Join(sub, "test_.py")
			if !exists(tpath) {
				ctx := tmplCtx{ID: "", Title: p.Title, Samples: samples, Strategy: "Solution"}
				body, err := renderTest(spec, ctx)
				if err != nil {
					return created, err
				}
				if err := os.WriteFile(tpath, []byte(body), 0o644); err != nil {
					return created, err
				}
				created = append(created, tpath)
			}
		}
	}
	return created, nil
}

func minimalSolutionStub() string {
	return "from typing import List, Optional\n\n\nclass Solution:\n    pass\n"
}

func exists(path string) bool {
	_, err := os.Stat(path)
	return err == nil
}

func firstNonEmpty(a, b string) string {
	if a != "" {
		return a
	}
	return b
}

// typingImportFor inspects the LeetCode starter and emits the typing imports
// the user will likely need. LeetCode's snippets reference List/Optional/Dict
// without importing them — the existing repo files always add this header
// themselves (see Python3/Array/MatrixDiagonalSum/Naive1572.py:1).
func typingImportFor(starter string) string {
	want := []string{}
	for _, t := range []string{"List", "Optional", "Dict", "Tuple", "Set", "Deque"} {
		if strings.Contains(starter, t+"[") {
			want = append(want, t)
		}
	}
	if len(want) == 0 {
		return ""
	}
	return "from typing import " + strings.Join(want, ", ") + "\n"
}

// FolderMeta is the readme-row view of a problem folder. Filled by
// InspectFolder.
type FolderMeta struct {
	ID          string
	Title       string
	Difficulty  string
	Date        string
	Category    string
	Solutions   []SolutionMeta
	NoteRelPath string
}

type SolutionMeta struct {
	Method  string
	TimeStr string
	RelPath string
}

// InspectFolder reads a problem folder and returns metadata for the
// readme-row command. Detects layout heuristically:
//   - if `meta.json` exists, use it (structured)
//   - else infer from filename suffix (legacy)
func InspectFolder(folder string) (FolderMeta, error) {
	abs, err := filepath.Abs(folder)
	if err != nil {
		return FolderMeta{}, err
	}
	meta := FolderMeta{
		Category: filepath.Base(filepath.Dir(abs)),
	}

	// Try meta.json first (structured).
	if exists(filepath.Join(abs, "meta.json")) {
		m, err := ReadMeta(filepath.Join(abs, "meta.json"))
		if err != nil {
			return meta, err
		}
		meta.ID = m.ID
		meta.Title = m.Title
		meta.Difficulty = m.Difficulty
		meta.Date = m.DateAdded
		for _, s := range m.Strategies {
			meta.Solutions = append(meta.Solutions, SolutionMeta{
				Method:  s.Name,
				RelPath: filepath.Join("Python3", meta.Category, filepath.Base(abs), s.File),
			})
		}
		if exists(filepath.Join(abs, "README.md")) {
			meta.NoteRelPath = filepath.Join("Python3", meta.Category, filepath.Base(abs), "README.md")
		}
		return meta, nil
	}

	// Legacy: filenames carry the ID, no meta.json.
	meta.Title = splitPascal(filepath.Base(abs))
	entries, err := os.ReadDir(abs)
	if err != nil {
		return meta, err
	}
	for _, e := range entries {
		name := e.Name()
		if !strings.HasSuffix(name, ".py") || strings.HasPrefix(name, "test_") {
			continue
		}
		stem := strings.TrimSuffix(name, ".py")
		method, id := splitMethodID(stem)
		if id != "" {
			meta.ID = id
		}
		meta.Solutions = append(meta.Solutions, SolutionMeta{
			Method:  method,
			RelPath: filepath.Join("Python3", meta.Category, filepath.Base(abs), name),
		})
	}
	if meta.ID != "" {
		notePath := filepath.Join(abs, "Note"+meta.ID+".md")
		if exists(notePath) {
			meta.NoteRelPath = filepath.Join("Python3", meta.Category, filepath.Base(abs), "Note"+meta.ID+".md")
		}
	}
	return meta, nil
}

// splitMethodID splits "Naive1572" -> ("Naive", "1572"); "Better2_023" ->
// ("Better2", "023") — close enough for README purposes; the user can edit.
func splitMethodID(stem string) (method, id string) {
	i := len(stem)
	for i > 0 && stem[i-1] >= '0' && stem[i-1] <= '9' {
		i--
	}
	if i == len(stem) {
		return stem, ""
	}
	method = strings.TrimRight(stem[:i], "_")
	id = stem[i:]
	return method, id
}

// splitPascal turns "MatrixDiagonalSum" back into "Matrix Diagonal Sum".
// Used for legacy folders that don't have meta.json.
func splitPascal(s string) string {
	var b strings.Builder
	for i, r := range s {
		if i > 0 && r >= 'A' && r <= 'Z' {
			b.WriteByte(' ')
		}
		b.WriteRune(r)
	}
	return b.String()
}

// sentinelErrors so callers can distinguish missing folder from other errors.
var ErrNotADir = errors.New("not a directory")

// statDir is a helper used by tests to validate folder existence cleanly.
func statDir(p string) error {
	info, err := os.Stat(p)
	if err != nil {
		if errors.Is(err, fs.ErrNotExist) {
			return ErrNotADir
		}
		return err
	}
	if !info.IsDir() {
		return ErrNotADir
	}
	return nil
}
