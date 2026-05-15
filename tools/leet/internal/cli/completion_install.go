package cli

import (
	"errors"
	"fmt"
	"os"
	"path/filepath"
	"strings"

	"github.com/spf13/cobra"
)

// registerCompletionInstall attaches an "install" subcommand under cobra's
// generated `completion` command. We call this from Root() once all
// subcommands are wired up so cobra has already registered `completion`.
func registerCompletionInstall(root *cobra.Command) {
	var completionCmd *cobra.Command
	for _, c := range root.Commands() {
		if c.Name() == "completion" {
			completionCmd = c
			break
		}
	}
	if completionCmd == nil {
		return // cobra didn't add it for some reason; not fatal
	}
	completionCmd.AddCommand(newCompletionInstallCmd(root))
}

func newCompletionInstallCmd(root *cobra.Command) *cobra.Command {
	var (
		shellFlag string
		printOnly bool
		homeFlag  string
	)
	cmd := &cobra.Command{
		Use:   "install",
		Short: "Write the shell completion script to its conventional location",
		Long: `Detects $SHELL (or use --shell) and writes the completion script
to a path the shell auto-loads:

  zsh   → ~/.zfunc/_leet   (needs fpath=(~/.zfunc $fpath) in .zshrc)
  bash  → ~/.bash_completion.d/leet
  fish  → ~/.config/fish/completions/leet.fish

--print writes to stdout instead.`,
		RunE: func(cmd *cobra.Command, _ []string) error {
			shell := shellFlag
			if shell == "" {
				shell = detectShell()
			}
			if shell == "" {
				return errors.New("could not detect shell; pass --shell=zsh|bash|fish")
			}

			if printOnly {
				return writeCompletion(shell, root, os.Stdout)
			}

			home := homeFlag
			if home == "" {
				h, err := os.UserHomeDir()
				if err != nil {
					return err
				}
				home = h
			}
			path, hint, err := completionTargetPath(shell, home)
			if err != nil {
				return err
			}
			if err := os.MkdirAll(filepath.Dir(path), 0o755); err != nil {
				return err
			}
			f, err := os.Create(path)
			if err != nil {
				return err
			}
			defer f.Close()
			if err := writeCompletion(shell, root, f); err != nil {
				return err
			}
			fmt.Fprintf(os.Stderr, "✓ wrote %s completion → %s\n", shell, path)
			if hint != "" {
				fmt.Fprintln(os.Stderr, hint)
			}
			fmt.Fprintln(os.Stderr, "reload your shell (or run `exec "+shell+"`) to activate.")
			return nil
		},
	}
	cmd.Flags().StringVar(&shellFlag, "shell", "", "shell to target (zsh|bash|fish); default: detect")
	cmd.Flags().BoolVar(&printOnly, "print", false, "print to stdout instead of writing")
	cmd.Flags().StringVar(&homeFlag, "home", "", "override HOME directory (for tests)")
	return cmd
}

// detectShell guesses from $SHELL. Returns "" if it can't tell.
func detectShell() string {
	sh := os.Getenv("SHELL")
	switch {
	case strings.Contains(sh, "zsh"):
		return "zsh"
	case strings.Contains(sh, "bash"):
		return "bash"
	case strings.Contains(sh, "fish"):
		return "fish"
	}
	return ""
}

// completionTargetPath returns (path, hint) where hint is an optional
// shell-rc note to print if the target location may not be auto-sourced.
func completionTargetPath(shell, home string) (string, string, error) {
	switch shell {
	case "zsh":
		hint := "ensure your .zshrc has:\n  fpath=(~/.zfunc $fpath)\n  autoload -U compinit; compinit"
		return filepath.Join(home, ".zfunc", "_leet"), hint, nil
	case "bash":
		// Prefer XDG location if user-bashrc style is set; else fall back.
		if xdg := os.Getenv("XDG_DATA_HOME"); xdg != "" {
			return filepath.Join(xdg, "bash-completion", "completions", "leet"), "", nil
		}
		return filepath.Join(home, ".bash_completion.d", "leet"), "ensure your .bashrc sources ~/.bash_completion.d/*", nil
	case "fish":
		return filepath.Join(home, ".config", "fish", "completions", "leet.fish"), "", nil
	default:
		return "", "", fmt.Errorf("unsupported shell %q", shell)
	}
}

func writeCompletion(shell string, root *cobra.Command, out interface{ Write([]byte) (int, error) }) error {
	switch shell {
	case "zsh":
		return root.GenZshCompletion(out)
	case "bash":
		return root.GenBashCompletion(out)
	case "fish":
		return root.GenFishCompletion(out, true)
	default:
		return fmt.Errorf("unsupported shell %q", shell)
	}
}
