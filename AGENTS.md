# CLAUDE.md — LeetCode practice repo

> Context for AI coding assistants working in this repo.

## What this repo is

A long-running personal LeetCode practice archive (since 2018, ~600+ problems
solved). Each problem has its own folder with:

- One or more solution files: `{Strategy}{ID}.py` (e.g. `Naive1572.py`,
  `HashTable001.py`, `DP005.py`)
- A `test_{ID}.py` using pytest's plain `assert` style
- An optional `Note{ID}.md` with intuition + complexity discussion

The README is a hand-maintained markdown table indexing every solved problem.

## Folder layout (preserved since 2018 — do not refactor without asking)

```
README.md                   — main index table (free-form markdown, hand-edited)
Python3/{Category}/{ProblemNamePascal}/
  Naive{ID}.py             — first-thought solution
  {OtherStrategy}{ID}.py   — alternative approaches
  test_{ID}.py             — pytest tests
  Note{ID}.md              — optional notes
Contest/LeetCodeWeeklyContest/WeeklyContest{N}/{1..4}/
  Solution.py / Naive.py   — contest problem solutions
Learn/                     — algorithm/data-structure learning material
Notes/                     — general algorithm reference notes
tools/leet/                — Go (Bubble Tea) TUI helper, see below
.claude/skills/socratic-tutor/  — guided-solving skill
```

The 12 historical Python categories are: `Array`, `BinaryTree`,
`BitManipulation`, `Design`, `DynamicProgramming`, `Graph`, `Interactive`,
`LinkedList`, `Math`, `Search`, `String`, `AdHoc`.

## Conventions (don't break these)

- **Filenames carry the problem ID.** `Naive1572.py` not `naive_1572.py`,
  `MatrixDiagonalSum/` not `matrix_diagonal_sum/`.
- **Test file format.** Module-level `testcases = [(input, expected), ...]`
  list, then one `def test_{Strategy}():` per solution iterating it. See
  `Python3/Array/MatrixDiagonalSum/test_1572.py` for the canonical shape.
- **No central conftest.py.** Each problem folder is self-contained.
- **Notes are optional.** Don't auto-create `Note{ID}.md` unless asked
  (e.g. via `leet daily --with-note`).
- **README is hand-curated.** Don't auto-edit it. `leet readme-row` prints a
  suggested row that the user pastes manually.

## tools/leet — TUI helper

Go (1.25) + Bubble Tea + Cobra. Lives in `tools/leet/`. Single binary,
`go install ./cmd/leet` puts `leet` on `$PATH`.

Key commands:

| Command | What it does |
|---|---|
| `leet auth` | Set/check `LEETCODE_SESSION` + `csrftoken` cookies |
| `leet daily [--no-edit] [--with-note]` | Fetch today's daily, scaffold folder under correct category, open `$EDITOR` |
| `leet contest weekly [N\|--latest]` | Fetch contest, scaffold 4 sub-folders |
| `leet test [path]` | Wrap pytest in a problem folder |
| `leet submit <path-to-Naive{ID}.py>` | Submit, poll verdict, save failed input to `cases/failed_*.txt` |
| `leet readme-row <folder>` | Print a suggested README row (not write) |
| `leet tui` | Bubble Tea interactive: list recent problems, open in editor |

Internal package layout: `cmd/leet/` (entrypoint), `internal/cli/` (cobra
subcommands), `internal/leetcode/` (GraphQL + REST), `internal/auth/` (cookie
storage), `internal/scaffold/` (folder/file generators), `internal/categories/`
(LeetCode tag → repo category), `internal/readme/` (row renderer),
`internal/editor/` (`$EDITOR` launcher), `internal/tui/` (Bubble Tea app).

## .claude/skills/socratic-tutor

A Socratic-style coaching skill for algorithm problems. Activates on
`/socratic-tutor`, "I'm stuck", "推一下", or when the user opens a
`Note{ID}.md` they want to fill in. **Does not give answers** — gives layered
hints, requires the user to commit to an approach, then derives complexity
together. Skip if the user says "just give me the answer" or is in a contest
under time pressure.

## Working with this repo as an agent

- For new problems: prefer `leet daily` over hand-scaffolding. It enforces
  conventions automatically.
- When asked to add a solution, first check if the user has already started
  one (look for an existing `Naive{ID}.py` in the folder). Don't overwrite.
- When the user asks for help solving (not implementing) a problem, consider
  whether `socratic-tutor` is the right tool first.
- The tests use plain pytest with `from {Module}{ID} import Solution as
  {Strategy}` — keep the import naming consistent so existing tests don't
  break.
- CI is **still on Travis** (`.travis.yml`); migration to GitHub Actions is
  in `TODO.md`.

## Backlog

See `TODO.md` (project root) for the prioritized backlog. Highlights:

- Structured per-problem `meta.json` to enable README regen + mkdocs site
- CI migration: Travis → GitHub Actions + ruff + pre-commit
- mkdocs site (skill `mkdocs-site-bootstrap` already symlinked, not yet run)
- Contest folder restructuring + sample tests
