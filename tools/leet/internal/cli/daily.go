package cli

import (
	"fmt"
	"path/filepath"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/auth"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/categories"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/config"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/editor"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/leetcode"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/scaffold"
	"github.com/spf13/cobra"
)

func newDailyCmd() *cobra.Command {
	var (
		noEdit   bool
		withNote bool
		repoRoot string
		category string
	)
	cmd := &cobra.Command{
		Use:   "daily",
		Short: "Fetch today's daily challenge and scaffold its folder",
		RunE: func(cmd *cobra.Command, _ []string) error {
			creds, _ := auth.Load() // daily query is public, auth optional
			client := leetcode.NewClient(creds)

			daily, err := client.DailyChallenge(cmd.Context())
			if err != nil {
				return fmt.Errorf("fetch daily: %w", err)
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

			cat := category
			if cat == "" {
				cat = categories.PickFromConfig(cfg, daily.TopicTagNames())
			}

			folder := scaffold.ProblemFolder(cfg, root, cat, daily.Title)
			created, err := scaffold.DailyFromQuestion(cfg, folder, daily, withNote)
			if err != nil {
				return err
			}

			rel, _ := filepath.Rel(root, folder)
			fmt.Printf("✓ %s. %s (%s) → %s\n", daily.QuestionFrontendID, daily.Title, daily.Difficulty, rel)
			for _, f := range created {
				r, _ := filepath.Rel(root, f)
				fmt.Printf("    + %s\n", r)
			}

			if noEdit {
				return nil
			}
			entry := scaffold.EntryPath(cfg, folder, daily.QuestionFrontendID)
			return editor.Launch(entry)
		},
	}
	cmd.Flags().BoolVar(&noEdit, "no-edit", false, "skip launching $EDITOR")
	cmd.Flags().BoolVar(&withNote, "with-note", false, "also create Note{ID}.md skeleton")
	cmd.Flags().StringVar(&repoRoot, "repo-root", "", "override repo root (default: auto-detect)")
	cmd.Flags().StringVar(&category, "category", "", "override category folder (default: auto-pick from tags)")
	return cmd
}
