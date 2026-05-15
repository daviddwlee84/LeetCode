#!/usr/bin/env bash
# add-language.sh — Retrofit a non-default language into an existing MkDocs site.
#
# Bash 3.2 compatible. Requires `yq` (mikefarah/yq v4+).
# Idempotent: re-running with the same --lang is a no-op.
#
# What it does (see references/i18n-guide.md for the full story):
#   1. Inserts (or augments) a `plugins.i18n` block in mkdocs.yml using
#      docs_structure: suffix.
#   2. Sets theme.language to the default language if not already set.
#   3. Creates *.<LANG>.md sibling stubs for every existing default-language
#      page, with the terminology-rule admonition pre-injected.
#   4. Records the choice in .skills/preferences.yaml.
#   5. Un-comments mkdocs-static-i18n in pyproject.toml if it's commented out.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ASSETS="$SKILL_DIR/assets"

usage() {
  cat <<'EOF'
Usage: add-language.sh --lang LANG [OPTIONS]

Retrofit a non-default language into an existing MkDocs site (uses
mkdocs-static-i18n with docs_structure: suffix).

Required:
  --lang LANG          Language code to add (e.g. zh-TW, ja, fr, de).

Options:
  --name NAME          Display name (default: derived from LANG, e.g.
                       zh-TW → "繁體中文 (zh-TW)"). Falls back to LANG.
  --default-lang LANG  Default language already on the site (default: en).
                       Used to seed theme.language and i18n.languages[0].
  --target-dir DIR     Repo root (default: walk up from CWD looking for mkdocs.yml).
  --no-stubs           Skip creating *.<LANG>.md sibling stubs.
  --remove-llmstxt     Remove the mkdocs-llmstxt plugin entry from mkdocs.yml.
                       Default behaviour KEEPS llmstxt because /llms.txt is the
                       LLM-friendly feature most users wanted in the first place.
                       Trade-off: llmstxt's source-path lookups break under
                       mkdocs-static-i18n's reconfigure_material, so 'mkdocs
                       build --strict' aborts with "Page URI not found" warnings.
                       Pair --remove-llmstxt with keeping --strict; OR keep
                       llmstxt (default) and pass --drop-strict to patch your
                       CI/Makefile so the build doesn't fail on warnings.
  --drop-strict        Patch .github/workflows/docs.yml and Makefile to remove
                       '--strict' from any 'mkdocs build --strict' invocation.
                       Use when keeping llmstxt with i18n. Idempotent.
  --dry-run            Print actions without writing.
  --force              Overwrite existing *.<LANG>.md stubs (default: skip).
  --help, -h           Show this help and exit.

Examples:
  add-language.sh --lang zh-TW                              # add Traditional Chinese
  add-language.sh --lang ja --name "日本語"                 # add Japanese with custom name
  add-language.sh --lang zh-TW --dry-run                    # preview changes
  add-language.sh --lang fr --no-stubs                      # plugin only, no stubs

Exit codes:
  0  success
  1  invalid arguments
  2  mkdocs.yml not found
  3  refusing to overwrite (use --force)
  4  yq error
EOF
}

log()  { printf '%s\n' "$*" >&2; }
die()  { printf 'error: %s\n' "$*" >&2; exit "${2:-1}"; }

LOCALE=""
LOCALE_NAME=""
DEFAULT_LANG="en"
TARGET=""
NO_STUBS=0
REMOVE_LLMSTXT=0
DROP_STRICT=0
DRY_RUN=0
FORCE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --lang)            LOCALE="${2:-}"; shift 2 ;;
    --name)            LOCALE_NAME="${2:-}"; shift 2 ;;
    --default-lang)    DEFAULT_LANG="${2:-}"; shift 2 ;;
    --target-dir)      TARGET="${2:-}"; shift 2 ;;
    --no-stubs)        NO_STUBS=1; shift ;;
    --remove-llmstxt)  REMOVE_LLMSTXT=1; shift ;;
    --drop-strict)     DROP_STRICT=1; shift ;;
    --dry-run)         DRY_RUN=1; shift ;;
    --force)           FORCE=1; shift ;;
    --help|-h)         usage; exit 0 ;;
    -*)                die "unknown flag: $1 (try --help)" 1 ;;
    *)                 die "unexpected positional argument: $1" 1 ;;
  esac
