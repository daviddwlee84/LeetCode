package scaffold

import (
	"bytes"
	"fmt"
	"strings"
	"text/template"
)

// solutionTmpl mirrors the existing repo style: minimal class with the method
// stub from LeetCode, no frills. Any List / Optional imports come from the
// LeetCode-provided code snippet, so we don't second-guess them.
const solutionTmpl = `# {{.ID}}. {{.Title}} ({{.Difficulty}})
# {{.URL}}
{{ .Starter -}}
`

// testTmpl matches the convention in test_1572.py:
//
//	from Naive1572 import Solution as Naive
//
//	testcases = [...]
//
//	def test_Naive():
//	    for ... assert
const testTmpl = `from Naive{{.ID}} import Solution as Naive

# Sample testcases from LeetCode. Replace the second tuple entry with the
# expected output. Add more cases — including failed-submission inputs —
# below.
testcases = [
{{- range .Samples }}
    ({{ . }}, None),  # TODO: fill expected
{{- end }}
]


def test_Naive():
    sol = Naive()
    for inputs, expected in testcases:
        # TODO: invoke the actual method, e.g. sol.{{.MethodName}}(*inputs) == expected
        assert expected is None or expected == expected
`

// noteTmpl is what we drop into Note{ID}.md when --with-note is set.
const noteTmpl = `# {{.ID}}. {{.Title}}

[LeetCode]({{.URL}}) — **{{.Difficulty}}**

## Description

{{.Content}}

## Approach

### Naive

- Idea:
- Time:  O(?)
- Space: O(?)

## Edge cases

-
`

type tmplCtx struct {
	ID         string
	Title      string
	Difficulty string
	URL        string
	Starter    string
	Content    string
	Samples    []string
	MethodName string
}

func renderSolution(c tmplCtx) (string, error) {
	return render("solution", solutionTmpl, c)
}

func renderTest(c tmplCtx) (string, error) {
	if c.MethodName == "" {
		c.MethodName = "solve"
	}
	// Each sample line from LeetCode is plain (e.g. "[1,2,3,4]" or "[[1,2],[4,5]]").
	// We wrap each into a single-element tuple so test syntax stays valid even
	// if the sample contains commas at top level.
	wrapped := make([]string, 0, len(c.Samples))
	for _, s := range c.Samples {
		// Heuristic: if the sample already looks like Python literal,
		// emit it as a single tuple element. We don't try to parse multi-arg
		// signatures — the user fixes those manually after scaffolding.
		wrapped = append(wrapped, fmt.Sprintf("(%s,)", s))
	}
	c.Samples = wrapped
	return render("test", testTmpl, c)
}

func renderNote(c tmplCtx) (string, error) {
	if c.Content == "" {
		c.Content = "_(paste / refine the LeetCode description here)_"
	} else {
		c.Content = strings.TrimSpace(c.Content)
	}
	return render("note", noteTmpl, c)
}

func render(name, tmpl string, data any) (string, error) {
	t, err := template.New(name).Parse(tmpl)
	if err != nil {
		return "", err
	}
	var buf bytes.Buffer
	if err := t.Execute(&buf, data); err != nil {
		return "", err
	}
	return buf.String(), nil
}
