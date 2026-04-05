# 🧩 Partitions with Given Difference

## 🔴 Problem
Given an array `arr[]` and an integer `diff`, count the number of ways to partition the array into two subsets such that the difference between their sums is equal to `diff`.

---

## ✨ Example

Input:
    arr = [5, 2, 6, 4]
    diff = 3

Output:
    1

Explanation:
    Partition:
    S1 = [6, 4] → sum = 10  
    S2 = [5, 2] → sum = 7  

    Difference = 10 - 7 = 3

---

# 🧠 Key Idea

Let:
    S1 - S2 = diff  
    S1 + S2 = total  

👉 Adding both:

    2 * S1 = diff + total  
    S1 = (diff + total) / 2  

---

## 🎯 Goal

👉 Count number of subsets with sum:

    target = (diff + total) / 2

---

# 🚨 Important Conditions

1. `(diff + total)` must be EVEN  
   Otherwise → no valid partition

2. `target` must be valid:
    
    0 ≤ target ≤ total

---

# 🚀 Approach: 1D DP (Count Subsets)

## 💡 Idea

    dp[j] = number of ways to form sum j

---

## ⚙️ Initialization

    dp[0] = 1

👉 One way to make sum 0 (empty subset)

---

## 🔁 Transition

For each number `num`:

    dp[j] += dp[j - num]

👉 Meaning:
    Ways to make j =
        existing ways +
        ways to make (j - num) and include num

---

## 🚨 Important Rule

Loop **backwards**:

    for j from target → num

👉 Ensures each element is used only once

---

# 💻 Code

    class Solution:
        def perfectSum(self, arr, target):
            dp = [0] * (target + 1)
            dp[0] = 1

            for num in arr:
                for j in range(target, num - 1, -1):
                    dp[j] += dp[j - num]

            return dp[target]

        def countPartitions(self, arr, diff):
            total = sum(arr)

            # Condition 1: must be even
            if (diff + total) % 2 != 0:
                return 0

            target = (diff + total) // 2

            # Condition 2: valid range
            if target < 0 or target > total:
                return 0

            return self.perfectSum(arr, target)

---

# 🧪 Dry Run (Quick Intuition)

arr = [1, 2, 3], diff = 1

total = 6

target = (1 + 6) / 2 = 3.5 ❌

👉 Not integer → answer = 0

---

# ⏱️ Complexity

Time:
    O(n * target)

Space:
    O(target)

---

# 🎯 Summary

- Convert partition problem → subset sum
- Use DP to count number of subsets
- Apply parity check before solving

---

# 🔥 Pattern

👉 0/1 Knapsack (Count variant)

---

# 💡 One-line Insight

👉 “Partition with given difference = count subsets with sum (diff + total)/2”
