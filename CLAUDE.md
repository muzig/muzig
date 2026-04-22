# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Project Overview

This repository is a small generator for a bilingual GitHub profile README.

- `content/profile.json` is the source of truth.
- `templates/README.en.md.tpl` and `templates/README.zh.md.tpl` are the templates.
- `scripts/build_readme.py` generates:
  - `README.md`
  - `README-zh.md`

This is not an application service. There is no runtime server, package manager, or build pipeline beyond regenerating the README files.

## Workflow

When making changes, follow this order:

1. Read `content/profile.json`, the relevant template file, and `scripts/build_readme.py`.
2. Edit source files first.
3. Regenerate outputs with `python3 scripts/build_readme.py`.
4. Verify the generated README files reflect the intended change.

Do not manually edit `README.md` or `README-zh.md` unless the task is explicitly about validating generated output.

## Key Files

- `content/profile.json`
  - Structured profile content.
  - Keep `en` and `zh` fields aligned unless the user explicitly wants a single-language change.
- `templates/README.en.md.tpl`
  - English output template.
- `templates/README.zh.md.tpl`
  - Chinese output template.
- `scripts/build_readme.py`
  - Standard-library-only generator.
- `.claude/skills/humanizer-cn/SKILL.md`
  - Local Chinese writing skill for reducing AI-sounding phrasing.

## Chinese Writing Guidance

When the user asks to:

- reduce “AI味” or “AI 腔”
- rewrite Chinese text to sound more natural
- remove boilerplate, assistant filler, or template-like prose
- polish Chinese README, profile, or bio copy

use `.claude/skills/humanizer-cn/SKILL.md` as the project-local writing reference.

Apply it conservatively:

- preserve facts and intent
- prefer specific wording over vague praise
- remove exaggerated significance claims
- keep tone aligned with the original audience and context

## Verification

Before finishing, run:

```bash
python3 scripts/build_readme.py
git diff -- README.md README-zh.md
```

Check that:

- generated files changed only as expected
- English and Chinese content remain structurally aligned
- no `{{ key }}` placeholders remain in output

## Notes

- Prefer minimal, source-first edits.
- Keep the repository simple and dependency-free.
- If `AGENTS.md` and `CLAUDE.md` overlap, keep them consistent.
