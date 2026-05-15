package scaffold

import (
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/config"
)

// renderLegacyTest produces the historical test_{ID}.py shape used by this
// repo since 2018:
//
//	from Naive{ID} import Solution as Naive
//
//	testcases = [...]
//
//	def test_Naive():
//	    sol = Naive()
//	    for inputs, expected in testcases:
//	        assert sol.<method>(*inputs) == expected
//
// The method name isn't known at scaffold time, so we leave a TODO comment
// in the assert line — the user fills it in after seeing the LeetCode
// signature.
const legacyTestTmpl = `from {{ .Strategy }}{{ .ID }} import Solution as {{ .Strategy }}

# Sample testcases from LeetCode. Replace the second tuple entry with the
# expected output. Add more cases — including failed-submission inputs —
# below.
testcases = [
{{- range .Samples }}
    ({{ . }}, None),  # TODO: fill expected
{{- end }}
]


def test_{{ .Strategy }}():
    sol = {{ .Strategy }}()
    for inputs, expected in testcases:
        # TODO: invoke the actual method, e.g. sol.solve(*inputs) == expected
        assert expected is None or expected == expected
`

func renderLegacyTest(_ config.LayoutSpec, c tmplCtx) (string, error) {
	wrapped := tmplCtx{
		ID:       c.ID,
		Title:    c.Title,
		Strategy: c.Strategy,
		Samples:  wrapSamples(c.Samples),
	}
	return render("legacy_test", legacyTestTmpl, wrapped)
}
