#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Check for secrets in agent artifact directories (specstory history + coding
agent plan/rules dirs) using gitleaks and detect-private-key patterns.
Reports findings and suggests redaction.

Default covered prefixes (kept in sync with assets/artifact-dirs.txt):
    .specstory/history/   (SpecStory chat transcripts)
    .claude/plans/        (Claude Code plans)
    .cursor/plans/        (Cursor plans)
    .cursor/rules/        (Cursor rules)
    .opencode/plans/      (OpenCode plans)
    .specify/             (GitHub spec-kit artifacts)
    .codex/               (Codex CLI artifacts)

Usage:
    ./redact_secrets.py                         # Check staged files (default paths)
    ./redact_secrets.py --fix                   # Auto-redact and re-stage files
    ./redact_secrets.py --working-dir           # Scan working directory instead of staged
    ./redact_secrets.py --paths .specstory/history
    ./redact_secrets.py --fix --paths .cursor/plans .claude/plans
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


DEFAULT_PATHS = [
    ".specstory/history",
    ".claude/plans",
    ".cursor/plans",
    ".cursor/rules",
    ".opencode/plans",
    ".specify",
    ".codex",
]

# Repo-root gitleaks config; we pass it explicitly so custom rules apply
# even when the script is invoked from a different CWD (pre-commit etc.).
GITLEAKS_CONFIG = ".gitleaks.toml"


def read_text(path: Path) -> str:
    """Read as UTF-8 while preserving invalid bytes via surrogate escape."""
    return path.read_text(encoding="utf-8", errors="surrogateescape")


def write_text(path: Path, content: str) -> None:
    """Write UTF-8 while preserving surrogate-escaped bytes."""
    path.write_text(content, encoding="utf-8", errors="surrogateescape")


