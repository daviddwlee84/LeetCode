package scaffold

import (
	"os"
	"path/filepath"
	"strings"
	"testing"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/config"
)

// TestInitRepo_legacy verifies the legacy layout output: PascalCase
// category folders, .leet/config.toml with layout = "legacy".
func TestInitRepo_legacy(t *testing.T) {
	tmp := t.TempDir()
	cfg := config.Defaults()
	created, err := InitRepo(cfg, InitOpts{
		Target:        tmp,
		Layout:        "legacy",
		Name:          "test-repo",
		InitGit:       false,
		WithAgents:    true,
		WithPyproject: true,
	})
	if err != nil {
		t.Fatal(err)
	}
	if len(created) == 0 {
		t.Fatal("InitRepo created nothing")
	}
	mustExist(t, tmp, ".leet/config.toml")
	mustExist(t, tmp, "Python3/Array/.gitkeep")
	mustExist(t, tmp, "Python3/BinaryTree/.gitkeep")
	mustExist(t, tmp, "Python3/DynamicProgramming/.gitkeep")
	mustExist(t, tmp, "AGENTS.md")
	mustExist(t, tmp, "pyproject.toml")
	mustExist(t, tmp, ".claude/settings.json")

	assertSymlink(t, filepath.Join(tmp, "CLAUDE.md"), "AGENTS.md")
	assertSymlink(t, filepath.Join(tmp, ".claude/skills"), "../.agents/skills")

	cfgBody, _ := os.ReadFile(filepath.Join(tmp, ".leet/config.toml"))
	if !strings.Contains(string(cfgBody), `layout = "legacy"`) {
		t.Errorf(".leet/config.toml missing legacy layout pin: %s", cfgBody)
	}
}

// TestInitRepo_structured asserts kebab-case lowercase category folders
// and the structured layout pin.
func TestInitRepo_structured(t *testing.T) {
	tmp := t.TempDir()
	cfg := config.Defaults()
	_, err := InitRepo(cfg, InitOpts{
		Target:        tmp,
		Layout:        "structured",
		Name:          "demo",
		InitGit:       false,
		WithAgents:    true,
		WithPyproject: true,
	})
	if err != nil {
		t.Fatal(err)
	}
	mustExist(t, tmp, "Python3/array/.gitkeep")
	mustExist(t, tmp, "Python3/binary-tree/.gitkeep")
	mustExist(t, tmp, "Python3/dynamic-programming/.gitkeep")
	mustExist(t, tmp, "Python3/ad-hoc/.gitkeep")
	// PascalCase folders should NOT appear in readdir output. We check via
	// readdir (not os.Stat) because macOS HFS+/APFS are case-insensitive
	// by default — stat("Python3/Array") would succeed even if the actual
	// dir name on disk is "array".
	entries, err := os.ReadDir(filepath.Join(tmp, "Python3"))
	if err != nil {
		t.Fatal(err)
	}
	for _, e := range entries {
		if e.Name() == "Array" || e.Name() == "BinaryTree" || e.Name() == "DynamicProgramming" {
			t.Errorf("structured layout produced PascalCase folder %q in readdir", e.Name())
		}
	}

	cfgBody, _ := os.ReadFile(filepath.Join(tmp, ".leet/config.toml"))
	if !strings.Contains(string(cfgBody), `layout = "structured"`) {
		t.Errorf(".leet/config.toml missing structured layout pin: %s", cfgBody)
	}
}

// TestInitRepo_refusesExisting checks that init doesn't clobber a repo
// that already has a .leet/ directory (unless --force).
func TestInitRepo_refusesExisting(t *testing.T) {
	tmp := t.TempDir()
	if err := os.MkdirAll(filepath.Join(tmp, ".leet"), 0o755); err != nil {
		t.Fatal(err)
	}
	cfg := config.Defaults()
	_, err := InitRepo(cfg, InitOpts{Target: tmp, Layout: "structured"})
	if err == nil {
		t.Fatal("expected error when .leet/ exists without --force")
	}
	if !strings.Contains(err.Error(), "already exists") {
		t.Errorf("error message unhelpful: %v", err)
	}

	// With --force it should proceed.
	_, err = InitRepo(cfg, InitOpts{Target: tmp, Layout: "structured", Force: true})
	if err != nil {
		t.Fatalf("--force should allow overlay: %v", err)
	}
}