done

[ -n "$LOCALE" ] || die "--lang is required (try --help)" 1
command -v yq >/dev/null 2>&1 || die "yq not found in PATH (install: brew install yq)" 4

# --- Locate mkdocs.yml ---
if [ -z "$TARGET" ]; then
  cur="$(pwd)"
  while [ "$cur" != "/" ]; do
    if [ -f "$cur/mkdocs.yml" ]; then TARGET="$cur"; break; fi
    cur="$(dirname "$cur")"
  done
  [ -n "$TARGET" ] || die "could not find mkdocs.yml walking up from $(pwd)" 2
fi
MKDOCS="$TARGET/mkdocs.yml"
[ -f "$MKDOCS" ] || die "no mkdocs.yml in $TARGET" 2
DOCS_DIR="$TARGET/docs"

# --- Derive display name if not given ---
if [ -z "$LOCALE_NAME" ]; then
  case "$LOCALE" in
    zh-TW) LOCALE_NAME="繁體中文 (zh-TW)" ;;
    zh-CN) LOCALE_NAME="简体中文 (zh-CN)" ;;
    ja)    LOCALE_NAME="日本語 (ja)" ;;
    ko)    LOCALE_NAME="한국어 (ko)" ;;
    fr)    LOCALE_NAME="Français (fr)" ;;
    de)    LOCALE_NAME="Deutsch (de)" ;;
    es)    LOCALE_NAME="Español (es)" ;;
    pt)    LOCALE_NAME="Português (pt)" ;;
    it)    LOCALE_NAME="Italiano (it)" ;;
    en)    LOCALE_NAME="English" ;;
    *)     LOCALE_NAME="$LOCALE" ;;
  esac
fi

DEFAULT_NAME="English"
[ "$DEFAULT_LANG" = "en" ] || DEFAULT_NAME="$DEFAULT_LANG"

log "Target: $TARGET"
log "Locale: $LOCALE ($LOCALE_NAME)"
log "Default language: $DEFAULT_LANG"

# --- Detect current i18n state ---
HAS_I18N=$(yq '[.plugins[]? | select(type == "!!map") | keys | .[0]] | contains(["i18n"])' "$MKDOCS" 2>/dev/null || echo "false")
HAS_LOCALE="false"
if [ "$HAS_I18N" = "true" ]; then
  HAS_LOCALE=$(LOC="$LOCALE" yq '[.plugins[]? | select(has("i18n")) | .i18n.languages[].locale] | contains([env(LOC)])' "$MKDOCS" 2>/dev/null || echo "false")
fi

log "i18n plugin present: $HAS_I18N"
log "Locale already configured: $HAS_LOCALE"

# --- yq write helper ---
yq_inplace() {
  local expr="$1"
  if [ "$DRY_RUN" = "1" ]; then
    log "[dry-run] yq -i '$expr' $MKDOCS"
    return 0
  fi
  local tmp="${MKDOCS}.tmp.$$"
  yq "$expr" "$MKDOCS" > "$tmp" || { rm -f "$tmp"; die "yq failed: $expr" 4; }
  mv "$tmp" "$MKDOCS"
}

