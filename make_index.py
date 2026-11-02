#!/usr/bin/env python3
"""Regenerate index.json, the catalog the 栞 Shiori app reads.

Run after adding a skill or changing one (bump its "version" so installed
copies are offered the update):

    python3 make_index.py
"""
import json
from pathlib import Path

here = Path(__file__).parent
skills = []
for f in sorted(here.glob("*.json")):
    if f.name == "index.json":
        continue
    s = json.loads(f.read_text(encoding="utf-8"))
    if "novelcheck_skill" not in s:
        continue
    skills.append({
        "id": s["id"],
        "name": s["name"],
        "version": s.get("version", ""),
        "description": s.get("description", ""),
        "hosts": s.get("hosts", []),
        "format": s["novelcheck_skill"],
        "file": f.name,
    })

index = {"shiori_skills_index": 1, "skills": skills}
(here / "index.json").write_text(
    json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"index.json: {len(skills)} skills")
