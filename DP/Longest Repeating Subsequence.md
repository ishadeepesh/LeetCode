# 🔁 Longest Repeating Subsequence (LRS)

## 🧩 Problem Statement

Given a string `s`, find the length of the **longest repeating subsequence**.

👉 The subsequence should appear **at least twice**  
👉 Same character can be reused **only if indices are different**

---

## 📌 Example

### Input:
s = "aab"

### Output:
1  

### 💡 Explanation:
Repeating subsequence = "a"

---

## 🧠 Key Idea

👉 This is a modified **Longest Common Subsequence (LCS)** problem.

We compare:
```
s vs s
```

BUT with a condition:
```
i != j
```

---

## 🔁 Why This Works

- We want repeating subsequence → compare string with itself  
- To avoid picking same index → enforce `i != j`

---

# 🚀 Approach: LCS with Condition

## 💡 Idea

- Build LCS table for `s` and `s`
- Only count when:
```
s[i-1] == s[j-1] AND i != j
```

---

## 🧾 Code (Python)

```python
class Solution:
    def LongestRepeatingSubsequence(self, s):
        n = len(s)
        t = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s[j-1] and i != j:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])

        return t[n][n]
```

---

## 🔍 Intuition

- Match → extend subsequence  
- Same index → ignore (to avoid cheating)  

---

## 🎯 Example Walkthrough

s = "aab"

Compare:
```
a a b
a a b
```

Valid matches:
- First 'a' with second 'a' (different indices)

👉 LRS length = 1

---

## ⏱️ Complexity

- Time: `O(n^2)`  
- Space: `O(n^2)`  

---

# 🔥 Summary

| Concept | Meaning |
|--------|--------|
| LCS(s, s) | compare string with itself |
| i != j | avoid same index |
| Result | longest repeating subsequence |

---

## 💬 Pro Tip

👉 If problem says:
- “repeating subsequence”  

➡️ Think:
```
LCS(s, s) + (i != j condition)
```

---

## ⚠️ Common Mistakes

- Forgetting `i != j` ❌  
- Using substring logic ❌  
- Comparing different strings ❌  

---

## 🧠 Final Insight

👉 This is just LCS with a small twist  

That one condition changes everything.