# --- Step 1: insert / extend plugins.i18n ---
if [ "$HAS_I18N" = "false" ]; then
  log "Inserting plugins.i18n block..."
  yq_inplace "
    .plugins = (
      [{
        \"i18n\": {
          \"docs_structure\": \"suffix\",
          \"fallback_to_default\": true,
          \"reconfigure_material\": true,
          \"reconfigure_search\": true,
          \"languages\": [
            {\"locale\": \"$DEFAULT_LANG\", \"name\": \"$DEFAULT_NAME\", \"default\": true},
            {\"locale\": \"$LOCALE\", \"name\": \"$LOCALE_NAME\"}
          ]
        }
      }] + (.plugins // [])
    )
  "
elif [ "$HAS_LOCALE" = "false" ]; then
  log "Appending $LOCALE to existing plugins.i18n.languages..."
  yq_inplace "
    .plugins |= map(
      if has(\"i18n\") then
        .i18n.languages += [{\"locale\": \"$LOCALE\", \"name\": \"$LOCALE_NAME\"}]
      else
        .
      end
    )
  "
else
  log "Locale $LOCALE already in plugins.i18n.languages — no plugin change."
fi

# --- Step 2: set theme.language if missing ---
THEME_LANG=$(yq -r '.theme.language // ""' "$MKDOCS" 2>/dev/null || echo "")
if [ -z "$THEME_LANG" ]; then
  log "Setting theme.language: $DEFAULT_LANG"
  yq_inplace ".theme.language = \"$DEFAULT_LANG\""
elif [ "$THEME_LANG" != "$DEFAULT_LANG" ]; then
  log "Note: theme.language is already '$THEME_LANG' (not '$DEFAULT_LANG'). Leaving as-is."
fi

# --- Step 2b: drop theme features incompatible with mkdocs-static-i18n ---
# The plugin's contextual language switcher is incompatible with
# navigation.instant (DOM links injected via instant nav can't be rewritten
# per language). Removing navigation.instant on first i18n add.
HAS_INSTANT=$(yq '.theme.features // [] | contains(["navigation.instant"])' "$MKDOCS" 2>/dev/null || echo "false")
if [ "$HAS_INSTANT" = "true" ]; then
  log "Removing navigation.instant / navigation.instant.progress (incompatible with i18n language switcher)..."
  yq_inplace '.theme.features |= ((. // []) - ["navigation.instant", "navigation.instant.progress"])'
fi

# --- Step 2c: handle mkdocs-llmstxt incompatibility ---
# mkdocs-llmstxt resolves source URIs against the page index, which
# mkdocs-static-i18n's reconfigure_material remaps. Result: every entry in
# llmstxt.sections triggers a "Page URI not found" warning, which aborts
# `mkdocs build --strict`. Auto-discovery isn't an option (sections: is
# required by the llmstxt schema).
# Default: KEEP llmstxt — most users opted into this skill BECAUSE of the
# /llms.txt feature. Pair with --drop-strict to neutralise the warnings in
# CI. --remove-llmstxt is the opt-out for users who'd rather keep --strict.
HAS_LLMSTXT=$(yq '[.plugins[]? | select(has("llmstxt"))] | length > 0' "$MKDOCS" 2>/dev/null || echo "false")
if [ "$HAS_LLMSTXT" = "true" ]; then
  if [ "$REMOVE_LLMSTXT" = "1" ]; then
    log "Removing mkdocs-llmstxt plugin entry (--remove-llmstxt)..."
    yq_inplace 'del(.plugins[] | select(has("llmstxt")))'
  else
    log "Keeping mkdocs-llmstxt (default). 'mkdocs build --strict' will fail"
    log "  with 'Page URI not found' warnings — pair with --drop-strict, or"
    log "  drop --strict from your CI manually."
  fi
fi

# --- Step 2d: optionally drop --strict from CI files ---
if [ "$DROP_STRICT" = "1" ]; then
  for ci_file in "$TARGET/.github/workflows/docs.yml" "$TARGET/Makefile"; do
    [ -f "$ci_file" ] || continue
    if ! grep -q 'mkdocs build --strict' "$ci_file" 2>/dev/null; then
      continue
    fi
    if [ "$DRY_RUN" = "1" ]; then
      log "[dry-run] drop --strict in $ci_file"
    else
      sed -i.bak -E 's|mkdocs build --strict|mkdocs build|g' "$ci_file"
      rm -f "${ci_file}.bak"
      log "Dropped --strict from $ci_file"
    fi
  done
fi

# --- Step 3: collect all configured locales for stub-skipping ---
# Compute deterministically so dry-run shows the post-state, not the pre-state.
if [ "$HAS_LOCALE" = "true" ]; then
  ALL_LOCALES=$(yq '.plugins[]? | select(has("i18n")) | .i18n.languages[].locale' "$MKDOCS" 2>/dev/null | tr '\n' ' ')
elif [ "$HAS_I18N" = "true" ]; then
  OLD_LOCALES=$(yq '.plugins[]? | select(has("i18n")) | .i18n.languages[].locale' "$MKDOCS" 2>/dev/null | tr '\n' ' ')
  ALL_LOCALES="${OLD_LOCALES}${LOCALE}"
else
  ALL_LOCALES="$DEFAULT_LANG $LOCALE"
fi
log "All configured locales: $ALL_LOCALES"

# --- Step 4: create *.LANG.md sibling stubs ---
STUBS_CREATED=0
STUBS_EXISTING=0
STUBS_SKIPPED=0
STUB_TEMPLATE="$ASSETS/translation-stub.md.template"

if [ "$NO_STUBS" = "1" ]; then
  log "Skipping stub creation (--no-stubs)."
elif [ ! -d "$DOCS_DIR" ]; then
  log "No docs/ dir — skipping stub creation."
elif [ ! -f "$STUB_TEMPLATE" ]; then
  die "stub template missing: $STUB_TEMPLATE" 4
else
  TMP_LIST="$(mktemp)"
  find "$DOCS_DIR" -type f -name '*.md' \
    -not -path "$DOCS_DIR/_snippets/*" \
    -not -path "$DOCS_DIR/assets/*" \
    > "$TMP_LIST" 2>/dev/null || true

  while IFS= read -r src; do
    [ -z "$src" ] && continue
    base="${src%.md}"
    # Skip if this file is itself a locale-suffixed sibling.
    is_locale=0
    for loc in $ALL_LOCALES; do
      case "${base}" in
        *.$loc) is_locale=1; break ;;
      esac
    done
    [ "$is_locale" = "1" ] && { STUBS_SKIPPED=$((STUBS_SKIPPED + 1)); continue; }

    target="${base}.${LOCALE}.md"
    if [ -e "$target" ] && [ "$FORCE" = "0" ]; then
      STUBS_EXISTING=$((STUBS_EXISTING + 1))
      continue
    fi

    # Extract title from source (first '# ' heading), fallback to filename.
    src_title=$(grep -m1 '^# ' "$src" 2>/dev/null | sed 's/^# *//' || true)
    [ -n "$src_title" ] || src_title="$(basename "$src" .md)"

    if [ "$DRY_RUN" = "1" ]; then
      log "[dry-run] create $target  (title: $src_title)"
    else
      sed -e "s|{{PAGE_TITLE}}|${src_title}|g" \
          -e "s|{{LANG}}|${LOCALE}|g" \
          "$STUB_TEMPLATE" > "$target"
    fi
    STUBS_CREATED=$((STUBS_CREATED + 1))
  done < "$TMP_LIST"
  rm -f "$TMP_LIST"
fi

log "Stubs: $STUBS_CREATED created, $STUBS_EXISTING already existed, $STUBS_SKIPPED skipped (locale-suffixed)"

# --- Step 5: update preferences ---
PREFS="$SKILL_DIR/scripts/check-preferences.sh"
ALL_LOCALES_LITERAL="["
first=1
for loc in $ALL_LOCALES; do
  [ -z "$loc" ] && continue
  if [ "$first" = "1" ]; then
    ALL_LOCALES_LITERAL="${ALL_LOCALES_LITERAL}\"$loc\""
    first=0
  else
    ALL_LOCALES_LITERAL="${ALL_LOCALES_LITERAL}, \"$loc\""
  fi
done
ALL_LOCALES_LITERAL="${ALL_LOCALES_LITERAL}]"

if [ "$DRY_RUN" = "1" ]; then
  log "[dry-run] check-preferences.sh --set mkdocs_site_bootstrap.languages=$ALL_LOCALES_LITERAL"
  log "[dry-run] check-preferences.sh --set mkdocs_site_bootstrap.keep_english_terms=true"
  log "[dry-run] check-preferences.sh --set mkdocs_site_bootstrap.i18n_structure=suffix"
else
  bash "$PREFS" \
    --set "mkdocs_site_bootstrap.languages=$ALL_LOCALES_LITERAL" \
    --set "mkdocs_site_bootstrap.keep_english_terms=true" \
    --set "mkdocs_site_bootstrap.i18n_structure=suffix" \
    >/dev/null
fi

# --- Step 6: uncomment mkdocs-static-i18n in pyproject.toml ---
PYPROJECT="$TARGET/pyproject.toml"
if [ -f "$PYPROJECT" ]; then
  if grep -qE '^[[:space:]]*"mkdocs-static-i18n' "$PYPROJECT"; then
    log "pyproject.toml already lists mkdocs-static-i18n — leaving alone."
  elif grep -qE '^[[:space:]]*#[[:space:]]*"mkdocs-static-i18n' "$PYPROJECT"; then
    if [ "$DRY_RUN" = "1" ]; then
      log "[dry-run] uncomment mkdocs-static-i18n in $PYPROJECT"
    else
      sed -i.bak -E 's|^([[:space:]]*)#[[:space:]]*("mkdocs-static-i18n[^"]*",)|\1\2|' "$PYPROJECT"
      rm -f "${PYPROJECT}.bak"
      log "Uncommented mkdocs-static-i18n in $PYPROJECT"
    fi
  else
    log "Note: mkdocs-static-i18n not found in $PYPROJECT. Add manually:"
    log '        "mkdocs-static-i18n>=1.2",'
  fi
else
  log "Note: no pyproject.toml in $TARGET. Install mkdocs-static-i18n yourself."
fi

if [ "$DRY_RUN" = "1" ]; then
  log "Dry run complete."
  exit 0
fi

# --- Structured success output ---
LANGUAGES_JSON=""
for loc in $ALL_LOCALES; do
  [ -z "$loc" ] && continue
  if [ -z "$LANGUAGES_JSON" ]; then
    LANGUAGES_JSON="\"$loc\""
  else
    LANGUAGES_JSON="$LANGUAGES_JSON,\"$loc\""
  fi
done

printf '{"lang":"%s","stubs_created":%d,"stubs_existing":%d,"languages":[%s]}\n' \
  "$LOCALE" "$STUBS_CREATED" "$STUBS_EXISTING" "$LANGUAGES_JSON"

# --- Post-run tips (stderr, agent-readable) ---
# These nudge the next step without taking action. The script's job is the
# structural retrofit; translation and nav-label decisions are deliberate
# authoring work that needs human judgment.
if [ "$STUBS_CREATED" -gt 0 ] || [ "$STUBS_EXISTING" -gt 0 ]; then
  log ""
  log "Next steps:"
  log "  1. Stubs are placeholders. Each $LOCALE page contains the terminology"
  log "     admonition + a 'Translation pending' warning, and is otherwise empty."
  log "     Ask the user whether to translate them page-by-page now"
  log "     (recommended batch size: 4-6 pages, run 'mkdocs build' between batches)."
  log "     Translation is a separate authoring task — proceed only on explicit yes."
  log ""
  log "  2. Section headings in mkdocs.yml's nav stay in the default language."
  log "     To translate them (e.g. 'Reference' -> '參考資料'), add a"
  log "     nav_translations: block under the $LOCALE entry in mkdocs.yml."
  log "     See references/i18n-guide.md §nav_translations."
fi
