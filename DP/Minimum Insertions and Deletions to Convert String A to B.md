# 🔄 Minimum Insertions and Deletions to Convert String A to B

## 🧩 Problem Statement

Given two strings `s1` and `s2`, find the **minimum number of operations** required to convert `s1` into `s2`.

Allowed operations:
- ✅ Insert a character  
- ✅ Delete a character  

---

## 📌 Example

### Input:
s1 = "heap"  
s2 = "pea"  

### Output:
3  

### 💡 Explanation:
- Delete 'h' → "eap"  
- Replace (delete 'p' + insert 'p' properly) OR think via LCS  
- Final operations = 3  

---

## 🧠 Key Idea

👉 This problem is based on **Longest Common Subsequence (LCS)**

Let:
- `LCS = longest common subsequence length`

Then:

```
Deletions = len(s1) - LCS  
Insertions = len(s2) - LCS  
```

👉 Total operations:
```
= Deletions + Insertions  
= (m - LCS) + (n - LCS)  
= m + n - 2 * LCS
```

---

# 🚀 Approach: LCS Based

## 💡 Idea

1. Find LCS of `s1` and `s2`  
2. Use formula to compute operations  

---

## 🧾 Code (Python)

```python
class Solution:
    def minOperations(self, s1, s2):
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
        return m + n - (2 * t[m][n])
```

---

## 🔍 Intuition

👉 LCS represents the **common part we don’t need to touch**

Everything else:
- Remove extra characters from `s1`
- Insert missing characters to match `s2`

---

## 🎯 Example Walkthrough

s1 = "heap"  
s2 = "pea"  

LCS = "ea" → length = 2  

```
Deletions = 4 - 2 = 2  
Insertions = 3 - 2 = 1  
Total = 3
```

---

## ⏱️ Complexity

- Time: `O(m * n)`  
- Space: `O(m * n)`  

---

## 🔥 Summary

| Step | Action |
|------|--------|
| 1 | Find LCS |
| 2 | Apply formula |
| 3 | Return result |

---

## 💬 Pro Tip

👉 Whenever problem says:
- “convert string A to B”  
- using insert/delete  

➡️ Think **LCS immediately**

---

## ⚠️ Common Mistakes

- Forgetting LCS relation ❌  
- Trying greedy replacement ❌  
- Mixing with edit distance ❌  

---

## 🧠 Final Insight

👉 LCS = “what stays”  
👉 Everything else = operations  

That’s the whole trick.
