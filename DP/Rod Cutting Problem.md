# 🪵 Rod Cutting Problem

## 🧩 Problem Statement

Given a rod of length `n` and an array `price[]`, where `price[i]` denotes the value of a piece of length `i+1`.

Your task is to determine the **maximum value** obtainable by cutting up the rod and selling the pieces.

---

## 📌 Example

### Input:
price = [1, 5, 8, 9, 10, 17, 17, 20]

### Output:
22

### 💡 Explanation:
Best cut:
- Length 2 → value = 5  
- Length 6 → value = 17  

Total = **5 + 17 = 22**

---

## 🧠 Key Idea

This is a classic **Unbounded Knapsack** problem:

- You can use the same rod length multiple times  
- Goal: maximize total value  

---

# 🚀 Approach 1: 2D DP (Unbounded Knapsack)

## 💡 Idea

- Treat each rod length as an item  
- You can take it multiple times  
- Use DP table `t[i][j]`

Where:
- `i` → number of lengths considered  
- `j` → current rod length  

---

## 🧾 Code

```python
class Solution:
    def cutRod(self, price):
        n = len(price)
        length = [i for i in range(1, n+1)]

        t = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if length[i-1] <= j:
                    t[i][j] = max(
                        price[i-1] + t[i][j - length[i-1]],  # include
                        t[i-1][j]                           # exclude
                    )
                else:
                    t[i][j] = t[i-1][j]

        return t[n][n]
```

---

## ⏱️ Complexity

- Time: `O(n^2)`  
- Space: `O(n^2)`  

---

# ⚡ Approach 2: 1D DP (Optimized)

## 💡 Idea

- `dp[i]` = max profit for rod length `i`
- Try every possible **first cut**

---

## 🧾 Code

```python
class Solution:
    def cutRod(self, price):
        n = len(price)
        dp = [0] * (n + 1)

        for i in range(1, n+1):
            for j in range(i):
                dp[i] = max(dp[i], price[j] + dp[i-j-1])

        return dp[n]
```

---

## 🔍 Dry Insight

For each length `i`, we try:

- Cut at length `j+1`
- Remaining rod = `i - (j+1)`
- Total = `price[j] + dp[remaining]`

---

## ⏱️ Complexity

- Time: `O(n^2)`  
- Space: `O(n)`  

---

# 🔥 Final Thoughts

- 2D DP → easier to understand (knapsack style)  
- 1D DP → cleaner and interview-friendly  

👉 Most people mess up because they confuse:
- ❌ 0/1 Knapsack  
- ✅ Unbounded Knapsack  

---

## 💬 Pro Tip

Whenever:
- You can reuse elements unlimited times  
- And want max/min value  

👉 Think **Unbounded Knapsack / Rod Cutting pattern**
