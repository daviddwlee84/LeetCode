package cli

import (
	"fmt"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/auth"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/leetcode"
	"github.com/spf13/cobra"
)

func newSubmitCmd() *cobra.Command {
	cmd := &cobra.Command{
		Use:   "submit <path-to-solution.py>",
		Short: "Submit a Python solution to LeetCode",
		Args:  cobra.ExactArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			path := args[0]
			code, err := os.ReadFile(path)
			if err != nil {
				return err
			}

			id, err := guessProblemIDFromFile(path)
			if err != nil {
				return err
			}

			creds, err := auth.Load()
			if err != nil {
				return fmt.Errorf("submit needs auth: %w", err)
			}
			client := leetcode.NewClient(creds)

			slug, err := client.QuestionSlugByID(cmd.Context(), id)
			if err != nil {
				return err
			}

			submissionID, err := client.Submit(cmd.Context(), slug, "python3", string(code))
			if err != nil {
				return err
			}

			result, err := client.PollResult(cmd.Context(), submissionID)
			if err != nil {
				return err
			}

			fmt.Printf("verdict: %s\n", result.StatusMsg)
			if result.Runtime != "" {
				fmt.Printf("runtime: %s   memory: %s\n", result.Runtime, result.Memory)
			}

			if result.Accepted() {
				return nil
			}

			// Wrong answer / runtime error: persist input for later
			folder := filepath.Dir(path)
			casesDir := filepath.Join(folder, "cases")
			if err := os.MkdirAll(casesDir, 0o755); err != nil {
				return err
			}
			fname := fmt.Sprintf("failed_%s.txt", time.Now().Format("20060102_150405"))
			fpath := filepath.Join(casesDir, fname)
			body := fmt.Sprintf(
				"# %s — %s\n# input:\n%s\n# expected:\n%s\n# got:\n%s\n",
				result.StatusMsg, time.Now().Format(time.RFC3339),
				result.LastTestcase, result.ExpectedOutput, result.CodeOutput,
			)
			if err := os.WriteFile(fpath, []byte(body), 0o644); err != nil {
				return err
			}
			rel, _ := filepath.Rel(folder, fpath)
			fmt.Printf("→ saved failed case to %s\n", rel)
			return nil
		},
	}
	return cmd
}

// guessProblemIDFromFile extracts the trailing number from filenames like
// Naive1572.py / Better1572.py / Math342.py / Recursive2_023.py.
func guessProblemIDFromFile(path string) (int, error) {
	base := strings.TrimSuffix(filepath.Base(path), ".py")
	// Find the longest trailing run of digits, optionally preceded by '_'.
	i := len(base)
	for i > 0 && base[i-1] >= '0' && base[i-1] <= '9' {
		i--
	}
	digits := base[i:]
	if digits == "" {
		return 0, fmt.Errorf("cannot infer problem ID from %s", base)
	}
	n, err := strconv.Atoi(digits)
	if err != nil {
		return 0, err
	}
	return n, nil
}
