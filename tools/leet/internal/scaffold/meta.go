package scaffold

import (
	"encoding/json"
	"fmt"
	"os"
)

// Meta is the on-disk meta.json for a structured-layout problem folder.
// Schema is intentionally permissive — fields can be added without
// breaking existing files.
type Meta struct {
	ID                 string     `json:"id"`
	Title              string     `json:"title"`
	TitleSlug          string     `json:"title_slug"`
	Difficulty         string     `json:"difficulty"`
	Tags               []string   `json:"tags"`
	URL                string     `json:"url"`
	DateAdded          string     `json:"date_added"`
	LeetCodeQuestionID string     `json:"leetcode_question_id,omitempty"`
	Strategies         []Strategy `json:"strategies"`
}

// Strategy is one entry in Meta.Strategies. Kind distinguishes:
//   - "own"       — wrote it from scratch, no hints
//   - "reference" — saw a hint / discussion then re-wrote it
//   - "archive"   — collected verbatim from someone else; passes tests but
//                   explicitly NOT my original work, only for study
type Strategy struct {
	File       string            `json:"file"`              // "naive.py"
	Name       string            `json:"name"`              // "Naive"
	Kind       string            `json:"kind"`              // "own" | "reference" | "archive"
	Created    string            `json:"created"`           // "2026-05-15"
	Source     string            `json:"source,omitempty"`  // free-form (e.g. "leetcode editorial")
	Notes      string            `json:"notes,omitempty"`
	Complexity *Complexity       `json:"complexity,omitempty"`
	Extra      map[string]string `json:"extra,omitempty"`
}

type Complexity struct {
	Time  string `json:"time"`  // "O(n)"
	Space string `json:"space"` // "O(1)"
}

// ReadMeta parses meta.json. Returns a typed error chain so callers can
// distinguish "no meta.json" from "malformed".
func ReadMeta(path string) (Meta, error) {
	data, err := os.ReadFile(path)
	if err != nil {
		return Meta{}, err
	}
	var m Meta
	if err := json.Unmarshal(data, &m); err != nil {
		return Meta{}, fmt.Errorf("parse %s: %w", path, err)
	}
	return m, nil
}

// WriteMeta writes m to path with indented JSON (2 spaces) so it's
// readable in diffs.
func WriteMeta(path string, m Meta) error {
	body, err := json.MarshalIndent(m, "", "  ")
	if err != nil {
		return err
	}
	body = append(body, '\n')
	return os.WriteFile(path, body, 0o644)
}

// AddStrategy appends a new strategy entry to meta.json (or creates the
// file if missing). Idempotent on (File, Name) — re-running won't add
// duplicates. Returns the post-write Meta for inspection.
func AddStrategy(path string, s Strategy) (Meta, error) {
	m, err := ReadMeta(path)
	if err != nil && !os.IsNotExist(err) {
		return Meta{}, err
	}
	for _, existing := range m.Strategies {
		if existing.File == s.File && existing.Name == s.Name {
			return m, nil
		}
	}
	m.Strategies = append(m.Strategies, s)
	return m, WriteMeta(path, m)
}
