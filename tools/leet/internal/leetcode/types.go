package leetcode

import (
	"fmt"
	"path/filepath"
	"regexp"
	"strings"
)

// Question is the subset of LeetCode question data we need.
type Question struct {
	QuestionID         string     `json:"questionId"`
	QuestionFrontendID string     `json:"questionFrontendId"`
	Title              string     `json:"title"`
	TitleSlug          string     `json:"titleSlug"`
	Content            string     `json:"content"` // HTML
	Difficulty         string     `json:"difficulty"`
	ExampleTestcases   string     `json:"exampleTestcases"` // raw, newline-separated
	CodeSnippets       []Snippet  `json:"codeSnippets"`
	TopicTags          []TopicTag `json:"topicTags"`
}

type Snippet struct {
	Lang     string `json:"lang"`
	LangSlug string `json:"langSlug"`
	Code     string `json:"code"`
}

type TopicTag struct {
	Name string `json:"name"`
	Slug string `json:"slug"`
}

// URL returns the canonical leetcode.com URL.
func (q Question) URL() string {
	return "https://leetcode.com/problems/" + q.TitleSlug + "/"
}

// TopicTagNames flattens TopicTags into []string for categories.PickCategory.
func (q Question) TopicTagNames() []string {
	out := make([]string, 0, len(q.TopicTags))
	for _, t := range q.TopicTags {
		out = append(out, t.Name)
	}
	return out
}

// PythonStarter returns the python3 code snippet, or a minimal fallback.
func (q Question) PythonStarter() string {
	for _, s := range q.CodeSnippets {
		if s.LangSlug == "python3" {
			return s.Code
		}
	}
	return "class Solution:\n    pass\n"
}

var htmlTag = regexp.MustCompile(`<[^>]+>`)
var htmlEntities = strings.NewReplacer(
	"&nbsp;", " ",
	"&lt;", "<",
	"&gt;", ">",
	"&amp;", "&",
	"&quot;", `"`,
	"&#39;", "'",
	"&#x27;", "'",
)

// ContentMarkdown is a best-effort plaintext rendering of the HTML problem
// description — enough to drop into a problem.md / Note{ID}.md skeleton.
// We don't pull a real HTML→markdown lib; LeetCode markup is small.
func (q Question) ContentMarkdown() string {
	if q.Content == "" {
		return ""
	}
	s := q.Content
	// Convert a few block tags to newlines before stripping.
	for _, br := range []string{"<br>", "<br/>", "<br />", "</p>", "</li>", "</pre>"} {
		s = strings.ReplaceAll(s, br, "\n")
	}
	s = htmlTag.ReplaceAllString(s, "")
	s = htmlEntities.Replace(s)
	// Collapse runs of blank lines.
	s = regexp.MustCompile(`\n{3,}`).ReplaceAllString(s, "\n\n")
	return strings.TrimSpace(s)
}

// Samples returns the example test cases as raw strings (one per element).
// LeetCode returns them newline-separated; downstream code (scaffold) decides
// how to bucket them into the testcases list literal.
func (q Question) Samples() []string {
	if q.ExampleTestcases == "" {
		return nil
	}
	lines := strings.Split(q.ExampleTestcases, "\n")
	out := make([]string, 0, len(lines))
	for _, l := range lines {
		l = strings.TrimSpace(l)
		if l != "" {
			out = append(out, l)
		}
	}
	return out
}

// Contest holds the metadata for a weekly/biweekly contest plus its 4
// problems. The local on-disk layout is:
//
//	Contest/LeetCodeWeeklyContest/WeeklyContest{N}/{1..4}/
type Contest struct {
	Slug     string         // "weekly-contest-345"
	Number   int            // 345
	Kind     string         // "weekly" | "biweekly"
	Title    string         // "Weekly Contest 345"
	Problems []ContestEntry // index 0..3 → folder 1..4
}

type ContestEntry struct {
	Index    int    // 1..4 (matches existing folder names)
	Slug     string // titleSlug
	Title    string
	Question Question // populated lazily; may be empty if fetch failed
}

// LocalDir returns the on-disk directory for the contest under repoRoot.
func (c Contest) LocalDir(repoRoot string) string {
	dirName := fmt.Sprintf("WeeklyContest%d", c.Number)
	if c.Kind == "biweekly" {
		dirName = fmt.Sprintf("BiweeklyContest%d", c.Number)
	}
	return filepath.Join(repoRoot, "Contest", "LeetCodeWeeklyContest", dirName)
}

// SubmitResult is what we surface after polling the judge.
type SubmitResult struct {
	StatusMsg      string `json:"status_msg"`
	StatusCode     int    `json:"status_code"`
	Lang           string `json:"lang"`
	Runtime        string `json:"status_runtime"`
	Memory         string `json:"status_memory"`
	TotalCorrect   int    `json:"total_correct"`
	TotalTestcases int    `json:"total_testcases"`
	LastTestcase   string `json:"last_testcase"`
	ExpectedOutput string `json:"expected_output"`
	CodeOutput     string `json:"code_output"`
	CompileError   string `json:"compile_error"`
	RuntimeError   string `json:"runtime_error"`
	State          string `json:"state"`
}

// Accepted reports whether the submission passed all tests.
func (r SubmitResult) Accepted() bool {
	return r.StatusMsg == "Accepted"
}

// UserStatus is the auth-check response.
type UserStatus struct {
	IsSignedIn bool   `json:"isSignedIn"`
	Username   string `json:"username"`
}
