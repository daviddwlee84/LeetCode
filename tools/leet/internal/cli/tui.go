package cli

import (
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/tui"
	"github.com/spf13/cobra"
)

func newTUICmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "tui",
		Short: "Launch the interactive Bubble Tea UI",
		RunE: func(cmd *cobra.Command, _ []string) error {
			return tui.Run(cmd.Context())
		},
	}
	return cmd
}
