#!/usr/bin/env python3
"""Validate the skill's metadata, contracts, references, and Python syntax."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = ROOT / "SKILL.md"
REQUIRED_COMMENTARY_SECTIONS = (
    "## Alternative Angles (commentary only)",
    "## Rights and Platform Notes (commentary only)",
    "## Pre-Publish Checklist (commentary only)",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def frontmatter_value(content: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", content)
    return match.group(1) if match else None


def validate_frontmatter(content: str, errors: list[str]) -> None:
    if not content.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter.")
        return

    end = content.find("\n---\n", 4)
    if end == -1:
        errors.append("SKILL.md frontmatter is not closed.")
        return

    frontmatter = content[:end]
    name = frontmatter_value(frontmatter, "name")
    description = frontmatter_value(frontmatter, "description")

    if name != ROOT.name:
        errors.append(f"Skill name '{name}' must match folder '{ROOT.name}'.")
    if not description:
        errors.append("SKILL.md description is missing.")
    elif len(description) > 1024:
        errors.append("SKILL.md description exceeds 1024 characters.")


def validate_markdown(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        if read_text(path).count("```") % 2:
            errors.append(f"Unbalanced Markdown fence: {path.relative_to(ROOT)}")


def validate_references(skill_content: str, errors: list[str]) -> None:
    pattern = re.compile(r"`((?:references|assets|scripts)/[^`\s]+)`")
    for relative in sorted(set(pattern.findall(skill_content))):
        if not (ROOT / relative).is_file():
            errors.append(f"Missing referenced file: {relative}")


def validate_contracts(skill_content: str, errors: list[str]) -> None:
    for heading in REQUIRED_COMMENTARY_SECTIONS:
        if heading not in skill_content:
            errors.append(f"Missing commentary output contract: {heading}")

    commentary = read_text(ROOT / "references" / "commentary-scripts.md")
    if "80-130 words" in commentary:
        errors.append("English 20-second commentary still uses the old word range.")


def validate_python(errors: list[str]) -> None:
    for path in ROOT.rglob("*.py"):
        if ".git" in path.parts:
            continue
        try:
            compile(read_text(path), str(path), "exec")
        except SyntaxError as exc:
            errors.append(f"Python syntax error in {path.relative_to(ROOT)}: {exc}")


def main() -> int:
    errors: list[str] = []
    skill_content = read_text(SKILL_MD)

    validate_frontmatter(skill_content, errors)
    validate_markdown(errors)
    validate_references(skill_content, errors)
    validate_contracts(skill_content, errors)
    validate_python(errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
