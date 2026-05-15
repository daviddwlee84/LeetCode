# Bilingual / multi-language docs

How to add a non-English language (typically Traditional Chinese, `zh-TW`) to
a MkDocs Material site bootstrapped by this skill, and how to keep
terminology consistent so future contributors — human or agent — don't
introduce ambiguity.

## TL;DR

```bash
bash skills/local/mkdocs-site-bootstrap/scripts/add-language.sh --lang zh-TW
```

That single command:

1. Inserts a `plugins.i18n` block into `mkdocs.yml` (using
   `mkdocs-static-i18n` with `docs_structure: suffix`).
2. Sets `theme.language: en` (or whatever the default is) so Material's
   built-in UI strings have a baseline.
3. Creates `*.zh-TW.md` sibling stubs for every existing markdown file under
   `docs/` (with the terminology-rule admonition pre-injected).
4. Records the choice in `.skills/preferences.yaml`.
5. Un-comments `mkdocs-static-i18n>=1.2` in `pyproject.toml`.

After it finishes, run:

```bash
uv sync --extra docs
uv run mkdocs build --strict
```

The Material header will gain a language switcher. Translate the stub bodies
when ready.

## Why `mkdocs-static-i18n` + suffix structure

[Squidfunk's recommended approach](https://github.com/squidfunk/mkdocs-material/discussions/2346)
for content translation is the
[`mkdocs-static-i18n`](https://github.com/ultrabug/mkdocs-static-i18n) plugin.
We use **`docs_structure: suffix`** rather than `folder` because:

- **Zero file moves on retrofit.** Existing `docs/index.md`,
  `docs/getting-started.md`, etc. stay where they are. The `folder` mode
  would force you to move every file into `docs/en/` first.
- **Relative links keep working.** Sibling files share the same directory.
- **Per-page opt-in to translation.** A page is only translated when
  `<page>.<lang>.md` exists; otherwise the plugin falls back to the default
  language (`fallback_to_default: true`).

The trade-off: directory listings get crowded once you have many languages.
For sites that grow to 5+ languages the `folder` structure starts to win on
readability — but you can migrate later.

## Terminology preservation rule (hard requirement)

This is the rule for any non-English page in a project that uses this skill:

> **在 zh-TW 頁面，技術名詞首次出現時，以「中文 (English original)」格式呈現。**
> 例：「依賴注入 (dependency injection)」、「型別檢查 (type checking)」。
> 後續同段內可只用中文。
>
> **不自創翻譯。** 若無公認譯名，直接保留英文（如 `embedding`、`tokenizer`、
> `mkdocs-static-i18n`、`pymdownx.snippets`）。
>
> **代碼、API 名、CLI flag、套件名、檔名一律不翻。**

The reason: Chinese-language tech writing has competing translations for
many terms (e.g. `cache` → 快取 / 緩存 / 暫存; `repository` → 倉庫 / 儲存庫 /
版本庫). Keeping the English original on first mention removes the ambiguity
without forcing readers to guess which translation the author meant. It also
keeps the page grep-able for English search terms.

`add-language.sh` and `add-docs-page.sh` inject this rule as an admonition
at the top of every non-default-language stub so authors see it before they
start translating.

## What `add-language.sh` does, step by step

For users who want to apply pieces by hand or audit what the script touched:

1. **Locates `mkdocs.yml`** by walking up from CWD.
2. **Detects existing i18n state.** `yq` query against `.plugins[]` checks
   for an `i18n:` map.
3. **Inserts or extends `plugins.i18n`.**
   - If absent: prepends a fresh i18n block before `search`, with
     `[default-lang, new-lang]` as the language list.
   - If present and the new locale isn't there: appends to
     `plugins[].i18n.languages`.
   - If the locale is already present: no-op.
4. **Sets `theme.language`** to the default language if not already set
   (`mkdocs-static-i18n` warns when `theme.language` is missing).
5. **Removes `navigation.instant` / `navigation.instant.progress`** from
   `theme.features` (the language switcher's contextual link can't be
   rewritten by instant navigation).
6. **Keeps `mkdocs-llmstxt` by default** (the `/llms.txt` feature is the
   reason most users adopt this stack). Use `--remove-llmstxt` to drop it
   instead. With `--drop-strict`, also patches `.github/workflows/docs.yml`
   and `Makefile` to remove `--strict` from `mkdocs build` invocations,
   which is necessary for builds to pass while llmstxt is kept (the plugin
   is structurally incompatible with `reconfigure_material` under
   `--strict` — see "Interaction with `llmstxt` and `copy-to-llm`" below).
7. **Walks `docs/`** for `*.md` files (excluding `_snippets/` and `assets/`),
   and for each non-locale-suffixed source page, creates a sibling
   `*.<LANG>.md` from `assets/translation-stub.md.template`.
8. **Updates `.skills/preferences.yaml`** with three keys:
   `mkdocs_site_bootstrap.languages` (ordered list, default first),
   `keep_english_terms: true`, `i18n_structure: suffix`.
9. **Un-comments `mkdocs-static-i18n>=1.2`** in `pyproject.toml`. If the
   line isn't there at all, prints a hint asking you to add it manually.

The script is idempotent: re-running with the same `--lang` is a no-op.

## `theme.language` vs plugin `languages`

These are two different things:

- [`theme.language`](https://squidfunk.github.io/mkdocs-material/setup/changing-the-language/)
  is **Material's UI strings** (search placeholder, "Edit this page", footer
  navigation hints). One value site-wide. Material ships translations for
  ~70 locales out of the box.
- `plugins.i18n.languages` is **content translation**. A list. Each entry
  declares a locale that has translated `*.<lang>.md` files.

You almost always want `theme.language` set to your default content language
so the UI matches when readers land on a default-language page.

## `nav_translations`

To translate section titles in the nav (e.g. `Workflows` → `工作流程`), use
`mkdocs-static-i18n`'s per-language `nav_translations`:

```yaml
plugins:
  - i18n:
      docs_structure: suffix
      languages:
        - locale: en
          name: English
          default: true
        - locale: zh-TW
          name: 繁體中文 (zh-TW)
          nav_translations:
            Workflows: 工作流程
            Reference: 參考資料
```

`add-language.sh` does **not** populate `nav_translations` for you —
section names are project-specific and translating them is a deliberate
authorial choice. Add them by hand once you have section titles to translate.

!!! warning "Don't apply 「中文 (English original)」 to nav labels"
    The terminology rule that governs body prose **does not extend to
    `nav_translations` values.** Nav entries are navigation chrome — short
    labels in a sidebar — and bilingual labels like
    `Reference: 參考資料 (Reference)` are too long, wrap awkwardly, and
    duplicate information the URL slug already preserves.

    For nav labels: pick the most common Chinese term for each section
    and stick with it. Stay consistent across the whole nav. The URL
    slug still uses the English source name (`/zh-TW/reference/...`),
    so search engines and direct-link sharing are unaffected.

    Examples:

    | English heading | Good zh-TW label | Bad zh-TW label |
    |---|---|---|
    | `Reference` | `參考資料` | `參考資料 (Reference)` |
    | `Workflows` | `工作流程` | `工作流程 (Workflows)` |
    | `Skills` | `Skills` (keep — domain term, no canonical translation) | `技能 (Skills)` |
    | `Getting started` | `快速開始` | `快速開始 (Getting started)` |

    The "keep English" exception (third row) is reserved for terms where
    no canonical Chinese translation exists. When in doubt, keep English
    — it matches the body-prose rule's spirit (don't invent) without
    duplicating into the label.

## Interaction with `llmstxt` and `copy-to-llm`

- **`mkdocs-llmstxt` is incompatible with `mkdocs-static-i18n` under
  `--strict`.** The llmstxt plugin resolves source URIs against the page
  index, but `reconfigure_material: true` in static-i18n remaps that index,
  so every entry in `llmstxt.sections` triggers `Page URI 'X' not found`
  warnings — which abort `--strict` builds. `sections:` is a required field
  on the llmstxt plugin, so you can't just empty it out.

  **`add-language.sh` keeps `mkdocs-llmstxt` by default** because most users
  opted into this skill specifically to get `/llms.txt`. To make CI happy,
  pair the run with `--drop-strict`, which patches
  `.github/workflows/docs.yml` and `Makefile` to remove `--strict` from any
  `mkdocs build --strict` invocation:

  ```bash
  bash scripts/add-language.sh --lang zh-TW --drop-strict
  ```

  If you'd rather lose `/llms.txt` than lose `--strict`, flip the trade-off
  with `--remove-llmstxt` (the dep stays in `pyproject.toml` either way, so
  re-adding later is one yaml edit):

  ```bash
  bash scripts/add-language.sh --lang zh-TW --remove-llmstxt
  ```

- **`mkdocs-copy-to-llm` button text is English-only.** The "Copy to LLM" /
  "Open in ChatGPT" / "Open in Claude" labels stay in English on
  non-English pages. Customising them requires forking the plugin's CSS/JS —
  out of scope for this skill. Cosmetic only; doesn't break the build.

- **The translation-stub admonition is zh-TW-specific.** The terminology
  rule it injects is written for Traditional Chinese and uses the
  「中文 (English original)」 format. If you add `--lang ja` or another
  language, the admonition still says "Terminology rule (ja pages)" but the
  body is in Chinese. Either edit
  `assets/translation-stub.md.template` to be language-neutral first, or
  hand-edit the stubs after creation.

## Removing a language

To remove `zh-TW` later:

1. Delete the `zh-TW` entry from `plugins[].i18n.languages` in `mkdocs.yml`.
2. (Optional) Delete every `*.zh-TW.md` file under `docs/`.
3. Update `.skills/preferences.yaml`:
   ```bash
   bash scripts/check-preferences.sh \
     --set 'mkdocs_site_bootstrap.languages=["en"]'
   ```
4. If you only had two languages and want to fully remove the plugin, also
   delete the `i18n:` block and re-comment `mkdocs-static-i18n` in
   `pyproject.toml`.

## Reset path

If you want to fully back out of all the i18n decisions and start over:

```bash
bash scripts/check-preferences.sh --reset mkdocs_site_bootstrap
# Then manually revert mkdocs.yml / pyproject.toml as above, and
# re-run init-docs-site.sh or add-language.sh from scratch.
```

The `--reset` clears the recorded decision; the agent will re-interview on
the next invocation.

## Future work — `i18n_structure: folder`

The `i18n_structure` preference key exists, but `add-language.sh` currently
only implements `suffix`. If we add `folder` later, the migration path will
be: walk `docs/`, move every default-language file into `docs/<default>/`,
move every `*.<lang>.md` into `docs/<lang>/<base>.md`, rewrite relative
links. Non-trivial — punted unless someone actually needs it.
