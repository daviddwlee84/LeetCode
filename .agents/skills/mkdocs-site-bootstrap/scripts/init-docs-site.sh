#!/usr/bin/env bash
# init-docs-site.sh — Scaffold a MkDocs Material docs site in the current repo.
#
# Bash 3.2 compatible. See SKILL.md for the full workflow including consent
# gates and existing-docs handling (which the agent does, not this script).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
ASSETS="$SKILL_DIR/assets"

usage() {
  cat <<'EOF'
Usage: init-docs-site.sh [OPTIONS]

Scaffold mkdocs.yml, pyproject.toml (docs extras), .github/workflows/docs.yml,
and a starter docs/ tree in the current repo (or --target-dir).

Options:
  --site-name NAME         Display name for the site (required).
  --site-description DESC  One-paragraph site description (default: derived from --site-name).
  --site-url URL           Public URL (e.g., https://owner.github.io/repo/) (required).
  --repo-slug owner/repo   GitHub slug (required).
  --repo-name NAME         Python package-ish name for pyproject.toml (default: repo basename).
  --target-dir DIR         Repo root (default: walk up from CWD looking for .git).
  --existing skip|wrap     How to handle existing docs/ (default: skip — leave as-is, empty nav).
                           wrap: add files to nav alphabetically.
  --no-workflow            Don't create .github/workflows/docs.yml.
  --no-skeleton            Don't create the docs/ skeleton (use existing docs/ as-is).
  --dry-run                Print actions without writing.
  --force                  Overwrite existing files (mkdocs.yml, pyproject.toml).
  --help, -h               Show this help and exit.

Examples:
  init-docs-site.sh \
    --site-name "My Project" \
    --site-url https://owner.github.io/repo/ \
    --repo-slug owner/repo

  init-docs-site.sh --dry-run --site-name X --site-url https://x.io/ --repo-slug a/b

Exit codes:
  0  success
  1  invalid arguments
  2  target dir not found
  3  refusing to overwrite (use --force)
  4  template missing
EOF
}

log()  { printf '%s\n' "$*" >&2; }
die()  { printf 'error: %s\n' "$*" >&2; exit "${2:-1}"; }

SITE_NAME=""
SITE_DESC=""
SITE_URL=""
REPO_SLUG=""
REPO_NAME=""
TARGET=""
EXISTING="skip"
NO_WORKFLOW=0
NO_SKELETON=0
DRY_RUN=0
FORCE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --site-name)        SITE_NAME="${2:-}"; shift 2 ;;
    --site-description) SITE_DESC="${2:-}"; shift 2 ;;
    --site-url)         SITE_URL="${2:-}"; shift 2 ;;
    --repo-slug)        REPO_SLUG="${2:-}"; shift 2 ;;
    --repo-name)        REPO_NAME="${2:-}"; shift 2 ;;
    --target-dir)       TARGET="${2:-}"; shift 2 ;;
    --existing)         EXISTING="${2:-}"; shift 2 ;;
    --no-workflow)      NO_WORKFLOW=1; shift ;;
    --no-skeleton)      NO_SKELETON=1; shift ;;
    --dry-run)          DRY_RUN=1; shift ;;
    --force)            FORCE=1; shift ;;
    --help|-h)          usage; exit 0 ;;
    -*)                 die "unknown flag: $1 (try --help)" 1 ;;
    *)                  die "unexpected positional argument: $1" 1 ;;
  esac
done

[ -n "$SITE_NAME" ] || die "--site-name is required (try --help)" 1
[ -n "$SITE_URL" ]  || die "--site-url is required" 1
[ -n "$REPO_SLUG" ] || die "--repo-slug is required (e.g. owner/repo)" 1
case "$EXISTING" in skip|wrap) ;; *) die "--existing must be 'skip' or 'wrap'" 1 ;; esac

[ -n "$SITE_DESC" ] || SITE_DESC="Documentation for $SITE_NAME"

# Resolve target dir.
if [ -z "$TARGET" ]; then
  cur="$(pwd)"
  while [ "$cur" != "/" ]; do
    if [ -d "$cur/.git" ]; then TARGET="$cur"; break; fi
    cur="$(dirname "$cur")"
  done
  [ -n "$TARGET" ] || TARGET="$(pwd)"
fi
[ -d "$TARGET" ] || die "target dir not found: $TARGET" 2

[ -n "$REPO_NAME" ] || REPO_NAME="$(basename "$TARGET")"

log "Target: $TARGET"
log "Site:   $SITE_NAME @ $SITE_URL"
log "Repo:   $REPO_SLUG"

