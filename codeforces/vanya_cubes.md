# 🧩 Problem: Vanya and Cubes

**Platform**: Codeforces \
**Link**: [Problem Link](https://codeforces.com/problemset/problem/492/A) \
**Difficulty**: 800 \
**Tags**: `implementation`

---

## 📄 Problem Statement

Vanya got n cubes. He decided to build a pyramid from them. Vanya wants to build the pyramid as follows: the top level of the pyramid must consist of 1 cube, the second level must consist of 1 + 2 = 3 cubes, the third level must have 1 + 2 + 3 = 6 cubes, and so on. Thus, the i-th level of the pyramid must have 1 + 2 + ... + (i - 1) + i cubes.

Vanya wants to know what is the maximum height of the pyramid that he can make using the given cubes.

> Input: the first line contains integer n (1 ≤ n ≤ 104) — the number of cubes given to Vanya.

> Output: print the maximum possible height of the pyramid in the single line.

## 🧠 Approach

We build the pyramid level by level. Each level `i` needs `i * (i + 1) / 2` cubes. At each step, we subtract the cubes needed from the total `n`, and stop when we can’t afford the next level.
