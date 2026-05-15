package scaffold

import _ "embed"

// Templates for `leet init`. Each is rendered with simple text/template
// substitution using InitVars below. Files are written only if they don't
// already exist (init is idempotent).

const initREADMETmpl = `# {{.Name}}

A personal LeetCode practice repo, scaffolded by [leet](https://github.com/daviddwlee84/LeetCode/tree/master/tools/leet).

## Setup

` + "```sh\n" +
	`uv sync             # install dev tools (pytest, ruff, coverage)
leet auth           # paste LEETCODE_SESSION + csrftoken once
leet daily          # fetch today's daily, scaffold, open $EDITOR
leet tui            # interactive browser` +
	"\n```\n\n" + `## Layout

This repo uses the **{{.Layout}}** layout (see ` + "`.leet/config.toml`" + `).

| Layout | Folder | Files |
|---|---|---|
| ` + "`legacy`" + ` | ` + "`Python3/Array/MatrixDiagonalSum/`" + ` | ` + "`Naive1572.py`, `test_1572.py`, `Note1572.md`" + ` |
| ` + "`structured`" + ` | ` + "`Python3/array/matrix-diagonal-sum/`" + ` | ` + "`naive.py`, `test.py`, `README.md`, `meta.json`" + ` |

## Problems

<!-- problems-table-start -->
| Number | Difficulty | Problem | Date | Category | Method | Notes |
|---|---|---|---|---|---|---|
<!-- problems-table-end -->
`

const initAGENTSTmpl = `# AGENTS.md — {{.Name}}

> Canonical agent-context file. ` + "`CLAUDE.md`" + ` in the repo root is a
> symlink → this file, so Claude Code reads the same content. Future
> tools (Cursor / OpenCode / Codex) can symlink in the same way.

## What this repo is

A personal LeetCode practice archive. Scaffolding is done via
[leet](https://github.com/daviddwlee84/LeetCode/tree/master/tools/leet).

## Layout: ` + "{{.Layout}}" + `

{{ if eq .Layout "legacy" -}}
- Solution files: ` + "`{Strategy}{ID}.py`" + ` (e.g. ` + "`Naive1572.py`, `HashTable001.py`" + `)
- Test files:    ` + "`test_{ID}.py`" + ` with module-level ` + "`testcases = [...]`" + `
- Notes:         ` + "`Note{ID}.md`" + ` (optional)
- Daily:         ` + "`Python3/{Category}/{ProblemNamePascal}/`" + `
{{- else -}}
- Solution files: ` + "`{strategy_snake}.py`" + ` (e.g. ` + "`naive.py`, `hash_table.py`" + `)
- Test files:    ` + "`test.py`" + ` with ` + "`pytest.mark.parametrize`" + ` across strategies
- Notes:         ` + "`README.md`" + ` (folder-level docs)
- Meta:          ` + "`meta.json`" + ` (id, tags, strategies with kind: own/reference/archive)
- Daily:         ` + "`Python3/{category-kebab}/{problem-name-kebab}/`" + `
{{- end }}

## Conventions

- Run ` + "`leet daily`" + ` to scaffold new problems (enforces layout).
- Run ` + "`leet test`" + ` (local pytest) or ` + "`leet test --online`" + ` (LeetCode Run).
- Run ` + "`leet submit`" + ` to submit; failed inputs land in ` + "`cases/`" + `.

## Backlog

See ` + "`TODO.md`" + ` (if present) for prioritized backlog.
`

const initGitignoreTmpl = `# Python
__pycache__/
*.py[cod]
*$py.class
.pytest_cache/
.coverage
.coverage.*
coverage.xml
.tox/
.mypy_cache/
.ruff_cache/

# uv / virtualenv
.venv/
venv/
env/
ENV/

# Editor / OS
.vscode/
.idea/
.DS_Store

# leet-generated failed-submission cases
**/cases/failed_*.txt
**/cases/online_failed_*.txt

# Go build artifacts (if you keep tools/ inside this repo)
tools/leet/bin/
tools/leet/dist/
`

const initPyprojectTmpl = `[project]
name = "{{.PackageName}}"
version = "0.1.0"
description = "LeetCode algorithm practice archive"
requires-python = ">=3.11"
dependencies = []

[dependency-groups]
dev = [
    "pytest>=8.0",
    "pytest-cov>=5.0",
    "coverage>=7.4",
    "ruff>=0.5",
]

[tool.pytest.ini_options]
testpaths = ["Python3"]
python_files = ["test_*.py", "test.py"]
addopts = "-q --tb=short"

[tool.coverage.run]
source = ["Python3"]
branch = true
omit = ["**/test_*.py", "**/test.py"]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "SIM"]
ignore = ["E501"]
`

const initLeetConfigTmpl = `# Per-repo leet config. Overrides ~/.config/leet/config.toml; CLI flags win.
layout = "{{.Layout}}"
`

const initClaudeSettingsTmpl = `{
  "plansDirectory": "./.claude/plans"
}
`
