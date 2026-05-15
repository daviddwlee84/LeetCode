// Package tui hosts the Bubble Tea interactive UI. The MVP is intentionally
// minimal — list of recent problem folders + open in $EDITOR + submit. More
// screens (daily picker, contest, results pane) are layered on later.
package tui

import (
	"context"
	"fmt"
	"os"
	"path/filepath"
	"sort"
	"strings"

	"github.com/charmbracelet/bubbles/list"
	tea "github.com/charmbracelet/bubbletea"
	"github.com/charmbracelet/lipgloss"
	"github.com/daviddwlee84/LeetCode/tools/leet/internal/editor"
)

var (
	titleStyle    = lipgloss.NewStyle().Bold(true).Foreground(lipgloss.Color("212")).Padding(0, 1)
	statusStyle   = lipgloss.NewStyle().Foreground(lipgloss.Color("241")).Padding(0, 1)
	selectedStyle = lipgloss.NewStyle().Foreground(lipgloss.Color("170")).Bold(true)
)

// Run launches the TUI rooted at the current repo. The MVP shows the most
// recent problem folders under Python3/ and lets you open one in $EDITOR.
func Run(ctx context.Context) error {
	repo, err := findRepoRoot()
	if err != nil {
		return err
	}
	items, err := listProblems(repo)
	if err != nil {
		return err
	}
	if len(items) == 0 {
		return fmt.Errorf("no problem folders found under %s/Python3", repo)
	}

	d := list.NewDefaultDelegate()
	l := list.New(items, d, 0, 0)
	l.Title = "leet — recent problems"
	l.Styles.Title = titleStyle
	l.SetShowStatusBar(true)
	l.SetFilteringEnabled(true)

	m := model{repo: repo, list: l, status: "↵ open in $EDITOR · q quit · / filter"}
	p := tea.NewProgram(m, tea.WithContext(ctx), tea.WithAltScreen())
	_, err = p.Run()
	return err
}

type model struct {
	repo   string
	list   list.Model
	status string
}

type problemItem struct {
	name     string
	category string
	abs      string
	entry    string // path of the .py file to open
}

func (p problemItem) Title() string       { return p.name }
func (p problemItem) Description() string { return p.category + "  ·  " + p.entry }
func (p problemItem) FilterValue() string { return p.name + " " + p.category }

func (m model) Init() tea.Cmd { return nil }

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.WindowSizeMsg:
		h, v := titleStyle.GetFrameSize()
		m.list.SetSize(msg.Width-h, msg.Height-v-1)
		return m, nil
	case tea.KeyMsg:
		switch msg.String() {
		case "q", "ctrl+c":
			return m, tea.Quit
		case "enter":
			it, ok := m.list.SelectedItem().(problemItem)
			if !ok {
				return m, nil
			}
			cmd := editor.Command(it.entry)
			if cmd == nil {
				m.status = "no editor available"
				return m, nil
			}
			return m, tea.ExecProcess(cmd, func(err error) tea.Msg {
				if err != nil {
					return statusMsg(fmt.Sprintf("editor error: %v", err))
				}
				return statusMsg("✓ saved")
			})
		}
	case statusMsg:
		m.status = string(msg)
	}
	var cmd tea.Cmd
	m.list, cmd = m.list.Update(msg)
	return m, cmd
}

func (m model) View() string {
	return m.list.View() + "\n" + statusStyle.Render(m.status)
}

type statusMsg string

// listProblems walks Python3/ and returns problem folders sorted by mtime
// (newest first). Each item points at its first solution .py file (entry).
func listProblems(repo string) ([]list.Item, error) {
	pyRoot := filepath.Join(repo, "Python3")
	entries, err := os.ReadDir(pyRoot)
	if err != nil {
		return nil, err
	}

	type indexed struct {
		name string
		mod  int64
		abs  string
		cat  string
		py   string
	}
	var found []indexed

	for _, cat := range entries {
		if !cat.IsDir() {
			continue
		}
		catDir := filepath.Join(pyRoot, cat.Name())
		problems, err := os.ReadDir(catDir)
		if err != nil {
			continue
		}
		for _, prob := range problems {
			if !prob.IsDir() {
				continue
			}
			abs := filepath.Join(catDir, prob.Name())
			info, err := prob.Info()
			if err != nil {
				continue
			}
			py := pickEntryFile(abs)
			if py == "" {
				continue
			}
			found = append(found, indexed{
				name: prob.Name(),
				mod:  info.ModTime().Unix(),
				abs:  abs,
				cat:  cat.Name(),
				py:   py,
			})
		}
	}
	sort.Slice(found, func(i, j int) bool { return found[i].mod > found[j].mod })

	cap := 100
	if len(found) < cap {
		cap = len(found)
	}
	items := make([]list.Item, 0, cap)
	for _, f := range found[:cap] {
		items = append(items, problemItem{
			name:     f.name,
			category: f.cat,
			abs:      f.abs,
			entry:    f.py,
		})
	}
	return items, nil
}

func pickEntryFile(folder string) string {
	entries, err := os.ReadDir(folder)
	if err != nil {
		return ""
	}
	// Prefer Naive*.py (the convention), else first non-test .py.
	var fallback string
	for _, e := range entries {
		n := e.Name()
		if !strings.HasSuffix(n, ".py") || strings.HasPrefix(n, "test_") {
			continue
		}
		if strings.HasPrefix(n, "Naive") {
			return filepath.Join(folder, n)
		}
		if fallback == "" {
			fallback = filepath.Join(folder, n)
		}
	}
	return fallback
}

func findRepoRoot() (string, error) {
	dir, err := os.Getwd()
	if err != nil {
		return "", err
	}
	for {
		if info, err := os.Stat(filepath.Join(dir, ".git")); err == nil && info.IsDir() {
			return dir, nil
		}
		parent := filepath.Dir(dir)
		if parent == dir {
			return "", fmt.Errorf("not inside a git repo")
		}
		dir = parent
	}
}
