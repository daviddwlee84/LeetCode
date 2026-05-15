package cli

import (
	"fmt"
	"path/filepath"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/auth"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/config"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/leetcode"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/scaffold"
	"github.com/spf13/cobra"
)

func newContestCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "contest",
		Short: "Fetch a LeetCode contest and scaffold its folders",
	}
	cmd.AddCommand(contestSub("weekly", "weekly-contest-"))
	cmd.AddCommand(contestSub("biweekly", "biweekly-contest-"))
	return cmd
}

func contestSub(name, slugPrefix string) *cobra.Command {
	var latest bool
	var repoRoot string
	c := &cobra.Command{
		Use:   name + " [N]",
		Short: "Fetch " + name + " contest",
		Args:  cobra.MaximumNArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			if !latest && len(args) == 0 {
				return fmt.Errorf("provide contest number or --latest")
			}
			creds, _ := auth.Load()
			client := leetcode.NewClient(creds)

			var slug string
			if latest {
				n, err := client.LatestContestNumber(cmd.Context(), name)
				if err != nil {
					return err
				}
				slug = fmt.Sprintf("%s%d", slugPrefix, n)
			} else {
				slug = fmt.Sprintf("%s%s", slugPrefix, args[0])
			}

			contest, err := client.Contest(cmd.Context(), slug)
			if err != nil {
				return fmt.Errorf("fetch %s: %w", slug, err)
			}

			root := repoRoot
			if root == "" {
				r, err := findRepoRoot()
				if err != nil {
					return err
				}
				root = r
			}

			cfg, err := config.Load(root)
			if err != nil {
				return fmt.Errorf("load config: %w", err)
			}

			created, err := scaffold.Contest(cfg, root, contest)
			if err != nil {
				return err
			}
			rel, _ := filepath.Rel(root, contest.LocalDir(root))
			fmt.Printf("✓ %s (%d problems) → %s\n", contest.Title, len(contest.Problems), rel)
			for _, f := range created {
				r, _ := filepath.Rel(root, f)
				fmt.Printf("    + %s\n", r)
			}
			return nil
		},
	}
	c.Flags().BoolVar(&latest, "latest", false, "fetch most recent "+name+" contest")
	c.Flags().StringVar(&repoRoot, "repo-root", "", "override repo root (default: auto-detect)")
	return c
}
