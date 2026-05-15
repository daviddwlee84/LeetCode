package cli

import (
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"strings"
	"time"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/auth"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/leetcode"
	"github.com/spf13/cobra"
)

func newTestCmd() *cobra.Command {
	var (
		online    bool
		caseInput string
	)
	cmd := &cobra.Command{
		Use:   "test [path]",
		Short: "Run pytest locally, or run on LeetCode's Run endpoint with --online",
		Long: `Default behavior: wrap 'pytest -v' in the given problem folder
(or current dir). Use --online to run on LeetCode's "Run" endpoint
(interpret_solution) — that's the same as clicking Run in the web UI:
it does NOT count as a submission.

  leet test Python3/Array/MatrixDiagonalSum/                # local pytest
  leet test --online Python3/.../Naive1572.py               # LeetCode Run, default sample
  leet test --online --case "[[1,2],[3,4]]" .../Naive1572.py # custom input`,
		Args: cobra.MaximumNArgs(1),
		RunE: func(cmd *cobra.Command, args []string) error {
			if online {
				return runOnlineTest(cmd, args, caseInput)
			}
			return runLocalPytest(cmd, args)
		},
	}
	cmd.Flags().BoolVar(&online, "online", false, "run on LeetCode (Run endpoint, not Submit)")
	cmd.Flags().StringVar(&caseInput, "case", "", "custom test input (newline-separated); default: problem's sample test case")
	return cmd
}

func runLocalPytest(cmd *cobra.Command, args []string) error {
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
}

func runOnlineTest(cmd *cobra.Command, args []string, dataInput string) error {
	if len(args) != 1 {
		return fmt.Errorf("--online needs a .py path")
	}
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
		return fmt.Errorf("--online needs auth: %w", err)
	}
	client := leetcode.NewClient(creds)

	slug, err := client.QuestionSlugByID(cmd.Context(), id)
	if err != nil {
		return err
	}

	fmt.Printf("Running %s on LeetCode (Run, not Submit)…\n", filepath.Base(path))
	interpretID, err := client.InterpretSolution(cmd.Context(), slug, "python3", string(code), dataInput)
	if err != nil {
		return err
	}
	result, err := client.PollResult(cmd.Context(), interpretID)
	if err != nil {
		return err
	}

	printInterpretResult(result)

	// Capture wrong answers to a separate `online_failed_*` file so we
	// don't confuse Run-time mistakes with real submission failures.
	if !result.Accepted() && (result.LastTestcase != "" || len(result.CodeAnswer) > 0) {
		return captureOnlineFailure(path, result, dataInput)
	}
	return nil
}

func printInterpretResult(r leetcode.SubmitResult) {
	fmt.Printf("verdict: %s\n", r.StatusMsg)
	if r.Runtime != "" {
		fmt.Printf("runtime: %s   memory: %s\n", r.Runtime, r.Memory)
	}
	if r.CompileError != "" {
		fmt.Printf("\ncompile error:\n%s\n", r.CompileError)
		return
	}
	if r.RuntimeError != "" {
		fmt.Printf("\nruntime error:\n%s\n", r.RuntimeError)
	}
	if len(r.CodeAnswer) > 0 {
		fmt.Println("\noutput:")
		for i, ans := range r.CodeAnswer {
			fmt.Printf("  [%d] %s", i+1, ans)
			if i < len(r.ExpectedCodeAnswer) {
				exp := r.ExpectedCodeAnswer[i]
				if exp == ans {
					fmt.Printf("   ✓\n")
				} else {
					fmt.Printf("   ✗ expected: %s\n", exp)
				}
			} else {
				fmt.Println()
			}
		}
	}
}

func captureOnlineFailure(path string, r leetcode.SubmitResult, dataInput string) error {
	folder := filepath.Dir(path)
	casesDir := filepath.Join(folder, "cases")
	if err := os.MkdirAll(casesDir, 0o755); err != nil {
		return err
	}
	fname := fmt.Sprintf("online_failed_%s.txt", time.Now().Format("20060102_150405"))
	fpath := filepath.Join(casesDir, fname)
	body := fmt.Sprintf(
		"# %s — %s (online run, not submission)\n# input:\n%s\n# expected:\n%s\n# got:\n%s\n",
		r.StatusMsg, time.Now().Format(time.RFC3339),
		firstNonBlank(r.LastTestcase, dataInput),
		joinAnswers(r.ExpectedCodeAnswer),
		joinAnswers(r.CodeAnswer),
	)
	if err := os.WriteFile(fpath, []byte(body), 0o644); err != nil {
		return err
	}
	rel, _ := filepath.Rel(folder, fpath)
	fmt.Printf("→ saved online run output to %s\n", rel)
	return nil
}

func joinAnswers(xs []string) string {
	return strings.Join(xs, "\n")
}

func firstNonBlank(a, b string) string {
	if strings.TrimSpace(a) != "" {
		return a
	}
	return b
}
