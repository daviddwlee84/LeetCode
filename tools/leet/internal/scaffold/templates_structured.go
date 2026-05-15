package scaffold

import (
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/config"
)

// renderStructuredTest produces a single test.py that uses
// pytest.mark.parametrize over every strategy file in the folder. The
// {Strategies} list is left as a manual edit — at scaffold time we only
// know the initial strategy (usually "Naive"); subsequent additions need
// to be appended by the user (or `leet add-strategy` in a future phase).
//
// Example output for a brand-new problem with just the Naive strategy:
//
//	import pytest
//	from naive import Solution as Naive
//
//	STRATEGIES = [Naive]
//	TESTCASES = [
//	    ((<sample-1>,), None),  # TODO: fill expected
//	    ...
//	]
//
//	@pytest.mark.parametrize("sol_cls", STRATEGIES)
//	@pytest.mark.parametrize("inputs,expected", TESTCASES)
//	def test_solution(sol_cls, inputs, expected):
//	    # TODO: replace .solve with the actual method name from LeetCode
//	    assert expected is None or sol_cls().solve(*inputs) == expected
const structuredTestTmpl = `import pytest
from {{ .StrategySnake }} import Solution as {{ .StrategyCamel }}

STRATEGIES = [{{ .StrategyCamel }}]
TESTCASES = [
{{- range .Samples }}
    ({{ . }}, None),  # TODO: fill expected
{{- end }}
]


@pytest.mark.parametrize("sol_cls", STRATEGIES)
@pytest.mark.parametrize("inputs,expected", TESTCASES)
def test_solution(sol_cls, inputs, expected):
    # TODO: replace .solve with the actual method name from LeetCode
    assert expected is None or sol_cls().solve(*inputs) == expected
`

type structuredTmplCtx struct {
	StrategySnake string
	StrategyCamel string
	Samples       []string
}

func renderStructuredTest(_ config.LayoutSpec, c tmplCtx) (string, error) {
	strat := c.Strategy
	if strat == "" {
		strat = "Naive"
	}
	ctx := structuredTmplCtx{
		StrategySnake: config.SnakeCase(strat),
		StrategyCamel: config.PascalCase(strat),
		Samples:       wrapSamples(c.Samples),
	}
	return render("structured_test", structuredTestTmpl, ctx)
}
