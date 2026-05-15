package config

import (
	"strings"
	"unicode"
)

// PatternVars holds every value a layout pattern can substitute. Callers fill
// in the fields they have (e.g. scaffold passes Title + Strategy + ID; the
// folder pattern uses Title and ID, the solution pattern adds Strategy).
type PatternVars struct {
	Title    string // raw LeetCode title, e.g. "Matrix Diagonal Sum"
	Strategy string // canonical method label, e.g. "HashTable" / "Naive"
	ID       string // questionFrontendId, e.g. "1572"
}

// Expand substitutes the tokens listed below into pattern. Unknown tokens
// pass through unchanged so we can diagnose misconfiguration easily.
//
//	{title}          - raw title              "Matrix Diagonal Sum"
//	{title_pascal}   - PascalCase             "MatrixDiagonalSum"
//	{title_kebab}    - kebab-case / slug      "matrix-diagonal-sum"
//	{title_snake}    - snake_case             "matrix_diagonal_sum"
//	{strategy}       - raw strategy           "HashTable"
//	{strategy_snake} - snake_case strategy    "hash_table"
//	{strategy_kebab} - kebab strategy         "hash-table"
//	{strategy_camel} - PascalCase strategy    "HashTable" (no-op for already-pascal)
//	{id}             - frontend ID            "1572"
func Expand(pattern string, v PatternVars) string {
	if pattern == "" {
		return ""
	}
	r := strings.NewReplacer(
		"{title}", v.Title,
		"{title_pascal}", PascalCase(v.Title),
		"{title_kebab}", KebabCase(v.Title),
		"{title_snake}", SnakeCase(v.Title),
		"{strategy}", v.Strategy,
		"{strategy_snake}", SnakeCase(v.Strategy),
		"{strategy_kebab}", KebabCase(v.Strategy),
		"{strategy_camel}", PascalCase(v.Strategy),
		"{id}", v.ID,
	)
	return r.Replace(pattern)
}

// ApplyCategoryCase lowercases (or otherwise transforms) a category folder
// name per LayoutSpec.CategoryCase. Empty mode = preserve as given.
func ApplyCategoryCase(name, mode string) string {
	switch mode {
	case "lower":
		return KebabCase(name)
	case "snake":
		return SnakeCase(name)
	case "":
		return name
	default:
		return name
	}
}

// ---- case conversion ----
//
// All three converters share the same word-splitting logic: collect runs of
// alphanumeric characters and treat case-boundaries inside a word as
// additional split points (so "HashTable" → ["Hash", "Table"]).

func splitWords(s string) []string {
	var (
		words   []string
		current []rune
	)
	flush := func() {
		if len(current) > 0 {
			words = append(words, string(current))
			current = current[:0]
		}
	}
	prevLower := false
	for _, r := range s {
		switch {
		case unicode.IsUpper(r):
			if prevLower {
				flush()
			}
			current = append(current, r)
			prevLower = false
		case unicode.IsLower(r), unicode.IsDigit(r):
			current = append(current, r)
			prevLower = unicode.IsLower(r)
		default:
			flush()
			prevLower = false
		}
	}
	flush()
	return words
}

// PascalCase: "Matrix Diagonal Sum" → "MatrixDiagonalSum". Idempotent on
// already-pascal input.
func PascalCase(s string) string {
	var b strings.Builder
	for _, w := range splitWords(s) {
		b.WriteString(capitalize(w))
	}
	return b.String()
}

// KebabCase: "Matrix Diagonal Sum" → "matrix-diagonal-sum".
func KebabCase(s string) string {
	parts := splitWords(s)
	for i, w := range parts {
		parts[i] = strings.ToLower(w)
	}
	return strings.Join(parts, "-")
}

// SnakeCase: "Matrix Diagonal Sum" → "matrix_diagonal_sum".
func SnakeCase(s string) string {
	parts := splitWords(s)
	for i, w := range parts {
		parts[i] = strings.ToLower(w)
	}
	return strings.Join(parts, "_")
}

// capitalize uppercases the first letter rune of w and leaves the rest
// alone. We don't blindly lowercase the tail because:
//   - "3Sum" must remain "3Sum" (the existing repo folder), not "3sum"
//   - mixed-case inputs like "HashTable" are already correctly cased
//     after splitWords (each word is one chunk)
//
// Inputs that are all-uppercase (e.g. "MYSQL") will stay all-uppercase
// after PascalCase — acceptable for this repo's title conventions.
func capitalize(w string) string {
	if w == "" {
		return ""
	}
	runes := []rune(w)
	for i := 0; i < len(runes); i++ {
		if unicode.IsLetter(runes[i]) {
			runes[i] = unicode.ToUpper(runes[i])
			return string(runes)
		}
	}
	return string(runes)
}
