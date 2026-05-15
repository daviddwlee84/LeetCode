package scaffold

import "testing"

func TestPascalCase(t *testing.T) {
	cases := map[string]string{
		"Two Sum":             "TwoSum",
		"Power of Four":       "PowerOfFour",
		"Matrix Diagonal Sum": "MatrixDiagonalSum",
		"3Sum":                "3Sum",
		"3Sum Closest":        "3SumClosest",
		"Pow(x, n)":           "PowXN",
		"Add Two Numbers":     "AddTwoNumbers",
		"  leading spaces  ":  "LeadingSpaces",
		"":                    "",
	}
	for in, want := range cases {
		if got := PascalCase(in); got != want {
			t.Errorf("PascalCase(%q) = %q, want %q", in, got, want)
		}
	}
}
