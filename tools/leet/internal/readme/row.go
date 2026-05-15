// Package readme renders a single suggested table row matching the README's
// historical format. The MVP only prints — it doesn't write README.md back.
//
// Existing format (see repo README.md ~line 92):
//
//	|Number | Difficulty | Problem | Date | Category | Method-TimeComplexity | Remark | TODO |
//	|👍 001|Easy    |[Two Sum](https://leetcode.com/problems/two-sum/)|2018/3/12|Array, HT|[HT-O(n)](Python3/Array/TwoSum/HashTable001.py)|[Note](Python3/Array/TwoSum/Note001.md)|-|
package readme

import (
	"fmt"
	"strings"
)

type Solution struct {
	Method   string // "Naive", "HashTable", "DP", ...
	TimeStr  string // "O(n)", "O(nlogn)", ...
	RelPath  string // "Python3/Array/TwoSum/Naive001.py"
}

type Input struct {
	ID         string // "1572"
	Title      string // "Matrix Diagonal Sum"
	Difficulty string // "Easy" | "Medium" | "Hard"
	Date       string // "2026/5/15"
	Category   string // "Array, HT" — free form
	Solutions  []Solution
	NotePath   string // "Python3/Array/MatrixDiagonalSum/Note1572.md", optional
}

// Row renders a single markdown row in the README's existing style.
func Row(in Input) string {
	id := padID(in.ID)
	diff := padDifficulty(in.Difficulty)
	probLink := fmt.Sprintf("[%s](https://leetcode.com/problems/%s/)", in.Title, slugify(in.Title))

	methods := make([]string, 0, len(in.Solutions))
	for _, s := range in.Solutions {
		label := s.Method
		if s.TimeStr != "" {
			label = fmt.Sprintf("%s-%s", s.Method, s.TimeStr)
		}
		methods = append(methods, fmt.Sprintf("[%s](%s)", label, s.RelPath))
	}
	methodCol := strings.Join(methods, ", ")

	remark := "-"
	if in.NotePath != "" {
		remark = fmt.Sprintf("[Note](%s)", in.NotePath)
	}

	cat := in.Category
	if cat == "" {
		cat = "-"
	}
	date := in.Date
	if date == "" {
		date = "TODO"
	}

	return fmt.Sprintf("|%s|%s|%s|%s|%s|%s|%s|-",
		id, diff, probLink, date, cat, methodCol, remark)
}

func padID(id string) string {
	for len(id) < 3 {
		id = "0" + id
	}
	return "  " + id
}

func padDifficulty(d string) string {
	switch d {
	case "Easy":
		return "Easy    "
	case "Medium":
		return "Medium  "
	case "Hard":
		return "Hard    "
	default:
		return d
	}
}

// slugify converts "Matrix Diagonal Sum" → "matrix-diagonal-sum". Any
// non-alphanumeric runs collapse into a single dash; "Pow(x, n)" → "pow-x-n".
func slugify(title string) string {
	var b strings.Builder
	b.Grow(len(title))
	prevDash := false
	for _, r := range strings.ToLower(title) {
		switch {
		case r >= 'a' && r <= 'z', r >= '0' && r <= '9':
			b.WriteRune(r)
			prevDash = false
		default:
			if !prevDash {
				b.WriteByte('-')
				prevDash = true
			}
		}
	}
	return strings.Trim(b.String(), "-")
}
