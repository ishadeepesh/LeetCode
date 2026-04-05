# 🧩 Minimum Sum Partition

## 🔴 Problem
Given an array `arr[]` containing non-negative integers, divide it into two subsets such that the **absolute difference between their sums is minimum**.

Return the minimum difference.

---

## ✨ Example

Input:
    arr = [1, 6, 11, 5]

Output:
    1

Explanation:
    Subset1 = {1, 5, 6} → sum = 12  
    Subset2 = {11} → sum = 11  

    Minimum difference = |12 - 11| = 1

---

# 🧠 Key Idea

👉 Let total sum = `total`

We want:
    min |S1 - S2|

Since:
    S1 + S2 = total

👉 We can rewrite:
    difference = total - 2 * S1

---

## 🎯 Goal

👉 Find subset sum `S1` as close as possible to:
    
    total // 2

---

# 🚀 Approach: 1D DP (Subset Sum)

## 💡 Idea

    dp[j] = True if we can form sum j

---

## ⚙️ Initialization

    dp[0] = True

👉 Sum 0 is always possible (empty subset)

---

## 🔁 Transition

For each number `num`:

    dp[j] = dp[j] OR dp[j - num]

👉 Meaning:
    We can form sum `j` if:
        - it was already possible OR
        - we can form (j - num) and include num

---

## 🚨 Important Rule

Loop **backwards**:

    for j from total → num

👉 Prevents reusing same element

---

# 💻 Code

    class Solution:
        def minDifference(self, nums):
            total = sum(nums)
            target = total // 2

            dp = [False] * (total + 1)
            dp[0] = True

            for num in nums:
                for j in range(total, num - 1, -1):
                    dp[j] = dp[j] or dp[j - num]

            mn = float('inf')

            for i in range(target + 1):
                if dp[i]:
                    mn = min(mn, total - 2 * i)

            return mn

---

# 🧪 Dry Run (Quick Intuition)

arr = [1, 6, 11, 5]

Possible subset sums:
    {0,1,5,6,7,11,12,...}

Closest to total/2 = 11:

👉 Best choice:
    S1 = 11

Difference:
    total - 2 * 11 = 23 - 22 = 1

---

# ⏱️ Complexity

Time:
    O(n * total)

Space:
    O(total)

---

# ⚠️ Note

👉 We use full `total` range in DP  
👉 But only check till `total // 2`

---

# 🎯 Summary

- Convert to subset sum problem
- Try all possible sums
- Pick closest to half
- Compute difference

---

# 🔥 Pattern

👉 0/1 Knapsack (Boolean DP)

---

# 💡 One-line Insight

👉 “Split array into two parts with sums as equal as possible”
