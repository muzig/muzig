# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

This repository contains a bilingual (Chinese/English) GitHub profile README.

- `README.md` — Chinese version (primary)
- `README-zh.md` — English version

Both files are maintained directly. There is no build system, template engine, or package manager.

## Workflow

When making changes:

1. Edit `README.md` and `README-zh.md` directly.
2. Keep both versions structurally aligned (same sections, same order).
3. Verify with `git diff` before committing.

## Key Files

- `.claude/skills/humanizer-cn/SKILL.md`
  - Local Chinese writing skill for reducing AI-sounding phrasing.

## Chinese Writing Guidance

When the user asks to:

- reduce "AI味" or "AI 腔"
- rewrite Chinese text to sound more natural
- remove boilerplate, assistant filler, or template-like prose
- polish Chinese README, profile, or bio copy

use `.claude/skills/humanizer-cn/SKILL.md` as the project-local writing reference.

Apply it conservatively:

- preserve facts and intent
- prefer specific wording over vague praise
- remove exaggerated significance claims
- keep tone aligned with the original audience and context

## Notes

- Keep the repository simple.
- If `AGENTS.md` and `CLAUDE.md` overlap, keep them consistent.
