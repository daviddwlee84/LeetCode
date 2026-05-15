package cli

import (
	"fmt"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/readme"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/scaffold"
	"github.com/spf13/cobra"
)

func newReadmeCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "readme-row <path-to-problem-folder>",
		Short: "Print a suggested README markdown row for a problem",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			folder := args[0]
			meta, err := scaffold.InspectFolder(folder)
			if err != nil {
				return err
			}
			sols := make([]readme.Solution, 0, len(meta.Solutions))
			for _, s := range meta.Solutions {
				sols = append(sols, readme.Solution{
					Method:  s.Method,
					TimeStr: s.TimeStr,
					RelPath: s.RelPath,
				})
			}
			row := readme.Row(readme.Input{
				ID:         meta.ID,
				Title:      meta.Title,
				Difficulty: meta.Difficulty,
				Date:       meta.Date,
				Category:   meta.Category,
				Solutions:  sols,
				NotePath:   meta.NoteRelPath,
			})
			fmt.Println(row)
			return nil
		},
	}
	return cmd
}
