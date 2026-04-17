# 🔗 Shortest Common Supersequence (Length)

## 🧩 Problem Statement

Given two strings `s1` and `s2`, find the **length of the shortest string** that has both `s1` and `s2` as subsequences.

👉 The resulting string must contain both strings while preserving order.

---

## 📌 Example

### Input:
s1 = "geek"  
s2 = "eke"  

### Output:
5  

### 💡 Explanation:
One possible SCS = "geeke"

---

## 🧠 Key Idea

👉 This problem is based on **Longest Common Subsequence (LCS)**

Formula:
```
Length of SCS = len(s1) + len(s2) - LCS(s1, s2)
```

---

## 🔁 Why This Works

- LCS = common part (no need to repeat)
- Remaining characters must be added

---

# 🚀 Approach: LCS-Based

## 💡 Idea

1. Find LCS of `s1` and `s2`  
2. Apply formula  

---

## 🧾 Code (Python)

```python
class Solution:
    def minSuperSeq(self, s1, s2):
        m, n = len(s1), len(s2)

        # Step 1: Build LCS table
        t = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])

        # Step 2: Apply formula
        return m + n - t[m][n]
```

---

## 🔍 Intuition

- Common characters → counted once  
- Non-common → added separately  

---

## 🎯 Example Walkthrough

s1 = "geek"  
s2 = "eke"  

LCS = "ek" → length = 2  

```
SCS length = 4 + 3 - 2 = 5
```

---

## ⏱️ Complexity

- Time: `O(m * n)`  
- Space: `O(m * n)`  

---

# 🔥 Summary

| Concept | Formula |
|--------|--------|
| LCS | common part |
| SCS length | m + n - LCS |

---

## 💬 Pro Tip

👉 If problem asks:
- “shortest string containing both”  

➡️ Think:
```
SCS = combine strings - overlap (LCS)
```

---

## ⚠️ Common Mistakes

- Trying to construct string instead of length ❌  
- Forgetting LCS relation ❌  
- Using substring logic ❌  

---

## 🧠 Final Insight

👉 LCS = overlap  
👉 SCS = merge using overlap  

That’s the whole trick.
