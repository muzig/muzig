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


def render_about(text: str) -> str:
    return text


def render_skills(items: list[dict], lang: str) -> str:
    lines = []
    for item in items:
        lines.append(f"### {item['emoji']} {item['title'][lang]}\n")
        for bullet in item["items"][lang]:
            lines.append(f"- {bullet}\n")
        if "note" in item and item["note"]:
            lines.append(f"\n{item['note'][lang]}\n")
    return "".join(lines).rstrip()


def render_current(items: list[dict], lang: str) -> str:
    lines = []
    for item in items:
        lines.append(f"### {item['emoji']} {item['title'][lang]}\n")
        for bullet in item["items"][lang]:
            lines.append(f"- {bullet}\n")
        if "goal" in item and item["goal"]:
            lines.append(f"\n{item['goal'][lang]}\n")
    return "".join(lines).rstrip()


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

    titles = profile["section_titles"]

    return render_template(
        template,
        {
            "title": profile["title"][lang],
            "headline": " | ".join(profile["headline"][lang]),
            "badges": render_badges(profile["badge_groups"]),
            "about_title": titles["about"][lang],
            "about": render_about(profile["about"][lang]),
            "skills_title": titles["skills"][lang],
            "skills": render_skills(profile["skills"], lang),
            "current_title": titles["current"][lang],
            "current": render_current(profile["current"], lang),
            "blog_title": titles["blog"][lang],
            "blog_url": profile["blog"]["url"],
            "blog_desc": profile["blog"]["desc"][lang],
            "connect_title": titles["connect"][lang],
            "connect": render_connect(profile["connect"], lang),
            "tagline_title": titles["tagline"][lang],
            "tagline": profile["tagline"][lang],
            "language_title": titles.get("language", {"en": "Language", "zh": "语言"})[lang],
        },
    )


def main() -> None:
    profile = load_profile()
    for lang, output_path in OUTPUTS.items():
        output_path.write_text(build_readme(profile, lang), encoding="utf-8")


if __name__ == "__main__":
    main()
