import json
import os

# Load solved count from progress.json
with open("progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

total_solved = progress.get("total", 0)

# Count language usage
lang_counter = {"Python": 0, "C++": 0}
for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            lang_counter["Python"] += 1
        elif file.endswith((".cpp", ".h")):
            lang_counter["C++"] += 1

dominant_lang = max(lang_counter, key=lang_counter.get, default="Unknown")

# GitHub repo details
github_user = "faisaljayousi"
repo_name = "competitive-programming"

# Generate updated badge block
badge_block = f"""\
![Problems Solved](https://img.shields.io/badge/Solved-{total_solved}-blue)
![Last Commit](https://img.shields.io/github/last-commit/{github_user}/{repo_name})
![Language](https://img.shields.io/badge/Top_Language-{dominant_lang}-informational)
"""


# Update top of README.md
with open("README.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Insert or replace badge block
start = 0
while start < len(lines) and lines[start].strip().startswith("!["):
    start += 1

# Replace existing badge block or insert new one
new_lines = [badge_block + "\n"] + lines[start:]

with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("✅ README.md badges updated.")
