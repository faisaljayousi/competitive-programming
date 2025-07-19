import os
import re

rows = []

# Root folders to search for problem files
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

            title = title_match.group(1).strip() if title_match else "Unknown"
            link = link_match.group(1).strip() if link_match else "#"
            tags = tags_match.group(1).strip() if tags_match else ""
            tags_formatted = (
                "`" + "`, `".join([tag.strip() for tag in tags.split(",")]) + "`"
                if tags
                else "–"
            )

            base = filename.replace(".md", "")
            py_file = f"./{dirpath}/{base}.py"
            cpp_file = f"./{dirpath}/{base}.cpp"

            rows.append(
                [
                    f"[{title}]({link})",
                    "LeetCode" if "leetcode" in dirpath else "Codeforces",
                    tags_formatted,
                    f"[💻]({py_file})" if os.path.exists(py_file) else "–",
                    f"[💻]({cpp_file})" if os.path.exists(cpp_file) else "–",
                    f"[📝]({md_path})",
                ]
            )

# Sort and write table
rows.sort()

with open("problems.md", "w", encoding="utf-8") as f:
    f.write("# 📘 Solved Problems\n\n")
    f.write("| # | Problem | Platform | Tags | Python | C++ | Notes |\n")
    f.write("|----|---------|----------|------|--------|-----|-------|\n")
    for i, row in enumerate(rows, start=1):
        f.write(f"| {i} | " + " | ".join(row) + " |\n")

print("✅ problems.md updated.")
