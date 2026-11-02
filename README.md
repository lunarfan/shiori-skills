# 栞 Shiori skills

Site definitions ("skills") for the 栞 Shiori novel-update tracker. The app
itself contains no site-specific code; it reads sites through skills
imported from this repo (from a URL, a file, or pasted JSON).

| File | Site | Format |
|---|---|---|
| `linovelib-tw.json` | 嗶哩輕小說（繁） | 1 |
| `sfacg.json` | SF轻小说 (mobile site) | 2 |

`ref.md` holds reference URLs used when writing the linovelib skill.

## Catalog

The app lists the skills in `index.json` (Settings → Skill → 匯入 Skill) and
offers updates when a skill's `version` is higher than the installed one.
After adding or changing a skill, bump its `version` and run:

```
python3 make_index.py
```

The skill format is documented in the app repo: `docs/skill-format.md`.
