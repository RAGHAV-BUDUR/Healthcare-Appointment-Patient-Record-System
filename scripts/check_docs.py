"""Docs consistency check run by CI on every pull request.

Fails if a Markdown file under docs/:
  * uses a requirement or test-case ID that is not in docs/requirements-registry.md
  * links an image that does not exist
  * contains AI-attribution lines
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
REGISTRY = DOCS / "requirements-registry.md"

ID_RE = re.compile(r"\bHAP-(?:F|NF|SR|SO)-\d+\b|\bTC-[A-Z]+-\d{2}\b")
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
BANNED_RE = re.compile(r"co-authored-by|generated (?:by|with) (?:ai|claude|chatgpt)", re.I)


def main() -> int:
    errors = []
    md_files = sorted(p for p in DOCS.rglob("*.md")) if DOCS.exists() else []
    known = set(ID_RE.findall(REGISTRY.read_text(encoding="utf-8"))) if REGISTRY.exists() else None

    for md in md_files:
        text = md.read_text(encoding="utf-8")
        rel = md.relative_to(ROOT)
        if known is not None and md != REGISTRY:
            for unknown in sorted(set(ID_RE.findall(text)) - known):
                errors.append(f"{rel}: ID {unknown} is not in the requirements registry")
        for target in IMG_RE.findall(text):
            if not target.startswith(("http://", "https://")) and not (md.parent / target).resolve().exists():
                errors.append(f"{rel}: image not found: {target}")
        if BANNED_RE.search(text):
            errors.append(f"{rel}: contains an AI attribution line")

    print(f"Checked {len(md_files)} Markdown files" + ("" if known is not None else " (registry not present yet, ID check skipped)"))
    for e in errors:
        print("ERROR:", e)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
