package cli

import (
	"fmt"
	"path/filepath"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/config"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/scaffold"
	"github.com/spf13/cobra"
)

func newInitCmd() *cobra.Command {
	var (
		layout        string
		name          string
		noGit         bool
		noAgents      bool
		noPyproject   bool
		force         bool
	)
	cmd := &cobra.Command{
		Use:   "init [target-dir]",
		Short: "Bootstrap a fresh LeetCode practice repo",
		Long: `Create the standard folder skeleton + config files for a new
practice repo. Choose the layout (legacy / structured) — the resulting
.leet/config.toml pins it so leet daily/contest follow the same rules
every run.

Defaults: WithAgents = true (creates AGENTS.md + .agents/ + symlinks),
WithPyproject = true (creates pyproject.toml).`,
		Args: cobra.MaximumNArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			target := "."
			if len(args) == 1 {
				target = args[0]
			}
			abs, err := filepath.Abs(target)
			if err != nil {
				return err
			}

			// Use user-level config for defaults; per-repo config doesn't exist yet
			// inside a freshly-init'd dir.
			cfg, err := config.Load("")
			if err != nil {
				return err
			}

			opts := scaffold.InitOpts{
				Target:        abs,
				Layout:        layout,
				Name:          name,
				InitGit:       !noGit,
				WithAgents:    !noAgents,
				WithPyproject: !noPyproject,
				Force:         force,
			}
			created, err := scaffold.InitRepo(cfg, opts)
			if err != nil {
				return err
			}
			effective := opts.Layout
			if effective == "" {
				effective = cfg.DefaultLayout
				if effective == "" {
					effective = "structured"
				}
			}
			fmt.Printf("✓ initialized %s (layout=%s)\n", abs, effective)
			for _, c := range created {
				fmt.Printf("    + %s\n", c)
			}
			fmt.Printf("\nnext:\n  cd %s\n  leet auth\n  leet daily\n", abs)
			return nil
		},
	}
	cmd.Flags().StringVar(&layout, "layout", "", "layout: legacy | structured (default: from user config or structured)")
	cmd.Flags().StringVar(&name, "name", "", "repo display name (default: target folder name)")
	cmd.Flags().BoolVar(&noGit, "no-git", false, "skip git init")
	cmd.Flags().BoolVar(&noAgents, "no-agents", false, "skip AGENTS.md + .agents/ + symlinks")
	cmd.Flags().BoolVar(&noPyproject, "no-pyproject", false, "skip pyproject.toml")
	cmd.Flags().BoolVar(&force, "force", false, "overlay onto existing .leet/")
	return cmd
}