def run_gitleaks_staged() -> list[dict]:
    """Run gitleaks on staged files and return findings as JSON."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        report_path = f.name

    # Post v8.19.0 `gitleaks protect` is deprecated in favor of `gitleaks git`.
    cmd = [
        "gitleaks",
        "git",
        "--staged",
        "--report-format",
        "json",
        "--report-path",
        report_path,
        "--exit-code",
        "0",
    ]
    if Path(GITLEAKS_CONFIG).is_file():
        cmd.extend(["--config", GITLEAKS_CONFIG])
    try:
        subprocess.run(cmd, capture_output=True, text=True)
        content = read_text(Path(report_path))
        if not content.strip():
            return []
        return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
    finally:
        Path(report_path).unlink(missing_ok=True)


def run_gitleaks_workdir(target_path: str) -> list[dict]:
    """Scan every *.md under target_path and return combined findings.

    We pipe each file through `gitleaks stdin` instead of `gitleaks dir`
    because the latter silently skips hidden directories (e.g.
    `.claude/plans/`) in gitleaks >= 8.x, which is exactly where our
    agent artifacts live.
    """
    findings: list[dict] = []
    target = Path(target_path)
    if not target.exists():
        return findings
    for md_file in sorted(target.rglob("*.md")):
        if not md_file.is_file():
            continue
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
            report_path = f.name
        cmd = [
            "gitleaks",
            "stdin",
            "--report-format",
            "json",
            "--report-path",
            report_path,
            "--exit-code",
            "0",
        ]
        if Path(GITLEAKS_CONFIG).is_file():
            cmd.extend(["--config", GITLEAKS_CONFIG])
        try:
            with open(md_file, "rb") as src:
                subprocess.run(cmd, stdin=src, capture_output=True)
            content = read_text(Path(report_path))
            if content.strip():
                file_findings = json.loads(content)
                # `gitleaks stdin` reports File="" — rewrite to the real path
                # so downstream code can match against it.
                for finding in file_findings:
                    finding["File"] = str(md_file)
                findings.extend(file_findings)
        except (json.JSONDecodeError, FileNotFoundError):
            pass
        finally:
            Path(report_path).unlink(missing_ok=True)
    return findings


def redact_secret(secret: str, keep_chars: int = 3) -> str:
    """Redact secret keeping first/last N chars: sk-abc...xyz"""
    if len(secret) <= keep_chars * 2 + 3:
        return "[REDACTED]"
    return f"{secret[:keep_chars]}...{secret[-keep_chars:]}"


def redact_file(file_path: Path, findings: list[dict]) -> bool:
    """Redact secrets in a file. Returns True if modified."""
    content = read_text(file_path)
    original = content

    file_findings = [
        f for f in findings if Path(f["File"]).resolve() == file_path.resolve()
    ]

    for finding in file_findings:
        secret = finding.get("Secret", "")
        if secret and secret in content:
            content = content.replace(secret, redact_secret(secret))

    if content != original:
        write_text(file_path, content)
        return True
    return False


def filter_by_prefixes(findings: list[dict], prefixes: list[str]) -> list[dict]:
    """Filter findings whose File path contains any of the given prefixes."""
    normalized = [p.rstrip("/") + "/" for p in prefixes]
    return [
        f
        for f in findings
        if any(p in f.get("File", "") for p in normalized)
    ]


# Matches actual PEM private key blocks
_PEM_BLOCK_RE = re.compile(
    r"-----BEGIN[^-]*PRIVATE KEY[^-]*-----.*?-----END[^-]*PRIVATE KEY[^-]*-----",
    re.DOTALL,
)

# Matches the literal string the detect-private-key hook greps for
_PRIVATE_KEY_STR = "PRIVATE KEY"


def find_private_key_files(files: list[Path]) -> dict[Path, list[str]]:
    """Find files containing private key patterns. Returns {path: [match_descriptions]}."""
    results: dict[Path, list[str]] = {}
    for path in files:
        if not path.is_file() or path.suffix != ".md":
            continue
        try:
            content = read_text(path)
        except OSError:
            continue
        if _PRIVATE_KEY_STR not in content:
            continue
        matches = []
        pem_blocks = _PEM_BLOCK_RE.findall(content)
        if pem_blocks:
            matches.append(f"{len(pem_blocks)} PEM private key block(s)")
        # Count remaining mentions (outside PEM blocks)
        without_pem = _PEM_BLOCK_RE.sub("", content)
        mention_count = without_pem.count(_PRIVATE_KEY_STR)
        if mention_count:
            matches.append(f'{mention_count} "{_PRIVATE_KEY_STR}" mention(s)')
        if matches:
            results[path] = matches
    return results


def redact_private_keys(file_path: Path) -> bool:
    """Redact private key patterns in a file. Returns True if modified.

    The PEM-block placeholder must NOT contain the substring "PRIVATE
    KEY", otherwise the follow-up literal replacement below would
    corrupt it into "[REDACTED PRIV***KEY BLOCK]".
    """
    content = read_text(file_path)
    original = content
    # Replace full PEM blocks first, using a sentinel that won't be
    # clobbered by the literal-string replacement on the next line.
    content = _PEM_BLOCK_RE.sub("[REDACTED PEM PRIVKEY BLOCK]", content)
    # Replace remaining literal "PRIVATE KEY" mentions
    content = content.replace(_PRIVATE_KEY_STR, "PRIV***KEY")
    if content != original:
        write_text(file_path, content)
        return True
    return False


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Check/redact secrets in agent artifact directories "
            "(specstory history + coding agent plan dirs)."
        )
    )
    parser.add_argument(
        "--fix", action="store_true", help="Auto-redact secrets and re-stage files"
    )
    parser.add_argument(
        "--working-dir",
        action="store_true",
        help="Scan working directory instead of staged files (default: scan staged)",
    )
    parser.add_argument(
        "--paths",
        nargs="+",
        default=DEFAULT_PATHS,
        metavar="PREFIX",
        help=(
            "Path prefixes to scan. Default: "
            + " ".join(DEFAULT_PATHS)
        ),
    )
    args = parser.parse_args()

    prefixes = [p.rstrip("/") for p in args.paths]
    existing_prefixes = [p for p in prefixes if Path(p).exists()]
    missing_prefixes = [p for p in prefixes if not Path(p).exists()]

    for p in missing_prefixes:
        print(f"Skipping missing path: {p}/")

    if not existing_prefixes:
        print("No target directories found; nothing to scan.")
        return 0

    prefix_list_str = ", ".join(f"{p}/" for p in existing_prefixes)

    # --- Detect gitleaks secrets ---
    if args.working_dir:
        print(f"Scanning working directory: {prefix_list_str}")
        findings: list[dict] = []
        for p in existing_prefixes:
            findings.extend(run_gitleaks_workdir(p))
    else:
        print(f"Scanning staged files under: {prefix_list_str}")
        all_findings = run_gitleaks_staged()
        findings = filter_by_prefixes(all_findings, existing_prefixes)

    has_issues = False

    if findings:
        has_issues = True
        print(f"\nFound {len(findings)} potential secret(s):\n")

        # Group by file
        by_file: dict[str, list[dict]] = {}
        for f in findings:
            file_path = f["File"]
            by_file.setdefault(file_path, []).append(f)

        for file_path, file_findings in by_file.items():
            print(f"  {file_path}:")
            for finding in file_findings:
                rule = finding.get("RuleID", "unknown")
                secret = finding.get("Secret", "")
                line = finding.get("StartLine", "?")
                redacted = redact_secret(secret)
                print(f"    Line {line}: [{rule}] {redacted}")
            print()
    else:
        by_file = {}

    # --- Detect private key patterns ---
    if args.working_dir:
        scan_files: list[Path] = []
        for p in existing_prefixes:
            scan_files.extend(Path(p).glob("*.md"))
    else:
        result = subprocess.run(
            ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
            capture_output=True,
            text=True,
        )
        staged_md = [
            Path(f)
            for f in result.stdout.strip().splitlines()
            if f.endswith(".md")
            and any(f.startswith(p + "/") for p in existing_prefixes)
        ]
        scan_files = staged_md

    pk_files = find_private_key_files(scan_files)
    if pk_files:
        has_issues = True
        print(f"Found private key pattern(s) in {len(pk_files)} file(s):\n")
        for path, descriptions in pk_files.items():
            print(f"  {path}:")
            for desc in descriptions:
                print(f"    {desc}")
            print()

    if not has_issues:
        print(f"No secrets found in: {prefix_list_str}")
        return 0

    if args.fix:
        print("Redacting secrets...")
        modified_files: set[Path] = set()

        # Redact gitleaks findings
        for file_path in by_file:
            path = Path(file_path)
            if path.suffix == ".md" and redact_file(path, findings):
                modified_files.add(path)

        # Redact private key patterns
        for path in pk_files:
            if redact_private_keys(path):
                modified_files.add(path)

        for f in modified_files:
            print(f"  Redacted: {f}")

        # Verify private keys
        remaining_pk = find_private_key_files(
            [Path(f) for f in modified_files if Path(f).is_file()]
        )
        if remaining_pk:
            print("ERROR: Private key patterns still detected after redaction!")
            return 1

        print(f"\nSuccessfully redacted {len(modified_files)} file(s)")
        print("Review changes with: git diff")
        stage_hint = " ".join(f"{p}/" for p in existing_prefixes)
        print(f"Then stage with: git add {stage_hint}")
        return 0
    else:
        print("Run with --fix to auto-redact these secrets")
        print("Or manually edit the files to remove sensitive information")
        return 1


if __name__ == "__main__":
    sys.exit(main())
