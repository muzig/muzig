# AGENTS.md

## Project Overview

This repository contains a bilingual (Chinese/English) GitHub profile README.

- `README.md` — English version (GitHub default)
- `README-zh.md` — Chinese version

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

## Cursor Cloud specific instructions

There is no package install, build, test suite, or service to start. Cloud Agents use the default image. The environment `install` command only checks that `README.md`, `README-zh.md`, `AGENTS.md`, and `CLAUDE.md` are present.

`README.md` is the English profile. `README-zh.md` is the Chinese profile. After an edit, keep the same sections in the same order, then review `git diff`.
