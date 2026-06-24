# AGENTS.md

## Project Overview

This repository contains a bilingual (Chinese/English) GitHub profile README.

- `README.md` — Chinese version (primary)
- `README-zh.md` — English version

Both files are maintained directly. There is no build system, template engine, or package manager.

## Working Agreement For AI Agents

When making changes:

1. Edit `README.md` and `README-zh.md` directly.
2. Keep both versions structurally aligned (same sections, same order).
3. Verify with `git diff` before committing.

## File Roles

### AI Collaboration Files

- `CLAUDE.md`
  - Claude Code project instructions.
- `.claude/skills/humanizer-cn/SKILL.md`
  - Local writing skill for reducing AI-sounding Chinese prose.

## Change Guidance

### Common Tasks

- Update profile text, links, projects, or contact info:
  - Edit both `README.md` and `README-zh.md`

- Change wording, layout, or section formatting:
  - Edit the relevant README file directly

### Localization Rules

- For sections with Chinese and English, update both unless the task explicitly requests a single-language change.
- Keep section ordering consistent across languages.
- Preserve existing markdown style unless the task requires a format change.

### Chinese Writing Humanization

When the task involves Chinese writing such as:

- reducing "AI味" or "AI 腔"
- making text sound more natural or more like a human wrote it
- removing boilerplate, marketing tone, or assistant-style filler

use `.claude/skills/humanizer-cn/SKILL.md` as the primary project reference.

Apply it conservatively:

- preserve facts and intent
- prefer specific wording over vague praise
- remove exaggerated significance claims
- keep the final tone aligned with the original audience and context

## Constraints

- Keep the repository simple.
- If `AGENTS.md` and `CLAUDE.md` overlap, keep them consistent.