// TestInitRepo_dailyEndToEnd combines init + Daily on the resulting repo,
// using a stub leetcode.Question (so we don't hit the live API).
func TestInitRepo_dailyEndToEnd_structured(t *testing.T) {
	tmp := t.TempDir()
	cfg := config.Defaults()
	if _, err := InitRepo(cfg, InitOpts{
		Target:     tmp,
		Layout:     "structured",
		WithAgents: false, // keep test focused
	}); err != nil {
		t.Fatal(err)
	}

	// Reload config — should now resolve to layout=structured (from per-repo).
	cfg2, err := config.Load(tmp)
	if err != nil {
		t.Fatal(err)
	}
	if cfg2.Layout != "structured" {
		t.Fatalf("post-init Load: Layout = %q, want structured", cfg2.Layout)
	}

	// Stub a problem.
	folder := ProblemFolder(cfg2, tmp, "array", "Matrix Diagonal Sum")
	in := Inputs{
		Folder:     folder,
		ID:         "1572",
		Title:      "Matrix Diagonal Sum",
		Difficulty: "Easy",
		URL:        "https://leetcode.com/problems/matrix-diagonal-sum/",
		TitleSlug:  "matrix-diagonal-sum",
		ContentMD:  "Find the matrix diagonal sum.",
		Samples:    []string{"[[1,2,3],[4,5,6],[7,8,9]]"},
		Tags:       []string{"Array"},
		Strategy:   "Naive",
		WithNote:   true,
	}
	_, err = Daily(cfg2, in)
	if err != nil {
		t.Fatal(err)
	}
	mustExist(t, folder, "naive.py")
	mustExist(t, folder, "test.py")
	mustExist(t, folder, "README.md")
	mustExist(t, folder, "meta.json")

	// Sanity: folder name is kebab-case.
	if filepath.Base(folder) != "matrix-diagonal-sum" {
		t.Errorf("structured folder = %q, want matrix-diagonal-sum", filepath.Base(folder))
	}

	// Sanity: meta.json contains the strategy with kind=own.
	m, err := ReadMeta(filepath.Join(folder, "meta.json"))
	if err != nil {
		t.Fatal(err)
	}
	if len(m.Strategies) != 1 {
		t.Fatalf("strategies count = %d, want 1", len(m.Strategies))
	}
	if m.Strategies[0].Kind != "own" {
		t.Errorf("initial strategy kind = %q, want own", m.Strategies[0].Kind)
	}
	if m.Strategies[0].File != "naive.py" {
		t.Errorf("initial strategy file = %q, want naive.py", m.Strategies[0].File)
	}
}

// TestInitRepo_dailyEndToEnd_legacy is the regression test for the
// existing repo: layout=legacy must produce Naive{ID}.py and test_{ID}.py
// exactly as Phase 1 did.
func TestInitRepo_dailyEndToEnd_legacy(t *testing.T) {
	tmp := t.TempDir()
	cfg := config.Defaults()
	if _, err := InitRepo(cfg, InitOpts{
		Target:     tmp,
		Layout:     "legacy",
		WithAgents: false,
	}); err != nil {
		t.Fatal(err)
	}
	cfg2, err := config.Load(tmp)
	if err != nil {
		t.Fatal(err)
	}
	if cfg2.Layout != "legacy" {
		t.Fatalf("post-init Layout = %q, want legacy", cfg2.Layout)
	}

	folder := ProblemFolder(cfg2, tmp, "Array", "Matrix Diagonal Sum")
	if filepath.Base(folder) != "MatrixDiagonalSum" {
		t.Errorf("legacy folder name = %q, want MatrixDiagonalSum", filepath.Base(folder))
	}
	_, err = Daily(cfg2, Inputs{
		Folder:   folder,
		ID:       "1572",
		Title:    "Matrix Diagonal Sum",
		Strategy: "Naive",
		Samples:  []string{"[[1,2,3],[4,5,6]]"},
	})
	if err != nil {
		t.Fatal(err)
	}
	mustExist(t, folder, "Naive1572.py")
	mustExist(t, folder, "test_1572.py")
	// Legacy does NOT write meta.json.
	if _, err := os.Stat(filepath.Join(folder, "meta.json")); err == nil {
		t.Error("legacy layout should not write meta.json")
	}

	// Test file must use the legacy `from Naive1572 import` import shape.
	testBody, _ := os.ReadFile(filepath.Join(folder, "test_1572.py"))
	if !strings.Contains(string(testBody), "from Naive1572 import Solution as Naive") {
		t.Errorf("legacy test missing expected import:\n%s", testBody)
	}
}

// --- helpers ---

func mustExist(t *testing.T, base, rel string) {
	t.Helper()
	p := filepath.Join(base, rel)
	if _, err := os.Stat(p); err != nil {
		t.Errorf("expected %s to exist: %v", rel, err)
	}
}

func assertSymlink(t *testing.T, path, wantTarget string) {
	t.Helper()
	info, err := os.Lstat(path)
	if err != nil {
		t.Errorf("lstat %s: %v", path, err)
		return
	}
	if info.Mode()&os.ModeSymlink == 0 {
		t.Errorf("%s is not a symlink", path)
		return
	}
	target, err := os.Readlink(path)
	if err != nil {
		t.Errorf("readlink %s: %v", path, err)
		return
	}
	if target != wantTarget {
		t.Errorf("%s -> %q, want %q", path, target, wantTarget)
	}
}
