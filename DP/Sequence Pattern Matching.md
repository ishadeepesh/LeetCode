# 🔍 Sequence Pattern Matching (Subsequence Check)

## 🧩 Problem Statement

Given two strings `s1` and `s2`, check whether `s1` is a **subsequence** of `s2`.

👉 A subsequence is formed by deleting characters **without changing order**

---

## 📌 Example

### Input:
s1 = "abc"  
s2 = "ahbgdc"  

### Output:
True  

---

## 🧠 Key Idea

👉 We don’t need DP here.

We just need to check:
> Can we match all characters of `s1` inside `s2` in order?

---

# 🚀 Optimal Approach: Two Pointers (Greedy)

## 💡 Idea

- Traverse both strings
- Move pointer in `s1` only when characters match
- Always move pointer in `s2`

---

## 🧾 Code (Python)

```python
class Solution:
    def isSubsequence(self, s1: str, s2: str) -> bool:
        i, j = 0, 0

        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i += 1
            j += 1

        return i == len(s1)
```

---

## 🔍 Intuition

- Match → move both  
- No match → move only in `s2`  

👉 We are “scanning” `s2` to find all chars of `s1`

---

## 🎯 Dry Run

s1 = "abc"  
s2 = "ahbgdc"  

```
a == a → i++
h skip
b == b → i++
g skip
c == c → i++
```

👉 All characters matched → True

---

## ⏱️ Complexity

- Time: `O(n)`  
- Space: `O(1)`  

---

# ❌ Why NOT DP (LCS)?

DP approach:
```
Check if LCS(s1, s2) == len(s1)
```

### Problems:

- Time: `O(m * n)` ❌  
- Space: `O(m * n)` ❌  
- Overkill for simple check  

---

# 🔥 Summary

| Approach | Time | Space | Use |
|--------|------|------|-----|
| Two Pointer ✅ | O(n) | O(1) | Best |
| DP (LCS) ❌ | O(m*n) | O(m*n) | Avoid |

---

## 💬 Interview Tip

👉 If interviewer asks:
- “Is A a subsequence of B?”

➡️ Immediately say:
> “I’ll use a two-pointer greedy approach for O(n) time”

---

## ⚠️ Common Mistakes

- Using reverse traversal ❌  
- Using DP unnecessarily ❌  
- Not checking full match (`i == len(s1)`) ❌  

---

## 🧠 Final Insight

👉 Subsequence check ≠ DP problem  

👉 It’s a **greedy scanning problem**

---

## 🚀 One-Line Memory Trick

> “Move in s2 always, move in s1 only when match”
