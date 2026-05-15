package config

import (
	"os"
	"path/filepath"
	"testing"
)

func TestDefaults(t *testing.T) {
	c := Defaults()
	if c.DefaultLayout != "legacy" {
		t.Errorf("default layout = %q, want legacy", c.DefaultLayout)
	}
	if len(c.Categories) != 12 {
		t.Errorf("default categories count = %d, want 12", len(c.Categories))
	}
	if c.Layouts.Legacy.SolutionPattern != "{strategy}{id}.py" {
		t.Errorf("legacy solution pattern = %q", c.Layouts.Legacy.SolutionPattern)
	}
	if c.Layouts.Structured.SolutionPattern != "{strategy_snake}.py" {
		t.Errorf("structured solution pattern = %q", c.Layouts.Structured.SolutionPattern)
	}
}

func TestLoad_noFiles(t *testing.T) {
	tmp := t.TempDir()
	// Steer UserConfigDir to a fresh tmp so we don't pick up the real user's.
	withUserConfigDir(t, tmp)
	c, err := Load(tmp)
	if err != nil {
		t.Fatal(err)
	}
	if c.Layout != "legacy" {
		t.Errorf("Layout (no override) = %q, want legacy (from DefaultLayout)", c.Layout)
	}
}

func TestLoad_perRepoOverlay(t *testing.T) {
	tmp := t.TempDir()
	withUserConfigDir(t, tmp)
	writeFile(t, filepath.Join(tmp, ".leet/config.toml"), `layout = "structured"`)

	c, err := Load(tmp)
	if err != nil {
		t.Fatal(err)
	}
	if c.Layout != "structured" {
		t.Errorf("per-repo Layout = %q, want structured", c.Layout)
	}
	// Defaults should still be intact for everything else.
	if len(c.Categories) != 12 {
		t.Errorf("categories overridden unexpectedly: %v", c.Categories)
	}
}

func TestLoad_userThenRepoOverlay(t *testing.T) {
	tmp := t.TempDir()
	withUserConfigDir(t, tmp)
	// User config sets default_layout=structured.
	writeFile(t, filepath.Join(tmp, "leet/config.toml"), `default_layout = "structured"`)
	// Repo config sets layout=legacy (per-repo wins).
	repo := t.TempDir()
	writeFile(t, filepath.Join(repo, ".leet/config.toml"), `layout = "legacy"`)

	c, err := Load(repo)
	if err != nil {
		t.Fatal(err)
	}
	if c.Layout != "legacy" {
		t.Errorf("Layout = %q, want legacy (per-repo wins)", c.Layout)
	}
	if c.DefaultLayout != "structured" {
		t.Errorf("DefaultLayout = %q, want structured (from user-level)", c.DefaultLayout)
	}
}

func TestLayoutMap_Get(t *testing.T) {
	c := Defaults()
	if got := c.Layouts.Get("legacy"); got.SolutionPattern == "" {
		t.Error("legacy spec empty after Get")
	}
	if got := c.Layouts.Get("structured"); got.SolutionPattern == "" {
		t.Error("structured spec empty after Get")
	}
	// Unknown layout falls back to legacy (safest).
	if got := c.Layouts.Get("unknown"); got.SolutionPattern != "{strategy}{id}.py" {
		t.Errorf("unknown layout fallback got %q, want legacy", got.SolutionPattern)
	}
}

func TestExpand(t *testing.T) {
	v := PatternVars{
		Title:    "Matrix Diagonal Sum",
		Strategy: "HashTable",
		ID:       "1572",
	}
	cases := map[string]string{
		"{title_pascal}":        "MatrixDiagonalSum",
		"{title_kebab}":         "matrix-diagonal-sum",
		"{title_snake}":         "matrix_diagonal_sum",
		"{strategy}{id}.py":     "HashTable1572.py",
		"{strategy_snake}.py":   "hash_table.py",
		"{strategy_camel}.py":   "HashTable.py",
		"test_{id}.py":          "test_1572.py",
		"test.py":               "test.py", // no tokens
		"Note{id}.md":           "Note1572.md",
		"{title_kebab}/{id}":    "matrix-diagonal-sum/1572",
		"":                      "",
		"{unknown}":             "{unknown}", // unknown tokens pass through
	}
	for pat, want := range cases {
		if got := Expand(pat, v); got != want {
			t.Errorf("Expand(%q) = %q, want %q", pat, got, want)
		}
	}
}

func TestCaseConverters(t *testing.T) {
	cases := []struct {
		in, pascal, kebab, snake string
	}{
		{"Two Sum", "TwoSum", "two-sum", "two_sum"},
		{"Matrix Diagonal Sum", "MatrixDiagonalSum", "matrix-diagonal-sum", "matrix_diagonal_sum"},
		{"HashTable", "HashTable", "hash-table", "hash_table"},
		{"hash_table", "HashTable", "hash-table", "hash_table"},
		{"hash-table", "HashTable", "hash-table", "hash_table"},
		{"Naive", "Naive", "naive", "naive"},
		{"3Sum", "3Sum", "3sum", "3sum"},
		{"Pow(x, n)", "PowXN", "pow-x-n", "pow_x_n"},
		{"", "", "", ""},
	}
	for _, c := range cases {
		if got := PascalCase(c.in); got != c.pascal {
			t.Errorf("PascalCase(%q) = %q, want %q", c.in, got, c.pascal)
		}
		if got := KebabCase(c.in); got != c.kebab {
			t.Errorf("KebabCase(%q) = %q, want %q", c.in, got, c.kebab)
		}
		if got := SnakeCase(c.in); got != c.snake {
			t.Errorf("SnakeCase(%q) = %q, want %q", c.in, got, c.snake)
		}
	}
}

func TestApplyCategoryCase(t *testing.T) {
	if got := ApplyCategoryCase("Array", ""); got != "Array" {
		t.Errorf("preserve mode broke: %q", got)
	}
	if got := ApplyCategoryCase("BinaryTree", "lower"); got != "binary-tree" {
		t.Errorf("lower mode: got %q, want binary-tree", got)
	}
}

// --- test helpers ---

func writeFile(t *testing.T, path, body string) {
	t.Helper()
	if err := os.MkdirAll(filepath.Dir(path), 0o755); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(path, []byte(body), 0o644); err != nil {
		t.Fatal(err)
	}
}

// withUserConfigDir overrides the package-level userConfigPath function so
// tests don't pick up the developer's real ~/.config/leet/config.toml.
func withUserConfigDir(t *testing.T, dir string) {
	t.Helper()
	prev := userConfigPath
	userConfigPath = func() (string, error) {
		return filepath.Join(dir, "leet", "config.toml"), nil
	}
	t.Cleanup(func() { userConfigPath = prev })
}
