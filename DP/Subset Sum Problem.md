# 🧩 Subset Sum Problem

## 🔴 Problem
Given an array of positive integers arr[] and a value sum, determine if there exists a subset of the array with sum equal to the given sum.

---

## ✨ Example

Input:
    arr = [3, 34, 4, 12, 5, 2]
    sum = 9

Output:
    true

Explanation:
    Subset [4, 3, 2] gives sum = 9

---

# 🚀 Approach 1: Recursion (Brute Force)

## 💡 Idea
For each element:
    - Include it
    - Exclude it

## 🔁 Recurrence
    f(n, sum) =
        f(n-1, sum - arr[n-1])
        OR
        f(n-1, sum)

## 🛑 Base Cases
    if sum == 0 → True
    if n == 0 → False

## 💻 Code

    class Solution:
        def knapsack(self, arr, sum, n):
            if sum == 0:
                return True
            if n == 0:
                return False

            if arr[n - 1] <= sum:
                return (self.knapsack(arr, sum - arr[n - 1], n - 1) or
                        self.knapsack(arr, sum, n - 1))
            else:
                return self.knapsack(arr, sum, n - 1)

        def isSubsetSum(self, arr, sum):
            return self.knapsack(arr, sum, len(arr))

## ⏱️ Complexity
    Time: O(2^n)
    Space: O(n)

---

# 🚀 Approach 2: Memoization (Top-Down DP)

## 💡 Idea
Store results of subproblems to avoid recomputation

## 💻 Code

    class Solution:
        def knapsack(self, arr, sum, n, memo):
            if sum == 0:
                return True
            if n == 0:
                return False

            if memo[n][sum] != -1:
                return memo[n][sum]

            if arr[n - 1] <= sum:
                memo[n][sum] = (
                    self.knapsack(arr, sum - arr[n - 1], n - 1, memo) or
                    self.knapsack(arr, sum, n - 1, memo)
                )
            else:
                memo[n][sum] = self.knapsack(arr, sum, n - 1, memo)

            return memo[n][sum]

        def isSubsetSum(self, arr, sum):
            n = len(arr)
            memo = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]
            return self.knapsack(arr, sum, n, memo)

## ⏱️ Complexity
    Time: O(n * sum)
    Space: O(n * sum)

---

# 🚀 Approach 3: Bottom-Up DP (Tabulation)

## 💡 Idea
    t[i][j] = True if we can form sum j using first i elements

## ⚙️ Initialization
    t[i][0] = True
    t[0][j] = False

## 🔁 Transition
    if arr[i-1] <= j:
        t[i][j] = t[i-1][j-arr[i-1]] OR t[i-1][j]
    else:
        t[i][j] = t[i-1][j]

## 💻 Code

    class Solution:
        def isSubsetSum(self, arr, sum):
            n = len(arr)

            t = [[False] * (sum + 1) for _ in range(n + 1)]

            for i in range(n + 1):
                t[i][0] = True

            for j in range(1, sum + 1):
                t[0][j] = False

            for i in range(1, n + 1):
                for j in range(1, sum + 1):
                    if arr[i - 1] <= j:
                        t[i][j] = t[i - 1][j - arr[i - 1]] or t[i - 1][j]
                    else:
                        t[i][j] = t[i - 1][j]

            return t[n][sum]

## ⏱️ Complexity
    Time: O(n * sum)
    Space: O(n * sum)

---

# 🎯 Final Summary

- Recursion → explores all subsets (slow)
- Memoization → avoids recomputation
- Tabulation → most efficient

👉 Core idea:
    include or exclude each element

👉 Pattern:
    0/1 Knapsack
