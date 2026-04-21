# 🔗 Matrix Chain Multiplication (MCM)

## 🧩 Problem Statement

Given an array `arr[]` where the `i-th` matrix has dimensions:

```
Matrix i → arr[i-1] x arr[i]
```

Find the **minimum number of multiplications** needed to multiply the chain of matrices.

---

## 📌 Example

### Input:
arr = [2, 1, 3, 4]

### Output:
20  

---

## 🧠 Key Idea

👉 We are NOT actually multiplying matrices  
👉 We are deciding **where to place brackets** to minimize cost

---

## 💡 Cost Formula

If we split at `k`:

```
Cost = cost(i → k) + cost(k+1 → j) + arr[i-1] * arr[k] * arr[j]
```

---

# 🚀 Approach 1: Recursion (Brute Force)

## 💡 Idea

- Try all possible partition points `k`
- Recursively compute cost

---

## 🧾 Code

```python
class Solution:
    def matrixMultiplication(self, arr):
        return self.solve(arr, 1, len(arr) - 1)

    def solve(self, arr, i, j):
        if i >= j:
            return 0

        mn = float('inf')

        for k in range(i, j):
            temp_ans = (
                self.solve(arr, i, k)
                + self.solve(arr, k+1, j)
                + arr[i-1] * arr[k] * arr[j]
            )
            mn = min(mn, temp_ans)

        return mn
```

---

## ⏱️ Complexity

- Time: `O(2^n)` ❌ (very slow)  
- Space: recursion stack  

---

# ⚡ Approach 2: Memoization (Top-Down DP)

## 💡 Idea

- Store results of `(i, j)`  
- Avoid recomputing same subproblems  

---

## 🧾 Code

```python
class Solution:
    def matrixMultiplication(self, arr):
        n = len(arr)
        t = [[-1]*(n+1) for _ in range(n+1)]
        return self.solve(arr, 1, n-1, t)

    def solve(self, arr, i, j, t):
        if i >= j:
            return 0

        if t[i][j] != -1:
            return t[i][j]

        mn = float('inf')

        for k in range(i, j):
            temp_ans = (
                self.solve(arr, i, k, t)
                + self.solve(arr, k+1, j, t)
                + arr[i-1] * arr[k] * arr[j]
            )
            mn = min(mn, temp_ans)

        t[i][j] = mn
        return t[i][j]
```

---

## ⏱️ Complexity

- Time: `O(n^3)` ✅  
- Space: `O(n^2)`  

---

# 🔥 Summary

| Approach | Time | Space | Use |
|--------|------|------|-----|
| Recursion | Exponential ❌ | Stack | Concept only |
| Memoization | O(n³) ✅ | O(n²) | Practical |

---

## 🔍 Intuition

We are trying all ways to:
```
(A1 x A2 x A3 x ... x An)
```

and choosing the one with **minimum multiplication cost**

---

## ⚠️ Common Mistakes

- Using wrong `k` range ❌  
- Using `-inf` instead of `inf` ❌  
- Forgetting `arr[i-1] * arr[k] * arr[j]` ❌  
- Missing memoization ❌  

---

## 💬 Pro Tip

👉 MCM is a **partition DP problem**

Whenever you see:
- “split the array”
- “find optimal partition”

➡️ Think:
```
Try all k → minimize/maximize
```

---

## 🧠 Final Insight

👉 This is not about matrices  
👉 It’s about **optimal partitioning**

That pattern repeats in:
- Palindrome Partitioning  
- Boolean Parenthesization  
- Burst Balloons  

👉 Master this once → unlock many hard problems
