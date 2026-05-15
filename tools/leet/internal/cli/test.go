package cli

import (
	"os"
	"os/exec"
	"path/filepath"

	"github.com/spf13/cobra"
)

func newTestCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "test [path]",
		Short: "Run pytest in a problem folder (or current directory)",
		Args:  cobra.MaximumNArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			dir := "."
			if len(args) == 1 {
				info, err := os.Stat(args[0])
				if err != nil {
					return err
				}
				if info.IsDir() {
					dir = args[0]
				} else {
					dir = filepath.Dir(args[0])
				}
			}
			pyt := exec.CommandContext(cmd.Context(), "pytest", "-v")
			pyt.Dir = dir
			pyt.Stdout = os.Stdout
			pyt.Stderr = os.Stderr
			pyt.Stdin = os.Stdin
			return pyt.Run()
		},
	}
	return cmd
}
