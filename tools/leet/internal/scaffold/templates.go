package scaffold

import (
	"bytes"
	"fmt"
	"strings"
	"text/template"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/config"
)

// tmplCtx is the shared context type passed to every render function.
// Different layouts pick which fields they actually use.
type tmplCtx struct {
	ID         string   // "1572"
	Title      string   // "Matrix Diagonal Sum"
	Difficulty string   // "Easy"
	URL        string   // canonical LeetCode URL
	Starter    string   // python3 code snippet from LeetCode (or stub)
	Content    string   // problem description (best-effort markdown)
	Samples    []string // raw sample testcase lines from LeetCode
	Strategy   string   // e.g. "Naive"
}

const solutionHeaderTmpl = `# {{.ID}}. {{.Title}} ({{.Difficulty}})
# {{.URL}}
{{ .Starter -}}
`

// renderSolution writes the {strategy}{id}.py / {strategy_snake}.py contents.
// Layout doesn't change the file body; only filename + path.
func renderSolution(_ config.LayoutSpec, c tmplCtx) (string, error) {
	return render("solution", solutionHeaderTmpl, c)
}

// renderTest dispatches on TestStyle. "per_strategy" (legacy) keeps the
// historical `for case in testcases: assert` shape; "parametrize"
// (structured) uses pytest.mark.parametrize across strategies.
func renderTest(spec config.LayoutSpec, c tmplCtx) (string, error) {
	switch spec.TestStyle {
	case "parametrize":
		return renderStructuredTest(spec, c)
	default:
		return renderLegacyTest(spec, c)
	}
}

// renderNote dispatches: legacy → Note{ID}.md; structured → README.md.
// Both use the same body template (problem + approach section + complexity
// + edge cases); only filename differs.
func renderNote(_ config.LayoutSpec, c tmplCtx) (string, error) {
	if c.Content == "" {
		c.Content = "_(paste / refine the LeetCode description here)_"
	} else {
		c.Content = strings.TrimSpace(c.Content)
	}
	return render("note", noteTmpl, c)
}

const noteTmpl = `# {{.ID}}. {{.Title}}

[LeetCode]({{.URL}}) — **{{.Difficulty}}**

## Description

{{.Content}}

## Approach

### {{ if .Strategy }}{{ .Strategy }}{{ else }}Naive{{ end }}

- Idea:
- Time:  O(?)
- Space: O(?)

## Edge cases

-
`

// wrapSamples turns each sample line into a single-element Python tuple
// literal so commas inside the sample (e.g. "[1,2,3]\n5") don't break
// outer testcases-list syntax.
func wrapSamples(samples []string) []string {
	out := make([]string, 0, len(samples))
	for _, s := range samples {
		out = append(out, fmt.Sprintf("(%s,)", s))
	}
	return out
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
