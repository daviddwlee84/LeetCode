package cli

import (
	"path/filepath"
	"testing"
)

func TestCompletionTargetPath(t *testing.T) {
	home := "/tmp/fakehome"
	cases := []struct {
		shell string
		want  string
	}{
		{"zsh", filepath.Join(home, ".zfunc", "_leet")},
		{"bash", filepath.Join(home, ".bash_completion.d", "leet")},
		{"fish", filepath.Join(home, ".config", "fish", "completions", "leet.fish")},
	}
	for _, c := range cases {
		t.Run(c.shell, func(t *testing.T) {
			t.Setenv("XDG_DATA_HOME", "") // ensure default path
			got, _, err := completionTargetPath(c.shell, home)
			if err != nil {
				t.Fatal(err)
			}
			if got != c.want {
				t.Errorf("path = %q, want %q", got, c.want)
			}
		})
	}
}

func TestCompletionTargetPath_unsupported(t *testing.T) {
	if _, _, err := completionTargetPath("powershell", "/tmp"); err == nil {
		t.Error("expected error for unsupported shell")
	}
}

func TestDetectShell(t *testing.T) {
	cases := map[string]string{
		"/bin/zsh":              "zsh",
		"/opt/homebrew/bin/zsh": "zsh",
		"/bin/bash":             "bash",
		"/usr/bin/fish":         "fish",
		"":                      "",
		"/bin/dash":             "",
	}
	for sh, want := range cases {
		t.Run(sh, func(t *testing.T) {
			t.Setenv("SHELL", sh)
			if got := detectShell(); got != want {
				t.Errorf("SHELL=%q → %q, want %q", sh, got, want)
			}
		})
	}
}
