package cli

import (
	"errors"
	"os"
	"path/filepath"
)

// findRepoRoot walks up from the current working directory looking for a
// `.git` directory. We use this to anchor scaffolded folders under
// Python3/{Category}/ regardless of where the user invoked `leet`.
func findRepoRoot() (string, error) {
	dir, err := os.Getwd()
	if err != nil {
		return "", err
	}
	for {
		if info, err := os.Stat(filepath.Join(dir, ".git")); err == nil && info.IsDir() {
			return dir, nil
		}
		parent := filepath.Dir(dir)
		if parent == dir {
			return "", errors.New("not inside a git repo (use --repo-root to override)")
		}
		dir = parent
	}
}
