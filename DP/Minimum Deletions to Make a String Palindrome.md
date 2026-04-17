# 🗑️ Minimum Deletions to Make a String Palindrome

## 🧩 Problem Statement

Given a string `s`, delete the **minimum number of characters** so that the resulting string becomes a **palindrome**.

👉 You must maintain the **relative order** of characters.

---

## 📌 Example

### Input:
s = "aebcbda"

### Output:
2  

### 💡 Explanation:
Remove:
- 'e'
- 'd'

Result → "abcba" (palindrome)

---

## 🧠 Key Idea

👉 This problem is based on **Longest Palindromic Subsequence (LPS)**

```
Minimum Deletions = n - LPS
```

---

## 🔁 Why This Works

- LPS = longest part of string that is already a palindrome  
- Everything else must be deleted  

---

## 🔗 Relation

```
LPS(s) = LCS(s, reverse(s))
```

---

# 🚀 Approach: LCS-Based

## 💡 Idea

1. Reverse the string  
2. Find LCS between original and reversed  
3. Subtract from total length  

---

## 🧾 Code (Python)

```python
class Solution:
    def minDeletions(self, s):
        n = len(s)
        s1 = s[::-1]

        t = [[0]*(n+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, n+1):
                if s[i-1] == s1[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])

        return n - t[n][n]
```

---

## 🔍 Intuition

- Keep longest palindromic subsequence  
- Delete all other characters  

---

## 🎯 Example Walkthrough

s = "aebcbda"  

Reverse = "adbcb ea"  

LCS = "abcba" → length = 5  

```
Min deletions = 7 - 5 = 2
```

---

## ⏱️ Complexity

- Time: `O(n^2)`  
- Space: `O(n^2)`  

---

# 🔥 Summary

| Step | Action |
|------|--------|
| 1 | Reverse string |
| 2 | Find LCS |
| 3 | Apply formula |

---

## 💬 Pro Tip

👉 If problem says:
- “make palindrome”  
- “minimum deletions”  

➡️ Think:
```
Answer = n - LPS
```

---

## ⚠️ Common Mistakes

- Using substring instead of subsequence ❌  
- Forgetting reverse string ❌  
- Wrong DP size ❌  

---

## 🧠 Final Insight

👉 LPS = what you keep  
👉 Rest = what you delete  

That’s the whole trick.
