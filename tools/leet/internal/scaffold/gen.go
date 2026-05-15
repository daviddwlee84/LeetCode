// Package scaffold generates the per-problem files (Naive{ID}.py, test_{ID}.py,
// optional Note{ID}.md) following the repo's existing conventions.
//
// Idempotent: if a file already exists we skip it (don't overwrite the user's
// in-progress code). Returns the list of *newly* created files so the caller
// can show them.
package scaffold

import (
	"errors"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"
	"strings"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/leetcode"
)

// Inputs collects everything Daily needs to scaffold a problem folder.
type Inputs struct {
	Folder     string   // absolute path to the per-problem folder
	ID         string   // questionFrontendId, e.g. "1572"
	Title      string   // "Matrix Diagonal Sum"
	Difficulty string   // "Easy" | "Medium" | "Hard"
	URL        string   // canonical leetcode URL
	ContentMD  string   // problem description (best-effort markdown)
	Samples    []string // raw sample testcase lines from LeetCode
	WithNote   bool     // also create Note{ID}.md
}

// ProblemFolder returns the absolute path for a daily problem under
// repoRoot/Python3/{Category}/{PascalTitle}.
func ProblemFolder(repoRoot, category, title string) string {
	return filepath.Join(repoRoot, "Python3", category, PascalCase(title))
}

// NaivePath returns the path of the Naive{ID}.py entry file.
func NaivePath(folder, id string) string {
	return filepath.Join(folder, "Naive"+id+".py")
}

// Daily creates the standard set of files for a daily problem. The folder is
// created (mkdir -p) if missing.
func Daily(in Inputs) ([]string, error) {
	if err := os.MkdirAll(in.Folder, 0o755); err != nil {
		return nil, err
	}

	// Pull starter code from LeetCode if we have it; we do this lazily — the
	// caller provides Inputs without snippet, but if URL contains the slug
	// we don't have the snippet here. For now, scaffold a minimal class.
	starter := minimalSolutionStub()

	ctx := tmplCtx{
		ID:         in.ID,
		Title:      in.Title,
		Difficulty: in.Difficulty,
		URL:        in.URL,
		Starter:    starter,
		Content:    in.ContentMD,
		Samples:    in.Samples,
	}

	created := []string{}
	files := []struct {
		path   string
		render func() (string, error)
	}{
		{NaivePath(in.Folder, in.ID), func() (string, error) { return renderSolution(ctx) }},
		{filepath.Join(in.Folder, "test_"+in.ID+".py"), func() (string, error) { return renderTest(ctx) }},
	}
	if in.WithNote {
		files = append(files, struct {
			path   string
			render func() (string, error)
		}{
			filepath.Join(in.Folder, "Note"+in.ID+".md"),
			func() (string, error) { return renderNote(ctx) },
		})
	}

	for _, f := range files {
		if _, err := os.Stat(f.path); err == nil {
			continue // already exists, leave alone
		} else if !errors.Is(err, fs.ErrNotExist) {
			return created, err
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
	return created, nil
}

// DailyFromQuestion is a convenience wrapper that pulls starter code,
// description, and samples directly from a leetcode.Question.
func DailyFromQuestion(folder string, q leetcode.Question, withNote bool) ([]string, error) {
	in := Inputs{
		Folder:     folder,
		ID:         q.QuestionFrontendID,
		Title:      q.Title,
		Difficulty: q.Difficulty,
		URL:        q.URL(),
		ContentMD:  q.ContentMarkdown(),
		Samples:    q.Samples(),
		WithNote:   withNote,
	}
	created, err := Daily(in)
	if err != nil {
		return created, err
	}
	// Replace the Naive stub with the python3 starter from LeetCode if we
	// just created it.
	naive := NaivePath(folder, q.QuestionFrontendID)
	for _, c := range created {
		if c == naive {
			body := fmt.Sprintf(
				"# %s. %s (%s)\n# %s\n%s\n%s",
				q.QuestionFrontendID, q.Title, q.Difficulty, q.URL(),
				typingImportFor(q.PythonStarter()),
				q.PythonStarter(),
			)
			if err := os.WriteFile(naive, []byte(body), 0o644); err != nil {
				return created, err
			}
		}
	}
	return created, nil
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

// Contest scaffolds the four sub-folders for a weekly/biweekly contest. Files
// per sub-folder: problem.md (description), Solution.py (starter), test_.py
// (sample-based stub).
func Contest(repoRoot string, c leetcode.Contest) ([]string, error) {
	dir := c.LocalDir(repoRoot)
	if err := os.MkdirAll(dir, 0o755); err != nil {
		return nil, err
	}
	created := []string{}
	for _, p := range c.Problems {
		sub := filepath.Join(dir, fmt.Sprintf("%d", p.Index))
		if err := os.MkdirAll(sub, 0o755); err != nil {
			return created, err
		}

		// problem.md (always overwrite — scrape may improve over time)
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

		// Solution.py
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

		// test_.py — only if we have samples
		samples := p.Question.Samples()
		if len(samples) > 0 {
			tpath := filepath.Join(sub, "test_.py")
			if !exists(tpath) {
				ctx := tmplCtx{ID: "", Title: p.Title, Samples: samples}
				body, err := renderTest(ctx)
				if err != nil {
					return created, err
				}
				// renderTest assumes Naive{ID} module name; for contest we just
				// import Solution from Solution.
				body = strings.Replace(body, "from Naive import Solution as Naive", "from Solution import Solution as Naive", 1)
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

// Folder metadata for the readme-row command.
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

// InspectFolder reads a problem folder and returns the metadata needed to
// render a README row. We infer fields from filenames; difficulty/date are
// left blank for the user to fill in.
func InspectFolder(folder string) (FolderMeta, error) {
	abs, err := filepath.Abs(folder)
	if err != nil {
		return FolderMeta{}, err
	}
	entries, err := os.ReadDir(abs)
	if err != nil {
		return FolderMeta{}, err
	}

	meta := FolderMeta{
		Category: filepath.Base(filepath.Dir(abs)),
		Title:    splitPascal(filepath.Base(abs)),
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
	// Optional Note{ID}.md
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

// splitPascal turns "MatrixDiagonalSum" back into "Matrix Diagonal Sum" for
// README presentation.
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
