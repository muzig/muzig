# AGENTS.md

## Project Overview

This repository is a small generator for a bilingual GitHub profile README.

- `content/profile.json` is the source of truth.
- `templates/README.en.md.tpl` and `templates/README.zh.md.tpl` are the presentation templates.
- `scripts/build_readme.py` generates:
  - `README.md`
  - `README-zh.md`

This is not an application service. There is no runtime server, package manager, or build pipeline beyond regenerating the README files.

## Working Agreement For AI Agents

When making changes, follow this order:

1. Read `content/profile.json`, the relevant template files, and `scripts/build_readme.py`.
2. Update source files first.
3. Regenerate `README.md` and `README-zh.md` with `python3 scripts/build_readme.py`.
4. Verify that generated files reflect the source change.

Do not manually edit generated README files unless the task is specifically about generated output verification. Source changes should normally happen in `content/` or `templates/`.

## File Roles

### Source Files

- `content/profile.json`
  - Stores structured profile data.
  - Keep `en` and `zh` entries aligned when editing localized fields.
- `templates/README.en.md.tpl`
  - English README template.
- `templates/README.zh.md.tpl`
  - Chinese README template.
- `scripts/build_readme.py`
  - Pure Python generator using only the standard library.

### Generated Files

- `README.md`
- `README-zh.md`

Both generated files include a header comment stating they should not be edited directly.

### CI Validation

- `.github/workflows/validate-readme.yml`
  - Regenerates README files in CI.
  - Fails if committed generated files are out of date.

### AI Collaboration Files

- `CLAUDE.md`
  - Claude Code project instructions.
  - Mirrors the repository workflow in a Claude-native entry file.
- `.claude/skills/humanizer-cn/SKILL.md`
  - Local writing skill for reducing AI-sounding Chinese prose.
  - Claude-style project skill location.
  - Codex should treat this file as a reusable project instruction source when the task is about rewriting Chinese text to sound less formulaic or less assistant-like.
- `.codex/skills/humanizer-cn/SKILL.md`
  - Codex-local mirror of the same writing skill.
  - Keep it aligned with the Claude-side skill when updating the humanization rules.

## Change Guidance

### Common Tasks

- Update profile text, links, project items, focus items, or contact info:
  - Edit `content/profile.json`
  - Regenerate the README files

- Change wording, layout, or section formatting:
  - Edit the relevant template file
  - Regenerate the README files

- Change rendering logic:
  - Edit `scripts/build_readme.py`
  - Regenerate the README files

### Localization Rules

- For fields with `en` and `zh`, update both unless the task explicitly requests a single-language change.
- Keep section ordering consistent across languages.
- Preserve existing markdown style unless the task requires a format change.

### Chinese Writing Humanization

When the task involves Chinese writing such as:

- reducing “AI味” or “AI 腔”
- making text sound more natural or more like a human wrote it
- removing boilerplate, marketing tone, or assistant-style filler
- rewriting profile copy, bio text, README prose, or social copy in Chinese

use `.claude/skills/humanizer-cn/SKILL.md` as the primary project reference.
If the task is being handled through Codex-local skill loading, keep `.codex/skills/humanizer-cn/SKILL.md` aligned with it.

Apply it conservatively:

- preserve facts and intent
- prefer specific wording over vague praise
- remove exaggerated significance claims
- remove assistant-style closings and polite filler
- keep the final tone aligned with the original audience and context

## Verification Checklist

Before finishing a task, run:

```bash
python3 scripts/build_readme.py
git diff -- README.md README-zh.md
```

Check that:

- generated files changed only as expected
- English and Chinese content remain structurally aligned
- no placeholder tokens such as `{{ key }}` remain in output

## Constraints

- Prefer minimal, source-first edits.
- Avoid introducing new tooling unless clearly necessary.
- Keep the repository simple and dependency-free when possible.
- If a requested change conflicts with the generator workflow, update the source files and generator rather than patching generated output by hand.
