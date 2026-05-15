#!/usr/bin/env bash
# check-preferences.sh — Read, set, or reset .skills/preferences.yaml.
#
# Per-repo preferences for skills that need to remember user decisions across
# sessions. See references/preferences-schema.md for the schema.
#
# Bash 3.2 compatible. Requires `yq` (mikefarah/yq v4+).

set -euo pipefail

usage() {
  cat <<'EOF'
Usage: check-preferences.sh [OPTIONS]

Read, write, or reset entries in .skills/preferences.yaml (per-repo).

Options:
  --get KEY                  Print the value at KEY (e.g., mkdocs_site_bootstrap.enabled).
                             Prints empty string + exits 0 if absent.
  --set KEY=VALUE            Set a key. Repeatable. VALUE is parsed as YAML
                             (so 'true', '42', '2026-04-23', and bare strings
                             all work). Quote complex values.
  --reset NAMESPACE          Delete the entire top-level NAMESPACE key (returns
                             that skill to "never asked" state).
  --list                     Print the entire file (or "(empty)" if missing).
  --file PATH                Override file location (default: .skills/preferences.yaml
                             in the current dir or the first ancestor that has
                             a .git directory).
  --json                     Format --get / --list output as JSON.
  --dry-run                  Print actions but don't write.
  --help, -h                 Show this help and exit.

Examples:
  check-preferences.sh --get mkdocs_site_bootstrap.enabled
  check-preferences.sh --set mkdocs_site_bootstrap.enabled=true \
                       --set mkdocs_site_bootstrap.decided_at=2026-04-23
  check-preferences.sh --reset mkdocs_site_bootstrap
  check-preferences.sh --list --json

Exit codes:
  0  success (key absent on --get is also success — empty stdout)
  1  invalid arguments
  2  file/dir not accessible
  3  yq missing or yq error
EOF
}

log()  { printf '%s\n' "$*" >&2; }
die()  { printf 'error: %s\n' "$*" >&2; exit "${2:-1}"; }

# --- arg parsing ---
ACTION=""
KEY=""
NAMESPACE=""
FILE=""
JSON=0
DRY_RUN=0
SET_PAIRS=()

while [ $# -gt 0 ]; do
  case "$1" in
    --get)        ACTION="get"; KEY="${2:-}"; shift 2 ;;
    --set)        ACTION="set"; SET_PAIRS+=("${2:-}"); shift 2 ;;
    --reset)      ACTION="reset"; NAMESPACE="${2:-}"; shift 2 ;;
    --list)       ACTION="list"; shift ;;
    --file)       FILE="${2:-}"; shift 2 ;;
    --json)       JSON=1; shift ;;
    --dry-run)    DRY_RUN=1; shift ;;
    --help|-h)    usage; exit 0 ;;
    -*)           die "unknown flag: $1 (try --help)" 1 ;;
    *)            die "unexpected positional argument: $1 (try --help)" 1 ;;
  esac
done

[ -n "$ACTION" ] || die "must specify one of --get/--set/--reset/--list (try --help)" 1

command -v yq >/dev/null 2>&1 || die "yq not found in PATH (install: brew install yq)" 3

# --- file resolution ---
if [ -z "$FILE" ]; then
  cur="$(pwd)"
  ROOT=""
  while [ "$cur" != "/" ]; do
    if [ -d "$cur/.git" ]; then ROOT="$cur"; break; fi
    cur="$(dirname "$cur")"
  done
  if [ -z "$ROOT" ]; then ROOT="$(pwd)"; fi
  FILE="$ROOT/.skills/preferences.yaml"
fi

ensure_file() {
  local dir
  dir="$(dirname "$FILE")"
  if [ ! -d "$dir" ]; then
    [ "$DRY_RUN" = "1" ] && { log "[dry-run] mkdir -p $dir"; return 0; }
    mkdir -p "$dir"
  fi
  if [ ! -f "$FILE" ]; then
    [ "$DRY_RUN" = "1" ] && { log "[dry-run] touch $FILE with header"; return 0; }
    cat >"$FILE" <<'EOF'
# .skills/preferences.yaml
# Per-repo preferences recorded by skills. Each top-level key is a skill
# namespace. See:
#   skills/local/mkdocs-site-bootstrap/references/preferences-schema.md
EOF
  fi
}

# --- actions ---
case "$ACTION" in

get)
  [ -n "$KEY" ] || die "--get requires KEY" 1
  if [ ! -f "$FILE" ]; then
    if [ "$JSON" = "1" ]; then printf 'null\n'; fi
    exit 0
  fi
  # yq prints "null" for missing; convert to empty string for shell-friendliness.
  VALUE=$(yq -r ".${KEY}" "$FILE" 2>/dev/null || echo "null")
  if [ "$JSON" = "1" ]; then
    yq -o=json ".${KEY}" "$FILE" 2>/dev/null || printf 'null\n'
  else
    if [ "$VALUE" = "null" ]; then
      printf ''
    else
      printf '%s\n' "$VALUE"
    fi
  fi
  ;;

set)
  [ "${#SET_PAIRS[@]}" -gt 0 ] || die "--set requires at least one KEY=VALUE" 1
  ensure_file

  # Build a single yq expression so we make one atomic write.
  EXPR=""
  for pair in "${SET_PAIRS[@]}"; do
    case "$pair" in
      *=*) ;;
      *) die "--set value must be KEY=VALUE (got '$pair')" 1 ;;
    esac
    k="${pair%%=*}"
    v="${pair#*=}"
    # Quote v as a YAML scalar; let yq interpret bool/int unquoted.
    # Dates and everything else go through as strings (quoted) — yq treats
    # ISO-8601 unquoted as arithmetic / invalid expression.
    case "$v" in
      true|false|null) yv="$v" ;;
      \[*\]|\{*\}) yv="$v" ;;  # YAML flow sequence/mapping pass-through
      ''|*[!0-9]*) yv="\"${v//\"/\\\"}\"" ;;
      *) yv="$v" ;;
    esac
    if [ -z "$EXPR" ]; then
      EXPR=".${k} = ${yv}"
    else
      EXPR="${EXPR} | .${k} = ${yv}"
    fi
  done

  if [ "$DRY_RUN" = "1" ]; then
    log "[dry-run] yq -i '$EXPR' $FILE"
    exit 0
  fi

  TMP="${FILE}.tmp.$$"
  yq "$EXPR" "$FILE" > "$TMP" || { rm -f "$TMP"; die "yq failed applying: $EXPR" 3; }
  mv "$TMP" "$FILE"
  log "Updated $FILE"
  ;;

reset)
  [ -n "$NAMESPACE" ] || die "--reset requires NAMESPACE" 1
  if [ ! -f "$FILE" ]; then
    log "Nothing to reset (file does not exist): $FILE"
    exit 0
  fi
  if [ "$DRY_RUN" = "1" ]; then
    log "[dry-run] yq -i 'del(.${NAMESPACE})' $FILE"
    exit 0
  fi
  TMP="${FILE}.tmp.$$"
  yq "del(.${NAMESPACE})" "$FILE" > "$TMP" || { rm -f "$TMP"; die "yq failed deleting .${NAMESPACE}" 3; }
  mv "$TMP" "$FILE"
  log "Reset namespace .${NAMESPACE} in $FILE"
  ;;

list)
  if [ ! -f "$FILE" ]; then
    if [ "$JSON" = "1" ]; then printf '{}\n'; else printf '(empty: %s)\n' "$FILE"; fi
    exit 0
  fi
  if [ "$JSON" = "1" ]; then
    yq -o=json '.' "$FILE"
  else
    cat "$FILE"
  fi
  ;;

esac
