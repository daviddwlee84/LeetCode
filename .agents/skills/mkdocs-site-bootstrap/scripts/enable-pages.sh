#!/usr/bin/env bash
# enable-pages.sh — Enable GitHub Pages (Actions source) and trigger first deploy.
#
# Bash 3.2 compatible. Requires `gh` (GitHub CLI), authenticated.
#
# IMPORTANT: This is a high-trust action. The agent invoking this should have
# already obtained explicit user consent for the API call. The script itself
# enforces nothing beyond --dry-run; consent gating happens upstream in SKILL.md.

set -euo pipefail

usage() {
  cat <<'EOF'
Usage: enable-pages.sh [OPTIONS]

Enable GitHub Pages with Actions as source (POST /repos/:owner/:repo/pages
with build_type=workflow), then trigger the docs.yml workflow.

Options:
  --repo OWNER/REPO     Target repo (default: current repo via `gh repo view`).
  --workflow NAME       Workflow file to dispatch (default: docs.yml).
  --no-trigger          Enable Pages but don't trigger workflow run.
  --dry-run             Print the gh commands without executing.
  --help, -h            Show this help and exit.

Examples:
  enable-pages.sh --repo daviddwlee84/agent-skills
  enable-pages.sh --dry-run
  enable-pages.sh --no-trigger --repo owner/repo

Exit codes:
  0  success
  1  invalid arguments
  2  gh not installed or not authenticated
  3  Pages API call failed (already enabled is OK; other errors not OK)
  4  workflow trigger failed
EOF
}

log()  { printf '%s\n' "$*" >&2; }
die()  { printf 'error: %s\n' "$*" >&2; exit "${2:-1}"; }

REPO=""
WORKFLOW="docs.yml"
NO_TRIGGER=0
DRY_RUN=0

while [ $# -gt 0 ]; do
  case "$1" in
    --repo)        REPO="${2:-}"; shift 2 ;;
    --workflow)    WORKFLOW="${2:-}"; shift 2 ;;
    --no-trigger)  NO_TRIGGER=1; shift ;;
    --dry-run)     DRY_RUN=1; shift ;;
    --help|-h)     usage; exit 0 ;;
    -*)            die "unknown flag: $1 (try --help)" 1 ;;
    *)             die "unexpected positional argument: $1" 1 ;;
  esac
done

command -v gh >/dev/null 2>&1 || die "gh CLI not found in PATH (install: brew install gh)" 2
gh auth status >/dev/null 2>&1 || die "gh not authenticated (run: gh auth login)" 2

# Resolve repo from current dir if not supplied.
if [ -z "$REPO" ]; then
  REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner 2>/dev/null || true)
  [ -n "$REPO" ] || die "could not detect repo from current dir; pass --repo OWNER/REPO" 1
fi
log "Target repo: $REPO"

# --- 1. Enable Pages ---
PAGES_CMD="gh api -X POST repos/$REPO/pages -f build_type=workflow"
if [ "$DRY_RUN" = "1" ]; then
  log "[dry-run] $PAGES_CMD"
else
  log "Enabling GitHub Pages..."
  # Capture both stdout and stderr; tolerate "already enabled" 409.
  set +e
  OUT=$(gh api -X POST "repos/$REPO/pages" -f 'build_type=workflow' 2>&1)
  RC=$?
  set -e
  if [ $RC -ne 0 ]; then
    case "$OUT" in
      *"already enabled"*|*"409"*)
        log "Pages already enabled — continuing."
        ;;
      *)
        die "Pages API call failed: $OUT" 3
        ;;
    esac
  else
    log "Pages enabled. Site will be at: $(printf '%s\n' "$OUT" | sed -nE 's/.*"html_url":"([^"]+)".*/\1/p' | head -1)"
  fi
fi

# --- 2. Trigger workflow ---
if [ "$NO_TRIGGER" = "1" ]; then
  log "Skipping workflow trigger (--no-trigger)."
  exit 0
fi

DISPATCH_CMD="gh workflow run $WORKFLOW --repo $REPO"
if [ "$DRY_RUN" = "1" ]; then
  log "[dry-run] $DISPATCH_CMD"
  exit 0
fi

log "Triggering workflow: $WORKFLOW"
gh workflow run "$WORKFLOW" --repo "$REPO" || die "workflow dispatch failed" 4

# Brief pause then list latest run.
sleep 3
log "Latest run:"
gh run list --workflow="$WORKFLOW" --repo "$REPO" --limit 1 >&2 || true

printf '{"repo":"%s","workflow":"%s","status":"triggered","check_with":"gh run watch --repo %s"}\n' \
  "$REPO" "$WORKFLOW" "$REPO"
