package readme

import (
	"strings"
	"testing"
)

func TestRow_basic(t *testing.T) {
	row := Row(Input{
		ID:         "1572",
		Title:      "Matrix Diagonal Sum",
		Difficulty: "Easy",
		Date:       "2026/5/15",
		Category:   "Array, Math",
		Solutions: []Solution{
			{Method: "Naive", TimeStr: "O(n)", RelPath: "Python3/Array/MatrixDiagonalSum/Naive1572.py"},
			{Method: "Better", TimeStr: "O(n)", RelPath: "Python3/Array/MatrixDiagonalSum/Better1572.py"},
		},
		NotePath: "Python3/Array/MatrixDiagonalSum/Note1572.md",
	})

	wants := []string{
		"1572",
		"Easy",
		"[Matrix Diagonal Sum](https://leetcode.com/problems/matrix-diagonal-sum/)",
		"2026/5/15",
		"Array, Math",
		"[Naive-O(n)](Python3/Array/MatrixDiagonalSum/Naive1572.py)",
		"[Better-O(n)](Python3/Array/MatrixDiagonalSum/Better1572.py)",
		"[Note](Python3/Array/MatrixDiagonalSum/Note1572.md)",
	}
	for _, w := range wants {
		if !strings.Contains(row, w) {
			t.Errorf("row missing %q\nrow: %s", w, row)
		}
	}
}

func TestRow_noNote(t *testing.T) {
	row := Row(Input{
		ID: "342", Title: "Power of Four", Difficulty: "Easy", Date: "2026/5/14",
		Category: "Math",
		Solutions: []Solution{{Method: "Naive", TimeStr: "O(logn)", RelPath: "Python3/Math/PowerOfFour/Naive342.py"}},
	})
	if !strings.Contains(row, "|-|-") {
		// Last 2 columns: remark "-" and TODO "-"
		t.Errorf("expected dash remark + dash TODO when no note, got: %s", row)
	}
}

func TestSlugify(t *testing.T) {
	cases := map[string]string{
		"Two Sum":                 "two-sum",
		"Matrix Diagonal Sum":     "matrix-diagonal-sum",
		"Pow(x, n)":               "pow-x-n",
		"3Sum":                    "3sum",
		"  leading/trailing  ":    "leading-trailing",
	}
	for in, want := range cases {
		if got := slugify(in); got != want {
			t.Errorf("slugify(%q) = %q, want %q", in, got, want)
		}
	}
}
