# `.skills/preferences.yaml` schema

Per-repo preferences file used by `mkdocs-site-bootstrap` and any future
skill that needs to remember a user decision across sessions.

## Location

Always at `<repo-root>/.skills/preferences.yaml`. **Per-repo, not global.**
Each repository carries its own decisions; never write to `~/.skills/` or
`~/.config/`.

The directory is created on first write. Add `.skills/preferences.yaml` to
`.gitignore` if the user prefers it private, but the default assumption is
that it's committed (decisions about *this repo's tooling* belong in the
repo).

## Top-level structure

```yaml
# .skills/preferences.yaml
# Decisions recorded by skills. Each top-level key is a skill namespace.

mkdocs_site_bootstrap:
  enabled: true                  # null = never asked, true = opted in, false = opted out
  decided_at: 2026-04-23
  stack: mkdocs-material         # which docs stack variant
  auto_deploy: true              # deploy via GitHub Actions on push
  pages_deployed: true           # has the first deploy succeeded
  pages_enabled_at: 2026-04-23
  existing_docs_decision: skipped  # skipped | wrapped | none
  site_url: https://owner.github.io/repo/
  repo_slug: owner/repo
  # i18n keys — written by add-language.sh, read by add-docs-page.sh.
  languages: ["en", "zh-TW"]      # ordered list; first is default
  keep_english_terms: true         # injects terminology admonition into non-default stubs
  i18n_structure: suffix           # suffix | folder (folder reserved, not yet implemented)

# Future skills add their own top-level keys with the same shape.
# example_other_skill:
#   enabled: true
#   decided_at: 2026-05-01
```

## Conventions for skill namespaces

- **Namespace key matches the skill's directory name** with `-` → `_`
  (YAML-friendly): `mkdocs-site-bootstrap` → `mkdocs_site_bootstrap`.
- **Always include `enabled` and `decided_at`.** These are the universal
  fields. `enabled` is the consent state; `decided_at` lets the agent see
  how stale the decision is.
- **Don't store secrets.** This file is meant to be safely committable.
  API tokens, passwords, etc. go in `.env` (gitignored) or in CI secrets.
- **Don't store derived state.** Anything reproducible from other files
  (e.g., "is mkdocs.yml present") should be re-checked, not cached. Only
  store decisions and timestamps.

## Three-state semantics for `enabled`

| Value | Meaning | Agent behavior |
|---|---|---|
| key absent or `null` | Never asked | Run the interview |
| `true` | User opted in | Proceed without re-asking |
| `false` | User opted out | Don't pester. If the user is now asking for it, confirm they want to reverse the decision, then `--reset` and re-interview |

This three-state model is why we don't use a marker file (presence-only)
or a boolean (only two states). The "never asked" state matters.

## Reading and writing

Always go through `scripts/check-preferences.sh` rather than parsing the YAML
yourself. It handles:

- Creating the file and `.skills/` dir if missing
- Preserving the comment header
- Atomic writes (write to `.tmp`, then `mv`)
- Friendly errors for malformed input

```bash
# Read one key
bash scripts/check-preferences.sh --get mkdocs_site_bootstrap.enabled

# Set one or more keys
bash scripts/check-preferences.sh \
  --set mkdocs_site_bootstrap.enabled=true \
  --set mkdocs_site_bootstrap.decided_at=2026-04-23

# Reset an entire skill namespace (returns to "never asked" state)
bash scripts/check-preferences.sh --reset mkdocs_site_bootstrap

# Dump everything
bash scripts/check-preferences.sh --list
```

The script supports `--json` for structured output that an agent can parse
reliably.

## When to reset

The user explicitly says one of:

- "I changed my mind about <skill>" → `--reset <namespace>`
- "Stop nagging me about docs" → `--set <namespace>.enabled=false`
- "Re-ask me next time" → `--reset <namespace>`

Don't reset proactively. The whole point is to *avoid* re-asking.

## Cross-skill coordination

Two skills shouldn't share namespace keys. If `mkdocs-site-bootstrap` and
some hypothetical `docs-publisher` skill both care about whether a docs site
exists, the answer is to **detect from the filesystem** (does `mkdocs.yml`
exist?), not to share a preference key. Preferences record *intent*; the
filesystem records *state*.

## i18n keys (added when `add-language.sh` runs)

| Key | Type | Meaning |
|---|---|---|
| `languages` | ordered list of locale codes | First entry is the default language. Empty / missing means monolingual (default). |
| `keep_english_terms` | bool | Whether to inject the "Terminology rule" admonition into non-default-language stubs. Defaults to `true`; the user can flip this if they don't want the admonition. |
| `i18n_structure` | `suffix` \| `folder` | How translated files are laid out. **Currently only `suffix` is implemented.** `folder` is reserved for future work; setting it now will not change script behavior. |

`add-docs-page.sh` reads `languages` to decide whether to generate
`*.<LANG>.md` siblings alongside the default-language page. If the key is
missing or has only one entry, it stays mono-lingual (existing behavior).

## Array values via `--set`

`check-preferences.sh --set` recognises YAML flow sequences (`[…]`) and
mappings (`{…}`) and passes them through to `yq` unquoted. Use this for the
`languages` key:

```bash
bash scripts/check-preferences.sh \
  --set 'mkdocs_site_bootstrap.languages=["en", "zh-TW"]'
```

Bare strings, booleans, and numbers still work as before.

## Schema versioning

If we ever need to change the shape, add a top-level `schema_version: 1`
key and bump it. Until then, treat the schema as version 0 / implicit.

## Validation

`check-preferences.sh --validate` is a future addition (not yet implemented).
For now, trust the script's writes and don't hand-edit the file unless you
re-read it after to verify.
