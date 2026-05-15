// Package editor launches $EDITOR on a file. Used by `leet daily` after
// scaffolding so the user lands directly in the new Solution.py.
package editor

import (
	"errors"
	"os"
	"os/exec"
)

// Launch runs $EDITOR (fallback nvim, then vi) on path, attached to the
// current terminal. Returns nil if the editor exits 0.
func Launch(path string) error {
	bin := pickEditor()
	if bin == "" {
		return errors.New("no editor found ($EDITOR unset and neither nvim nor vi on PATH)")
	}
	cmd := exec.Command(bin, path)
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	return cmd.Run()
}

// Command builds the *exec.Cmd for $EDITOR + path without running it. Used by
// the Bubble Tea TUI which wraps it in tea.ExecProcess to suspend/restore the
// alt-screen.
func Command(path string) *exec.Cmd {
	bin := pickEditor()
	if bin == "" {
		return nil
	}
	return exec.Command(bin, path)
}

func pickEditor() string {
	if e := os.Getenv("EDITOR"); e != "" {
		if p, err := exec.LookPath(e); err == nil {
			return p
		}
	}
	for _, candidate := range []string{"nvim", "vim", "vi"} {
		if p, err := exec.LookPath(candidate); err == nil {
			return p
		}
	}
	return ""
}
