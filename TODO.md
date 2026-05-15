# TODO — LeetCode repo backlog

Priority/effort tagged. Items move to `backlog/{slug}.md` once they need a
real design write-up. Symptom-based traps go in `pitfalls/`.

Tags:
- **Priority**: P1 (do soon) / P2 (do eventually) / P3 (nice to have) / P4 (someday/maybe)
- **Effort**: S (≤ half day) / M (≤ 2 days) / L (≤ 1 week) / XL (open-ended)

---

## Phase 2 — directly unblocks regular practice

- [ ] **P1 / S** — `leet readme-update` writes the README row in the right
  position (currently `leet readme-row` only prints; user pastes manually).
  Needs README marker comments to find insertion point, or sort-by-ID logic.
- [ ] **P1 / M** — Per-problem `meta.json` (or central `data/problems.toml`).
  Unblocks: README regen, mkdocs index, stats dashboard, fuzzy problem
  search. New scaffolds write meta automatically; old problems backfill
  lazily.
- [ ] **P1 / S** — CI migration: Travis → GitHub Actions matrix
  (Python 3.11 / 3.12) + ruff format/check + pre-commit hooks. Add a job for
  `cd tools/leet && go test ./...` too. Remove `.travis.yml` once green.
- [ ] **P2 / S** — `leet test --merge-failed`: take entries from
  `cases/failed_*.txt` and append them to `test_{ID}.py`'s `testcases` list
  with a `# leet:failed-case-{date}` marker.

## Phase 3 — TUI polish (current TUI is "list + open editor" only)

- [ ] **P2 / M** — TUI: integrate `daily` (key `d` fetches today's daily,
  shows scaffold-confirmation form, then jumps into editor).
- [ ] **P2 / M** — TUI: integrate `submit` (key `s` runs submit on the
  highlighted file, shows verdict in a panel using lipgloss colors).
- [ ] **P2 / S** — TUI: keymap help footer, `?` overlay.
- [ ] **P2 / S** — Glamour render of problem detail (key `enter` →
  description preview before opening editor).

## Convention shifts (need explicit OK before doing)

- [ ] **P2 / L** — **Folder-level README** instead of `Note{ID}.md`. Drop
  problem ID from filenames entirely:
  - `Naive{ID}.py` → `Naive.py` / `HashTable.py` / `DP.py`
  - `test_{ID}.py` → `test.py`
  - `Note{ID}.md` → `README.md` (folder doc)
  - ID lives in `meta.json` frontmatter (or just the GitHub path).
  Cleaner imports (`from Naive import Solution`), no number-stuffing in
  scripts. Migration is mass rename across ~600 problems — needs a one-shot
  script + careful test sweep. Do **after** `meta.json` lands so we still
  have a structured ID source.
- [ ] **P2 / M** — `~/.config/leet/config.toml` for per-user overrides:
  category list, folder/file naming pattern, repo root anchor (default
  `.git`). Unlocks both `leet init` and the convention shift above without
  forking the binary.

## Phase 4 — scope expansion

- [ ] **P2 / M** — Contest folder restructuring: move from
  `Contest/LeetCodeWeeklyContest/WeeklyContest{N}/{1..4}/` to using the
  problem-name PascalCase under `Contest/Weekly{N}/{ProblemName}/` with
  proper test files. Currently contests have no tests at all. (User has
  said: "先維持現狀後續再結構化" — confirm before doing.)
- [ ] **P2 / M** — mkdocs site: bootstrap with the symlinked
  `mkdocs-site-bootstrap` skill. Generate problem index from `meta.json`
  (depends on P1 metadata). Optional zh-TW translation.
- [ ] **P2 / M** — Spaced-repetition / Anki-style review (`leet review`):
  per-problem **mastery level** (`familiar` / `shaky` / `forgot` / `did with
  hints`), bucket review intervals (1d / 3d / 1w / 2w / 1mo) like SM-2 lite,
  and **filter by problem type** (DP / greedy / graph / two-pointer / etc.).
  Source the initial seed from the existing README `Remark` column markers
  (`do it again`, `testcase`, `*`, `▲`). Each review session: pick one due
  problem, **hide the existing solution**, prompt re-solve, after submit ask
  user to re-rate mastery → schedule next review. Persist state in
  `.leet/review_state.toml` per-problem (or in `meta.json` once that lands).
  Subsumes the older "do it again queue" idea above.
- [ ] **P3 / S** — Personal stats dashboard: count problems by category,
  difficulty, month. Render in TUI as a Bubble Tea screen using lipgloss
  bar charts.
- [ ] **P3 / M** — `leet sync`: hit LeetCode profile, mark which solved
  problems aren't yet in the repo (gap analysis).
- [ ] **P3 / S** — Schedule integration: cron / `/schedule` to push a daily
  notification with today's problem (Mac notification or Slack webhook).
- [ ] **P2 / M** — `leet init <dir>`: bootstrap a fresh LeetCode practice
  repo for non-author users. Steps: `git init`, write `Python3/` skeleton +
  `Contest/` + `.gitignore` + `README.md` template + optional `CLAUDE.md` +
  optional `.claude/skills/socratic-tutor/` symlink/copy. Pairs with the
  `~/.config/leet/config.toml` task above so the user can pick category list
  + naming style. Eventually publish to PyPI-equivalent (`go install`
  already works once pushed).
- [ ] **P3 / S** — `goreleaser` config + Homebrew tap for `leet`.

## Phase 5 — long-tail repo hygiene (no rush)

- [ ] **P3 / XL** — Modernize old Python solutions: add type hints, use
  match statements where appropriate, refactor pre-3.10 patterns. Probably
  do per-category as the user revisits.
- [ ] **P4 / XL** — JavaScript / C++ subdirs: currently empty placeholders.
  Add real LSP-friendly structure if/when the user picks up another
  language. `leet` could grow `--lang js` / `--lang cpp` flags to scaffold
  there.
- [ ] **P4 / S** — Failed-case auto-shrinker: shrink `cases/failed_*.txt`
  inputs (binary search on list length, etc.) for minimal repros.

## Decisions / why we're doing this

The driver is reducing daily-practice friction. Manual scaffolding
(folder + Naive + test + README row + paste problem statement) was bad
enough to make the user skip days. Phase 1 (`tools/leet` Go TUI +
socratic-tutor) collapses scaffold to one command and adds real teaching
value when the user gets stuck.

The plan doc with full rationale lives at:
`.claude/plans/project-background-leetcode-project-linear-bumblebee.md`
