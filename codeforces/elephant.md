# 🧩 Problem: Elephant

**Platform**: Codeforces \
**Link**: [Problem Link](https://codeforces.com/problemset/problem/617/A) \
**Difficulty**: 800 \
**Tags**: `greedy`, `math`

---

## 📄 Problem Statement

An elephant decided to visit his friend. It turned out that the elephant's house is located at point 0 and his friend's house is located at point x(x > 0) of the coordinate line. In one step the elephant can move 1, 2, 3, 4 or 5 positions forward. Determine, what is the minimum number of steps he need to make in order to get to his friend's house.

> Input: the first line of the input contains an integer x (1 ≤ x ≤ 1 000 000) — The coordinate of the friend's house.

> Output: print the minimum number of steps that elephant needs to make to get from point 0 to point x.

---

## 🧠 Approach

We use a greedy strategy: always take the largest possible step (5, then 4, ..., down to 1) that fits into the remaining distance. For each step size, we compute how many full steps we can take, subtract the total distance covered, and accumulate the number of steps taken. This guarantees the minimum number of steps since we prioritise the largest strides first.
