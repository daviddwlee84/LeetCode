package cli

import (
	"fmt"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/auth"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/leetcode"
	"github.com/spf13/cobra"
)

func newAuthCmd() *cobra.Command {
	var (
		check        bool
		fromEnv      bool
		nonInteractive bool
		session      string
		csrf         string
	)
	cmd := &cobra.Command{
		Use:   "auth",
		Short: "Set or check LeetCode session cookies",
		Long: `Stores LEETCODE_SESSION + csrftoken under your user config dir
(file mode 0600). Use --check to verify the saved cookies still work.`,
		RunE: func(cmd *cobra.Command, _ []string) error {
			if check {
				creds, err := auth.Load()
				if err != nil {
					return err
				}
				client := leetcode.NewClient(creds)
				user, err := client.UserStatus(cmd.Context())
				if err != nil {
					return fmt.Errorf("verify failed: %w", err)
				}
				if !user.IsSignedIn {
					return fmt.Errorf("cookies present but LeetCode reports not signed in — re-run 'leet auth'")
				}
				fmt.Printf("✓ logged in as %s\n", user.Username)
				return nil
			}

			var creds auth.Credentials
			switch {
			case fromEnv:
				c, err := auth.FromEnv()
				if err != nil {
					return err
				}
				creds = c
			case nonInteractive:
				if session == "" || csrf == "" {
					return fmt.Errorf("--non-interactive requires --session and --csrf")
				}
				creds = auth.Credentials{Session: session, CSRF: csrf}
			default:
				c, err := auth.PromptInteractive()
				if err != nil {
					return err
				}
				creds = c
			}

			if err := auth.Save(creds); err != nil {
				return err
			}
			fmt.Println("✓ saved. Run 'leet auth --check' to verify.")
			return nil
		},
	}
	cmd.Flags().BoolVar(&check, "check", false, "verify saved cookies via userStatus query")
	cmd.Flags().BoolVar(&fromEnv, "from-env", false, "read LEETCODE_SESSION / LEETCODE_CSRF from environment")
	cmd.Flags().BoolVar(&nonInteractive, "non-interactive", false, "skip prompt; require --session and --csrf")
	cmd.Flags().StringVar(&session, "session", "", "LEETCODE_SESSION cookie value")
	cmd.Flags().StringVar(&csrf, "csrf", "", "csrftoken cookie value")
	return cmd
}
