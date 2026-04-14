#!/usr/bin/env python3
"""Repository validation for Claude packaging and Codex-facing skill docs."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins"
README = ROOT / "README.md"
AGENTS = ROOT / "AGENTS.md"
CONTRIBUTING = ROOT / "CONTRIBUTING.md"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def extract_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        raise ValueError("missing YAML frontmatter")

    raw = match.group(1).splitlines()
    body = match.group(2)
    data: dict[str, str] = {}
    i = 0
    while i < len(raw):
        line = raw[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith((" ", "\t")):
            i += 1
            continue

        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"invalid frontmatter line: {line!r}")

        key = key.strip()
        value = value.lstrip()

        if value in {">", ">-", "|", "|-"}:
            block: list[str] = []
            i += 1
            while i < len(raw):
                next_line = raw[i]
                if next_line.startswith("  "):
                    block.append(next_line[2:])
                    i += 1
                    continue
                if next_line == "":
                    block.append("")
                    i += 1
                    continue
                break
            data[key] = "\n".join(block).strip()
            continue

        data[key] = value.strip().strip('"').strip("'")
        i += 1

    return data, body


def load_marketplace() -> list[dict[str, str]]:
    with MARKETPLACE.open(encoding="utf-8") as handle:
        payload = json.load(handle)
    return payload["plugins"]


def canonical_skills() -> list[dict[str, str | Path]]:
    skills: list[dict[str, str | Path]] = []
    for path in sorted(PLUGIN_ROOT.glob("*/skills/*/SKILL.md")):
        plugin = path.parts[-4]
        skill_dir = path.parent
        frontmatter, _body = extract_frontmatter(path)
        skills.append(
            {
                "plugin": plugin,
                "path": path,
                "dir": skill_dir,
                "name": frontmatter.get("name", ""),
                "description": frontmatter.get("description", ""),
            }
        )
    return skills


def validate_marketplace(errors: list[str]) -> None:
    for plugin in load_marketplace():
        source = ROOT / plugin["source"]
        if not source.exists():
            errors.append(f"Marketplace source does not exist: {plugin['source']}")
            continue

        manifest = source / ".claude-plugin" / "plugin.json"
        if not manifest.exists():
            errors.append(f"Missing plugin manifest: {manifest.relative_to(ROOT)}")
            continue

        with manifest.open(encoding="utf-8") as handle:
            plugin_json = json.load(handle)

        if plugin_json.get("name") != plugin["name"]:
            errors.append(
                "Plugin name mismatch: "
                f"marketplace={plugin['name']} plugin.json={plugin_json.get('name')}"
            )


def validate_skills(errors: list[str]) -> list[dict[str, str | Path]]:
    skills = canonical_skills()
    if not skills:
        errors.append("No canonical skills found under plugins/*/skills/*")
        return skills

    for skill in skills:
        path = skill["path"]
        name = str(skill["name"])
        description = str(skill["description"])
        directory_name = Path(skill["dir"]).name

        if not NAME_RE.match(name):
            errors.append(f"Invalid skill name {name!r} in {Path(path).relative_to(ROOT)}")
        if directory_name != name:
            errors.append(
                f"Skill directory/name mismatch: {directory_name!r} != {name!r} in {Path(path).relative_to(ROOT)}"
            )
        if not description:
            errors.append(f"Missing description in {Path(path).relative_to(ROOT)}")

    return skills


def validate_docs(
    skills: list[dict[str, str | Path]],
    marketplace_plugins: list[dict[str, str]],
    errors: list[str],
) -> None:
    for doc in (AGENTS, CONTRIBUTING, README):
        if not doc.exists():
            errors.append(f"Missing required documentation file: {doc.relative_to(ROOT)}")

    if errors:
        return

    readme_text = README.read_text(encoding="utf-8")
    agents_text = AGENTS.read_text(encoding="utf-8")

    required_readme_markers = [
        "## Codex and Skills",
        "npx skills add",
        "personal/private",
        "plugins/<plugin>/skills/<skill>",
    ]
    for marker in required_readme_markers:
        if marker not in readme_text:
            errors.append(f"README is missing required marker: {marker!r}")

    for skill in skills:
        if skill["plugin"] == "p-assist":
            continue
        needle = f"`{skill['name']}`"
        if needle not in readme_text:
            errors.append(f"README does not mention public skill {skill['name']}")

    for plugin in marketplace_plugins:
        plugin_name = plugin["name"]
        if plugin_name not in readme_text:
            errors.append(f"README does not mention plugin {plugin_name}")

    for marker in ("make validate", "plugins/*/skills/*", "p-assist"):
        if marker not in agents_text:
            errors.append(f"AGENTS.md is missing required marker: {marker!r}")


def main() -> int:
    errors: list[str] = []

    marketplace_plugins = load_marketplace()
    validate_marketplace(errors)
    skills = validate_skills(errors)
    validate_docs(skills, marketplace_plugins, errors)

    if errors:
        print("Repository validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Repository validation passed: "
        f"{len(skills)} canonical skills checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
