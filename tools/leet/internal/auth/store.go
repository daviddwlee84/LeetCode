// Package auth stores LeetCode session cookies on disk so subsequent commands
// don't need to re-prompt. macOS path:
//
//	~/Library/Application Support/leet/auth.toml
//
// File mode is 0600. Future versions may layer go-keyring on top for the
// session cookie; for MVP we keep it simple.
package auth

import (
	"errors"
	"fmt"
	"io/fs"
	"os"
	"path/filepath"

	toml "github.com/pelletier/go-toml/v2"
)

const (
	envSession = "LEETCODE_SESSION"
	envCSRF    = "LEETCODE_CSRF"
)

// Credentials are the two cookies required to talk to LeetCode as the
// signed-in user. csrftoken also doubles as the X-Csrftoken header.
type Credentials struct {
	Session string `toml:"session"`
	CSRF    string `toml:"csrf"`
}

// Empty returns true if either cookie is missing — treat as "no auth".
func (c Credentials) Empty() bool {
	return c.Session == "" || c.CSRF == ""
}

// configPath resolves the per-user config file. Visible for testing.
var configPath = func() (string, error) {
	dir, err := os.UserConfigDir()
	if err != nil {
		return "", err
	}
	return filepath.Join(dir, "leet", "auth.toml"), nil
}

// Load reads cookies from disk. Returns an empty Credentials with a sentinel
// error if the file doesn't exist yet, so callers can distinguish "no auth
// configured" from "io broke".
var ErrNotConfigured = errors.New("no LeetCode credentials configured (run 'leet auth')")

func Load() (Credentials, error) {
	path, err := configPath()
	if err != nil {
		return Credentials{}, err
	}
	data, err := os.ReadFile(path)
	if err != nil {
		if errors.Is(err, fs.ErrNotExist) {
			return Credentials{}, ErrNotConfigured
		}
		return Credentials{}, err
	}
	var c Credentials
	if err := toml.Unmarshal(data, &c); err != nil {
		return Credentials{}, fmt.Errorf("parse %s: %w", path, err)
	}
	if c.Empty() {
		return Credentials{}, ErrNotConfigured
	}
	return c, nil
}

// Save writes cookies with mode 0600.
func Save(c Credentials) error {
	if c.Empty() {
		return errors.New("refusing to save empty credentials")
	}
	path, err := configPath()
	if err != nil {
		return err
	}
	if err := os.MkdirAll(filepath.Dir(path), 0o700); err != nil {
		return err
	}
	body, err := toml.Marshal(c)
	if err != nil {
		return err
	}
	// Write to temp file then rename so we never leave a half-written file.
	tmp := path + ".tmp"
	if err := os.WriteFile(tmp, body, 0o600); err != nil {
		return err
	}
	return os.Rename(tmp, path)
}

// FromEnv reads cookies from LEETCODE_SESSION + LEETCODE_CSRF.
func FromEnv() (Credentials, error) {
	s := os.Getenv(envSession)
	c := os.Getenv(envCSRF)
	if s == "" || c == "" {
		return Credentials{}, fmt.Errorf("set %s and %s in the environment", envSession, envCSRF)
	}
	return Credentials{Session: s, CSRF: c}, nil
}
