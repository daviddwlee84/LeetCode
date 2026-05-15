# TODO — LeetCode repo backlog

Priority/effort tagged. Items move to `backlog/{slug}.md` once they need a
real design write-up. Symptom-based traps go in `pitfalls/`.

Tags:
- **Priority**: P1 (do soon) / P2 (do eventually) / P3 (nice to have) / P4 (someday/maybe)
- **Effort**: S (≤ half day) / M (≤ 2 days) / L (≤ 1 week) / XL (open-ended)

---

## Done — Phases 1 & 2 (LANDED)

- ✅ **Phase 1** (commit `09ef72d`) — `tools/leet` Go (Bubble Tea + Cobra)
  CLI: `auth` / `daily` / `contest` / `submit` (with failed-case capture) /
  `test` / `readme-row` / `tui`. `.claude/skills/socratic-tutor` skill with
  7-phase Socratic flow + greedy proofs / DP state / complexity references.
  CLAUDE.md + TODO.md + .gitignore additions.
- ✅ **Phase 2.A** (`0aaa2e9`, `e49922e`) — pre-commit hygiene stack
  (`.pre-commit-config.yaml`, `.gitleaks.toml`, `scripts/redact_secrets.py`),
  prepare-commit-msg hook auto-stages SpecStory + plan files, mass
  whitespace/EOL cleanup of legacy files.
- ✅ **Phase 2.A2a** (`3a15741`) — migrate to `.agents/skills/` (real) +
  `.claude/skills/socratic-tutor` symlink, rename `CLAUDE.md → AGENTS.md`
  + symlink. Cross-tool convention (Cursor / OpenCode / Codex can join).
- ✅ **Phase 2.A2b** (`b311700`) — `pyproject.toml` + uv replaces
  `requirements.txt` + `.coveragerc`. `uv.lock` pinned. README updated.
  `uv run pytest` passes all 471 legacy tests in 32s.
- ✅ **Phase 2.B** (`bd31360`) — config-driven `leet`:
  `~/.config/leet/config.toml` + per-repo `.leet/config.toml`, 4-tier
  resolution (CLI > repo > user > built-in). Pattern tokens for filenames
  (`{title_kebab}`, `{strategy_snake}`, etc.). `meta.json` schema with
  `strategies[]` + `kind` (`own`/`reference`/`archive`). Templates split
  into legacy (per_strategy) and structured (parametrize). This repo
  pinned via `.leet/config.toml` to `layout = "legacy"`.
- ✅ **Phase 2.C** (`6710f03`, `8c58c4a`) — `leet init [dir]
  --layout=legacy|structured` bootstraps a fresh practice repo with all
  the same conventions (categories, AGENTS.md, .agents/, symlinks, .leet/
  config, pyproject.toml). 5 integration tests cover both layouts on
  `t.TempDir()`.
- ✅ **Phase 2.E2** (`8c58c4a`) — `leet completion install` auto-writes
  to `~/.zfunc/_leet` (zsh) / `~/.bash_completion.d/leet` (bash) /
  `~/.config/fish/completions/leet.fish` (fish) + prints fpath hint
  for zsh.

---

## Phase 3 — directly unblocks regular practice

- [ ] **P1 / S** — `leet test --online` (LeetCode Run endpoint, not
  Submit). Hits `/problems/{slug}/interpret_solution/`, polls
  `/submissions/detail/{id}/check/` like submit does. Wrong-answer
  captures to `cases/online_failed_*.txt` (separate prefix from
  submission failures). `--case "[1,2,3]\n5"` for custom input.
  Code skeleton already planned in `internal/leetcode/interpret.go`
  + extend `cli/test.go` with `--online` / `--case` flags.
- [ ] **P1 / S** — `leet readme-update` writes the README row in the
  right position (currently `leet readme-row` only prints; user pastes
  manually). Needs README marker comments or sort-by-ID logic.
- [ ] **P1 / M** — Mock LeetCode HTTP server for integration tests.
  Current `internal/scaffold/repo_init_test.go` uses `t.TempDir()` +
  stubbed `leetcode.Question` (covers scaffold/categories logic).
  Adding `httptest.Server` + `testdata/*.json` fixtures + injecting
  via `leetcode.NewClient(..., WithBaseURL(srv.URL))` would let
  `leet daily` / `leet submit` / `leet test --online` end-to-end run
  offline in CI.
- [ ] **P1 / S** — CI migration: Travis → GitHub Actions matrix
  (Python 3.11 / 3.12, Go 1.25) + `uv sync && uv run pytest` for
  Python + `go test ./...` for `tools/leet`. Remove `.travis.yml`
  once green.
- [ ] **P2 / S** — `leet test --merge-failed`: take entries from
  `cases/failed_*.txt` / `cases/online_failed_*.txt` and append them
  to `test_{ID}.py`'s `testcases` list with a `# leet:failed-case-{date}`
  marker.