# --- helper: substitute {{VAR}} placeholders ---
substitute() {
  local file="$1"
  if [ "$DRY_RUN" = "1" ]; then
    log "[dry-run] would substitute placeholders in $file"
    return 0
  fi
  sed -i.bak \
    -e "s|{{SITE_NAME}}|${SITE_NAME}|g" \
    -e "s|{{SITE_DESCRIPTION}}|${SITE_DESC}|g" \
    -e "s|{{SITE_URL}}|${SITE_URL}|g" \
    -e "s|{{REPO_SLUG}}|${REPO_SLUG}|g" \
    -e "s|{{REPO_NAME}}|${REPO_NAME}|g" \
    "$file"
  rm -f "${file}.bak"
}

# --- helper: copy template, refusing to overwrite unless --force ---
copy_template() {
  local src="$1" dst="$2"
  [ -f "$src" ] || die "template missing: $src" 4
  if [ -e "$dst" ] && [ "$FORCE" = "0" ]; then
    die "exists, refusing to overwrite: $dst (use --force)" 3
  fi
  if [ "$DRY_RUN" = "1" ]; then
    log "[dry-run] cp $src → $dst"
    return 0
  fi
  mkdir -p "$(dirname "$dst")"
  cp "$src" "$dst"
}

# --- 1. mkdocs.yml ---
copy_template "$ASSETS/mkdocs.yml.template" "$TARGET/mkdocs.yml"
substitute "$TARGET/mkdocs.yml"

# --- 2. pyproject.toml ---
if [ -e "$TARGET/pyproject.toml" ]; then
  log "Note: $TARGET/pyproject.toml already exists; not modifying it."
  log "      Add this to your [project.optional-dependencies]:"
  log "        docs = [\"mkdocs>=1.6\", \"mkdocs-material>=9.5\","
  log "                \"mkdocs-llmstxt>=0.2\", \"mkdocs-copy-to-llm>=0.1\","
  log "                \"pymdown-extensions>=10.7\"]"
else
  copy_template "$ASSETS/pyproject.toml.template" "$TARGET/pyproject.toml"
  substitute "$TARGET/pyproject.toml"
fi

# --- 3. .github/workflows/docs.yml ---
if [ "$NO_WORKFLOW" = "0" ]; then
  copy_template "$ASSETS/docs-workflow.yml.template" "$TARGET/.github/workflows/docs.yml"
fi

# --- 4. docs/ skeleton ---
if [ "$NO_SKELETON" = "0" ]; then
  if [ -d "$TARGET/docs" ] && [ "$(ls -A "$TARGET/docs" 2>/dev/null)" != "" ]; then
    log "Note: docs/ already has content. Honoring --existing=$EXISTING:"
    case "$EXISTING" in
      skip)
        log "  Skipping skeleton creation (existing files left alone)."
        log "  mkdocs.yml has empty nav: — MkDocs will auto-generate from filesystem."
        ;;
      wrap)
        log "  Existing files will be picked up by MkDocs auto-nav."
        log "  Edit mkdocs.yml's nav: block to reorder."
        ;;
    esac
  else
    if [ "$DRY_RUN" = "1" ]; then
      log "[dry-run] would copy docs-skeleton/* → $TARGET/docs/"
    else
      mkdir -p "$TARGET/docs/_snippets" "$TARGET/docs/assets/copy-to-llm"
      copy_template "$ASSETS/docs-skeleton/index.md" "$TARGET/docs/index.md"
      substitute "$TARGET/docs/index.md"
      copy_template "$ASSETS/docs-skeleton/getting-started.md" "$TARGET/docs/getting-started.md"
      substitute "$TARGET/docs/getting-started.md"
      copy_template "$ASSETS/docs-skeleton/_snippets/README.md" "$TARGET/docs/_snippets/README.md"
      cp "$ASSETS/docs-skeleton/assets/copy-to-llm/"* "$TARGET/docs/assets/copy-to-llm/"
    fi
  fi
fi

if [ "$DRY_RUN" = "1" ]; then
  log "Dry run complete."
  exit 0
fi

# Structured success output.
printf '{"target":"%s","site_name":"%s","site_url":"%s","next_steps":[' "$TARGET" "$SITE_NAME" "$SITE_URL"
printf '"uv sync --extra docs",'
printf '"uv run mkdocs build --strict",'
printf '"git add and commit the new files",'
printf '"Run enable-pages.sh to deploy to GitHub Pages"]}\n'
