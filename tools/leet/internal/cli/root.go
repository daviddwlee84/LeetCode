package cli

import (
	"github.com/spf13/cobra"
)

// version is set at build time via -ldflags "-X .../cli.version=...".
var version = "dev"

// Root returns the cobra root command with all subcommands attached.
func Root() *cobra.Command {
	root := &cobra.Command{
		Use:   "leet",
		Short: "LeetCode practice helper for the local repo",
		Long: `leet fetches LeetCode daily / contest problems, scaffolds the
standard Python3/{Category}/{ProblemName}/ folder, opens $EDITOR, runs the
local pytest, submits to LeetCode, and records failed cases.

Run 'leet auth' first to set cookies.`,
		Version:       version,
		SilenceUsage:  true,
		SilenceErrors: true,
	}

	root.AddCommand(
		newInitCmd(),
		newAuthCmd(),
		newDailyCmd(),
		newContestCmd(),
		newSubmitCmd(),
		newTestCmd(),
		newReadmeCmd(),
		newTUICmd(),
	)
	return root
}
