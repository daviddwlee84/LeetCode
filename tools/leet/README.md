# leet — LeetCode TUI helper

A Go-based TUI (Bubble Tea) for fetching LeetCode daily / weekly-contest problems into this repo, scaffolding the standard `Python3/{Category}/{ProblemName}/` folder, editing in `$EDITOR`, submitting, and recording failed test cases — without leaving the terminal.

## Status

Phase 1 — under active development. See `.claude/plans/project-background-leetcode-project-linear-bumblebee.md` at repo root for the full plan.

## Install

### From source (this repo)

```sh
cd tools/leet
make install            # go install ./cmd/leet  → ~/go/bin/leet
# or
make build              # builds bin/leet locally
```

### Without cloning (once pushed to GitHub)

```sh
go install github.com/daviddwlee84/LeetCode/tools/leet/cmd/leet@latest
```

Requires Go ≥ 1.25. The binary lands in `$(go env GOPATH)/bin/leet` — make
sure that directory is on your `$PATH`.

### For a fresh practice repo (planned, see TODO.md)

`leet init <dir>` will bootstrap a new repo with the same `Python3/{Category}/`
layout, `.gitignore`, README skeleton, and optional `socratic-tutor` skill.
Not yet implemented — until then, copy this repo's structure manually.

> **Heads-up for non-author users:** the scaffolder currently hardcodes this
> repo's 12 categories and the `Naive{ID}.py` / `test_{ID}.py` naming. A
> `~/.config/leet/config.toml` to override these is in the backlog (P2).

## Quick start

```sh
leet auth               # paste LEETCODE_SESSION + csrftoken from browser
leet daily              # fetch today's daily, scaffold folder, open $EDITOR
leet contest weekly     # fetch latest weekly contest, scaffold 4 folders
leet submit Python3/Array/MatrixDiagonalSum/Naive1572.py
leet test  Python3/Array/MatrixDiagonalSum
leet tui                # interactive mode (Bubble Tea)
```

## Auth

`leet` calls the unofficial LeetCode GraphQL endpoint with the same cookies your browser uses. To avoid pasting them every time:

1. Log into https://leetcode.com/ in Chrome
2. F12 → Application → Cookies → `https://leetcode.com`
3. Copy the values of `LEETCODE_SESSION` and `csrftoken`
4. Run `leet auth` and paste both

Cookies are stored under `~/Library/Application Support/leet/auth.toml` (macOS) — file mode `0600`. Use `leet auth --check` to verify.

## Conventions preserved

- Solution files: `{Strategy}{ID}.py` (e.g. `Naive1572.py`)
- Test files:    `test_{ID}.py` with module-level `testcases = [...]`
- Notes:         `Note{ID}.md` (optional)
- Daily:         `Python3/{Category}/{ProblemName}/`
- Contest:       `Contest/LeetCodeWeeklyContest/WeeklyContest{N}/{1..4}/`

## Dev

```sh
make test               # go test ./...
make lint               # golangci-lint run (or go vet fallback)
make tidy               # go mod tidy
```
