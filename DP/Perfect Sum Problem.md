# 🧩 Perfect Sum Problem (Count Subsets with Given Sum)

## 🔴 Problem
Given an array `arr` of non-negative integers and an integer `target`, count all subsets of the array whose sum is equal to the given target.

---

## ✨ Example

Input:
    arr = [5, 2, 3, 10, 6, 8]
    target = 10

Output:
    3

Explanation:
    Subsets with sum = 10:
    {5, 2, 3}
    {2, 8}
    {10}

---

# 🧠 Key Idea

👉 This is a **0/1 Knapsack (Count version)**

We convert the problem into:

    “Count number of ways to form sum = target”

---

# 🚀 Approach: 1D Dynamic Programming (Optimal)

## 💡 Idea

    dp[j] = number of ways to form sum j

---

## ⚙️ Initialization

    dp[0] = 1

👉 There is exactly **1 way to make sum 0**:
    (choose no elements)

---

## 🔁 Transition

For each number `num`:

    dp[j] += dp[j - num]

👉 Meaning:
    Ways to make j =
        existing ways +
        ways to make (j - num) and then include num

---

## 🚨 Important Rule

Loop **backwards**:

    for j from target → num

👉 This ensures:
    Each element is used only once

---

# 💻 Code

    class Solution:
        def perfectSum(self, arr, target):
            # dp[j] = number of ways to make sum j
            dp = [0] * (target + 1)

            # Base case
            dp[0] = 1

            for num in arr:
                # Traverse backwards
                for j in range(target, num - 1, -1):
                    dp[j] += dp[j - num]

            return dp[target]

---

# 🧪 Dry Run (Quick Intuition)

arr = [1, 2, 3], target = 4

Step-by-step sums:

    Start → {0}
    After 1 → {0,1}
    After 2 → {0,1,2,3}
    After 3 → {0,1,2,3,4}

👉 dp[4] = 1 → subset: [1,3]

---

# ⏱️ Complexity

Time:
    O(n * target)

Space:
    O(target)

---

# ⚠️ Edge Case (Important)

If array contains `0`:

👉 Each zero doubles the number of subsets

Example:
    arr = [0,0,1], target = 1
    Output = 4

---

# 🎯 Summary

- Use DP to track number of ways
- Build sums step by step
- Use backward loop to avoid reuse
- Final answer = dp[target]

---

# 🔥 Pattern

👉 0/1 Knapsack (Count variant)

---

# 💡 One-line Insight

👉 Each number expands the number of ways to build sums
