package scaffold

import (
	"strings"
	"unicode"
)

// PascalCase converts a LeetCode problem title to the folder-name convention
// the repo has used since 2018.
//
// Examples (all from the actual repo):
//
//	"Two Sum"               -> "TwoSum"
//	"Power of Four"         -> "PowerOfFour"
//	"Matrix Diagonal Sum"   -> "MatrixDiagonalSum"
//	"3Sum Closest"          -> "3SumClosest"
//	"Pow(x, n)"             -> "PowXN"     // existing folder PowXN
//	"Implement strStr()"    -> "Implement_strStr"  // edge — left as-is
//
// We don't try to perfectly match every historical folder name (some are
// idiosyncratic, like "Implement_strStr"); we just produce a sane,
// alphanumeric PascalCase string. The user can always pass --folder-name to
// override (TODO).
func PascalCase(title string) string {
	var b strings.Builder
	b.Grow(len(title))
	upNext := true
	for _, r := range title {
		switch {
		case unicode.IsLetter(r) || unicode.IsDigit(r):
			if upNext && unicode.IsLetter(r) {
				b.WriteRune(unicode.ToUpper(r))
			} else {
				b.WriteRune(r)
			}
			upNext = false
		default:
			// Any non-alphanumeric flips the next letter to upper, but
			// emits nothing.
			upNext = true
		}
	}
	return b.String()
}
