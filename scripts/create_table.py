import os
import re
import json
from collections import Counter

rows = []
platform_counter = Counter()
difficulty_counter = Counter()
tag_counter = Counter()
language_counter = Counter()
rating_counter = Counter()

problem_dirs = ["./leetcode", "./codeforces"]

for dirpath in problem_dirs:
    for filename in os.listdir(dirpath):
        if filename.endswith(".md") and filename != "problem_template.md":
            md_path = os.path.join(dirpath, filename)

            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Extract metadata
            title_match = re.search(r"# 🧩 Problem: (.+)", content)
            link_match = re.search(r"\[Problem Link\]\((.*?)\)", content)
            tags_match = re.search(r"\*\*Tags\*\*: (.+)", content)
            difficulty_match = re.search(r"\*\*Difficulty\*\*: (.+)", content)
            rating_match = re.search(r"\*\*Rating\*\*: (\d+)", content)

            title = title_match.group(1).strip() if title_match else "Unknown"
            link = link_match.group(1).strip() if link_match else "#"
            tags = tags_match.group(1).strip() if tags_match else ""
            difficulty = (
                re.sub(r"[\\\s]+$", "", difficulty_match.group(1)).capitalize()
                if difficulty_match
                else "Unknown"
            )
            rating = int(rating_match.group(1)) if rating_match else None

            tags_formatted = (
                "`" + "`, `".join([tag.strip() for tag in tags.split(",")]) + "`"
                if tags
                else "–"
            )

            base = filename.replace(".md", "")
            py_file = f"{dirpath}/{base}.py"
            cpp_file = f"{dirpath}/{base}.cpp"
            platform = "LeetCode" if "leetcode" in dirpath else "Codeforces"

            # Update counters
            platform_counter[platform] += 1
            difficulty_counter[difficulty] += 1
            if rating:
                rating_counter[rating] += 1
            for tag in tags.split(","):
                tag = tag.strip()
                if tag:
                    tag_counter[tag] += 1
            if os.path.exists(py_file):
                language_counter["Python"] += 1
            if os.path.exists(cpp_file):
                language_counter["C++"] += 1

            rows.append(
                [
                    f"[{title}]({link})",
                    platform,
                    difficulty,
                    tags_formatted,
                    f"[💻]({py_file})" if os.path.exists(py_file) else "–",
                    f"[💻]({cpp_file})" if os.path.exists(cpp_file) else "–",
                    f"[📝]({md_path})",
                ]
            )

# Sort alphabetically by title
rows.sort()

# Write to Markdown file
with open("problems.md", "w", encoding="utf-8") as f:
    f.write("# 📘 Solved Problems\n\n")
    f.write("| # | Problem | Platform | Difficulty | Tags | Python | C++ | Notes |\n")
    f.write("|----|---------|----------|------------|------|--------|-----|-------|\n")
    for i, row in enumerate(rows, start=1):
        f.write(f"| {i} | " + " | ".join(row) + " |\n")

    # Add stats at end
    f.write("\n---\n\n")
    f.write("## 📊 Summary Statistics\n\n")
    f.write(f"**Total problems solved**: {len(rows)}\n\n")

    f.write("### By Platform:\n")
    for platform, count in platform_counter.items():
        f.write(f"- {platform}: {count}\n")

    f.write("\n### By Difficulty:\n")
    for difficulty, count in difficulty_counter.items():
        f.write(f"- {difficulty}: {count}\n")

    f.write("\n### By Language:\n")
    for lang, count in language_counter.items():
        f.write(f"- {lang}: {count}\n")

    f.write("\n### By Tag:\n")
    for tag, count in tag_counter.most_common():
        f.write(f"- `{tag}`: {count}\n")

# Save stats as JSON
stats = {
    "platform": dict(platform_counter),
    "difficulty": dict(difficulty_counter),
    "language": dict(language_counter),
    "tags": dict(tag_counter),
    "ratings": dict(rating_counter),
    "total": len(rows),
}

# with open("progress.json", "w", encoding="utf-8") as jf:
#     json.dump(stats, jf, indent=2)
