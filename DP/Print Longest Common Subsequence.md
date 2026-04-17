# 🔗 Print Longest Common Subsequence (LCS)

## 🧩 Problem Statement

Given two strings `s1` and `s2`, return the **Longest Common Subsequence (LCS) string**.

👉 Unlike the standard LCS problem, here we need to **print the subsequence**, not just its length.

---

## 📌 Example

### Input:
s1 = "abcde"  
s2 = "ace"  

### Output:
"ace"  

---

## 🧠 Key Idea

### Step 1: Build DP Table
- `dp[i][j]` = length of LCS for first `i` chars of `s1` and first `j` chars of `s2`

### Step 2: Backtrack
- Start from `dp[n][m]`
- Move:
  - Diagonal ↖ if characters match  
  - Up ↑ or Left ← based on larger value  

---

# 🚀 Approach: DP + Backtracking

---

## 🧾 Code (Python)

```python
class Solution:
    def printLongestCommonSubsequence(self, s1: str, s2: str) -> str:
        n, m = len(s1), len(s2)

        # Step 1: Build DP table
        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # Step 2: Backtrack to build LCS string
        i, j = n, m
        res = []

        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:
                res.append(s1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1

        # Reverse because we built it backwards
        return "".join(res[::-1])
```

---

## 🔍 How Backtracking Works

From bottom-right:

- Match → take char + move diagonal ↖  
- No match → move to the side with larger value  

---

## 🎯 Example Walkthrough

s1 = "abcde"  
s2 = "ace"  

Backtracking path:
```
e == e → take 'e'
c == c → take 'c'
a == a → take 'a'
```

Built string (reverse): `"eca"`  
Final answer: `"ace"`

---

## ⏱️ Complexity

- Time: `O(n * m)`  
- Space: `O(n * m)`  

---

## ⚠️ Common Mistakes

- Forgetting to reverse result ❌  
- Using substring logic instead of subsequence ❌  
- Wrong movement during backtracking ❌  

---

## 💬 Pro Tip

👉 DP table gives **length**  
👉 Backtracking gives **actual string**

Both are needed for full solution.
