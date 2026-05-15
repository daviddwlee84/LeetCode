package auth

import (
	"fmt"

	"github.com/charmbracelet/huh"
)

// PromptInteractive shows a Huh form explaining where to grab cookies from
// the browser and collecting them. Returns the entered credentials.
func PromptInteractive() (Credentials, error) {
	fmt.Println(`
LeetCode auth setup
───────────────────
1. Open https://leetcode.com/ in Chrome (or Firefox) and make sure you're signed in.
2. Open DevTools → Application → Cookies → https://leetcode.com
3. Copy the values of these two cookies:
     • LEETCODE_SESSION
     • csrftoken
4. Paste them below.`)

	var session, csrf string
	form := huh.NewForm(
		huh.NewGroup(
			huh.NewInput().
				Title("LEETCODE_SESSION").
				EchoMode(huh.EchoModePassword).
				Validate(nonEmpty("session")).
				Value(&session),
			huh.NewInput().
				Title("csrftoken").
				EchoMode(huh.EchoModePassword).
				Validate(nonEmpty("csrf")).
				Value(&csrf),
		),
	)
	if err := form.Run(); err != nil {
		return Credentials{}, err
	}
	return Credentials{Session: session, CSRF: csrf}, nil
}

func nonEmpty(name string) func(string) error {
	return func(s string) error {
		if s == "" {
			return fmt.Errorf("%s is required", name)
		}
		return nil
	}
}