## Phase 4 — TUI polish (current TUI is "list + open editor" only)

- [ ] **P2 / M** — TUI: integrate `daily` (key `d` fetches today's daily,
  shows scaffold-confirmation form, then jumps into editor).
- [ ] **P2 / M** — TUI: integrate `submit` (key `s` runs submit on the
  highlighted file, shows verdict in a panel using lipgloss colors).
- [ ] **P2 / S** — TUI: keymap help footer, `?` overlay.
- [ ] **P2 / S** — Glamour render of problem detail (key `enter` →
  description preview before opening editor).
- [ ] **P2 / M** — `leet init` interactive Huh form (currently
  flag-based + `--non-interactive` implicit). Prompts: target dir,
  layout, categories preset, with-agents toggle.

## Convention shifts (need explicit OK before bulk-applying)

- [ ] **P2 / L** — **Migrate this repo from legacy → structured layout**
  (`Naive{ID}.py` → `naive.py`, folder PascalCase → kebab-case,
  `Note{ID}.md` → `README.md`, write `meta.json` for each problem).
  Layout machinery already supports both; this task is the bulk
  rename + meta backfill + test sweep across ~600 problems. Needs a
  one-shot script using `internal/scaffold` to derive new names +
  produce a single migration commit.

## Phase 5 — scope expansion

- [ ] **P2 / M** — Contest folder restructuring: move from
  `Contest/LeetCodeWeeklyContest/WeeklyContest{N}/{1..4}/` to
  `Contest/Weekly{N}/{problem-name-kebab}/` with proper test files.
  Currently contests have no tests at all. (User has said:
  "先維持現狀後續再結構化" — confirm before doing.)
- [ ] **P2 / M** — mkdocs site: bootstrap with the
  `.agents/skills/mkdocs-site-bootstrap` skill (already symlinked).
  Generate problem index from `meta.json` (depends on the layout
  migration above). Optional zh-TW translation.
- [ ] **P2 / M** — Spaced-repetition / Anki-style review (`leet review`):
  per-problem **mastery level** (`familiar` / `shaky` / `forgot` /
  `did with hints`), bucket review intervals (1d / 3d / 1w / 2w / 1mo)
  like SM-2 lite, and **filter by problem type** (DP / greedy / graph
  / two-pointer / etc.). Source initial seed from existing README
  `Remark` column markers (`do it again`, `testcase`, `*`, `▲`). Each
  review session: pick one due problem, **hide the existing solution**,
  prompt re-solve, after submit ask user to re-rate mastery → schedule
  next review. Persist in `meta.json` (already has Strategy.Kind;
  add Strategy.LastReviewed + ReviewLevel).
- [ ] **P3 / S** — Personal stats dashboard: count problems by category,
  difficulty, month. Render in TUI as a Bubble Tea screen using lipgloss
  bar charts.
- [ ] **P3 / M** — `leet sync`: hit LeetCode profile, mark which solved
  problems aren't yet in the repo (gap analysis).
- [ ] **P3 / S** — Schedule integration: cron / `/schedule` to push a daily
  notification with today's problem (Mac notification or Slack webhook).
- [ ] **P3 / S** — `goreleaser` config + Homebrew tap for `leet`.

## Phase 6 — long-tail repo hygiene (no rush)

- [ ] **P3 / XL** — Modernize old Python solutions: add type hints, use
  match statements where appropriate, refactor pre-3.10 patterns.
  Probably do per-category as the user revisits.
- [ ] **P4 / XL** — JavaScript / C++ subdirs: currently empty placeholders.
  Add real LSP-friendly structure if/when the user picks up another
  language. `leet` could grow `--lang js` / `--lang cpp` flags to scaffold
  there.
- [ ] **P4 / S** — Failed-case auto-shrinker: shrink `cases/failed_*.txt`
  inputs (binary search on list length, etc.) for minimal repros.

---

## Decisions / why we're doing this

The driver is reducing daily-practice friction. Manual scaffolding
(folder + Naive + test + README row + paste problem statement) was bad
enough to make the user skip days. Phase 1 (`tools/leet` Go TUI +
socratic-tutor) collapses scaffold to one command and adds real teaching
value when the user gets stuck. Phase 2 layered on hygiene + config-
driven scaffolding so other practitioners can `leet init` their own
repo with a different layout, and so this repo's future migration to
the structured layout is a single-flag flip rather than a code change.

The plan doc with full rationale lives at:
`.claude/plans/project-background-leetcode-project-linear-bumblebee.md`
(synonym: `.agents/plans/...` after Phase 2.A2a migration — currently
the plan stays under `.claude/plans/` since plans are Claude-specific).
