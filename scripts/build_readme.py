#!/usr/bin/env python3

import json
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent.parent
CONTENT_PATH = ROOT / "content" / "profile.json"
TEMPLATE_DIR = ROOT / "templates"
OUTPUTS = {
    "en": ROOT / "README.md",
    "zh": ROOT / "README-zh.md",
}


def load_profile() -> dict:
    with CONTENT_PATH.open(encoding="utf-8") as file:
        return json.load(file)


def build_badge(badge: dict) -> str:
    label = badge["label"]
    encoded_label = quote(badge["label"], safe="")
    color = badge["color"]
    logo = quote(badge["logo"], safe="")
    logo_color = quote(badge.get("logo_color", "white"), safe="")
    return (
        f"![{label}]"
        f"(https://img.shields.io/badge/{encoded_label}-{color}"
        f"?style=flat&logo={logo}&logoColor={logo_color})"
    )


def render_badges(groups: list[list[dict]]) -> str:
    return " &nbsp;·&nbsp; ".join(
        " ".join(build_badge(badge) for badge in group) for group in groups
    )


def render_projects(items: list[dict], lang: str) -> str:
    lines = []
    for item in items:
        name = item.get("name_localized", {}).get(lang, item["name"])
        lines.append(
            "- {emoji} **{name}** – [{url_label}]({url}) – {desc}".format(
                emoji=item["emoji"],
                name=name,
                url_label=item["url"].removeprefix("https://"),
                url=item["url"],
                desc=item["desc"][lang],
            )
        )
    return "\n".join(lines)


def render_focus(items: list[dict], lang: str) -> str:
    lines = []
    for item in items:
        lines.append(
            "- **{title}** – {desc}".format(
                title=item["title"][lang],
                desc=item["desc"][lang],
            )
        )
    return "\n".join(lines)


def render_connect(items: list[dict], lang: str) -> str:
    parts = []
    for item in items:
        parts.append("[{text}]({url})".format(text=item["text"][lang], url=item["url"]))
    return " · ".join(parts)


def render_template(template: str, replacements: dict[str, str]) -> str:
    rendered = template
    for key, value in replacements.items():
        rendered = rendered.replace("{{ " + key + " }}", value)
    return rendered.rstrip() + "\n"


def build_readme(profile: dict, lang: str) -> str:
    template_path = TEMPLATE_DIR / ("README.en.md.tpl" if lang == "en" else "README.zh.md.tpl")
    template = template_path.read_text(encoding="utf-8")
    return render_template(
        template,
        {
            "title": profile["title"][lang],
            "headline": " | ".join(profile["headline"][lang]),
            "badges": render_badges(profile["badge_groups"]),
            "summary": profile["summary"][lang],
            "projects_title": profile["section_titles"]["projects"][lang],
            "projects": render_projects(profile["projects"], lang),
            "focus_title": profile["section_titles"]["focus"][lang],
            "focus": render_focus(profile["focus"], lang),
            "connect_title": profile["section_titles"]["connect"][lang],
            "connect": render_connect(profile["connect"], lang),
            "language_title": profile["section_titles"]["language"][lang],
        },
    )


def main() -> None:
    profile = load_profile()
    for lang, output_path in OUTPUTS.items():
        output_path.write_text(build_readme(profile, lang), encoding="utf-8")


if __name__ == "__main__":
    main()
