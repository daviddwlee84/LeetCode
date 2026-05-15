# Handling existing `docs/` content

The single highest-trust action this skill takes is deciding what to do with
content the user already has. Get it wrong and you can quietly destroy
hand-curated documentation. **Default behavior: ask, never auto-migrate.**

## Decision tree

Run this check **before** scaffolding anything:

```
Does <repo>/mkdocs.yml exist?
├── YES → STOP. Report the path, don't overwrite. Suggest the user
│         either delete it first, or use add-docs-page.sh / check-preferences.sh
│         on the existing site.
└── NO  → continue
    Does <repo>/docs/ exist?
    ├── NO  → safe path. Scaffold from scratch with all templates.
    │         Record existing_docs_decision: none.
    └── YES → enumerate non-hidden files under docs/
        ├── 0 files (empty dir) → safe. Treat as "none".
        └── ≥1 files            → ASK the user. See "Three options" below.
```

## Three options to present

When the user has existing content under `docs/`, paste the file list and
present these three choices verbatim. Don't paraphrase — the wording matters
for an honest consent gate.

### (a) Skip — leave my docs alone, just create `mkdocs.yml`

- Scaffold `mkdocs.yml`, `pyproject.toml`, the workflow, but **leave
  `docs/` untouched**.
- The generated `mkdocs.yml` will have `docs_dir: docs` pointing at their
  files and an **empty** `nav:` so MkDocs auto-generates the nav from the
  filesystem.
- Best for: user already organized their docs the way they want.
- Risk: their existing files may not pass `--strict` build (relative-link
  rules, missing snippets dir). Run `uv run mkdocs build` (without
  `--strict`) first and report any warnings.

### (b) Wrap — add `mkdocs.yml` with my files explicitly in the nav

- Same as (a), but **enumerate their existing markdown files into an
  explicit `nav:` block** so the user can see/reorder them later.
- Best for: user wants a starting nav structure but trusts the agent to
  pick a reasonable initial order (alphabetical by default).
- Don't add the standard `index.md` / `getting-started.md` skeleton — their
  content is already there.

### (c) Manual — I'll reorganize first

- Bail out cleanly. Don't write anything.
- Tell the user to re-run when ready.
- Record `existing_docs_decision: deferred` so a later run knows the user
  has been asked once.

## What "non-hidden files" means

For the purposes of this check:

- Count: `*.md`, `*.html`, `*.txt`, any subdirectories with content.
- Don't count: dotfiles (`.DS_Store`, `.gitkeep`), `__pycache__`, `node_modules`.
- An empty directory or one containing only `.gitkeep` is treated as
  "no existing content".

Implementation hint:

```bash
find docs -type f \
  -not -path '*/\.*' \
  -not -name '.gitkeep' \
  -not -path '*/__pycache__/*' \
  -not -path '*/node_modules/*' \
  | head -50
```

## Things this skill must NOT do

- **Don't rename existing files.** Even "obvious" cleanups like
  `README.md → index.md` change git history and break user muscle memory.
- **Don't move files into subdirectories.** Users sometimes deliberately
  flatten or deliberately nest. Their structure stays.
- **Don't rewrite content.** No "I converted your relative links to
  absolute" without an explicit ask.
- **Don't add a frontmatter block to existing files.** Some users use
  `---` as a horizontal rule in markdown; assuming they want frontmatter
  breaks rendering.
- **Don't `git mv`.** Deferring file reorganization to the user means they
  decide whether to use `git mv` (preserves history) or plain `mv` (treats
  as new file). The skill shouldn't make that call.

If the user explicitly says "yes, please move my README into docs/", that's
a separate action with its own consent — not part of bootstrap.

## After bootstrap

Whichever option was chosen, run `uv run mkdocs build --strict` (or non-strict
for option a) and report:

- Any errors → must be fixed before deploy
- Any warnings → list them, let the user decide whether to fix now
- Any "info" messages about relative links to dirs outside `docs/` → these
  are tolerated by strict mode, mention them only briefly

## Recording the decision

```bash
bash scripts/check-preferences.sh \
  --set mkdocs_site_bootstrap.existing_docs_decision=skipped
```

Valid values: `none` (nothing was there), `skipped` (option a),
`wrapped` (option b), `deferred` (option c, user will re-run).
