# 🔗 Longest Common Substring

## 🧩 Problem Statement

Given two strings `s1` and `s2`, find the length of the **longest common substring**.

👉 A substring must be **contiguous** (unlike subsequence).

---

## 📌 Example

### Input:
s1 = "GeeksforGeeks"  
s2 = "GeeksQuiz"  

### Output:
5  

### 💡 Explanation:
Longest common substring = **"Geeks"**

---

## 🧠 Key Idea

- If characters match → extend substring  
- If not → reset to `0` (because substring must be continuous)

---

# 🚀 Approach 1: 2D DP (Tabulation)

## 💡 Idea

Let:
- `t[i][j]` = length of longest common substring ending at `s1[i-1]` and `s2[j-1]`

---

## 🧾 Code

```python
class Solution:
    def longCommSubstr(self, s1, s2):
        m, n = len(s1), len(s2)
        maxLen = 0

        t = [[0]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                    maxLen = max(maxLen, t[i][j])
                else:
                    t[i][j] = 0

        return maxLen
```

---

## ⏱️ Complexity

- Time: `O(m * n)`  
- Space: `O(m * n)`  

---

# ⚡ Approach 2: 1D DP (Space Optimized)

## 💡 Idea

- Use only previous row instead of full table  
- `prev[j]` = previous row  
- `curr[j]` = current row  

---

## 🧾 Code

```python
class Solution:
    def longCommSubstr(self, s1, s2):
        m, n = len(s1), len(s2)
        maxLen = 0

        prev = [0] * (n + 1)

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    curr[j] = 1 + prev[j-1]
                    maxLen = max(maxLen, curr[j])
                else:
                    curr[j] = 0
            prev = curr

        return maxLen
```

---

## ⏱️ Complexity

- Time: `O(m * n)`  
- Space: `O(n)`  

---

# 🔥 Substring vs Subsequence (CRITICAL)

| Feature | Substring | Subsequence |
|--------|----------|------------|
| Continuity | ✅ Required | ❌ Not required |
| On mismatch | Reset to `0` | Take max |
| DP relation | Diagonal only ↖ | Diagonal + top + left |

---

## 💬 Key Insight

👉 Substring = “continuous match”  
👉 So:
- Match → extend  
- Mismatch → break (reset)

---

## ⚠️ Common Mistake

Using LCS logic here:
```python
t[i][j] = max(t[i-1][j], t[i][j-1]) ❌
```

👉 This is for **subsequence**, not substring.

---

## 🧠 Pro Tip

If problem says:
- “continuous” / “substring” → reset to `0`
- “subsequence” → use max()

👉 That one keyword changes the entire DP logic.
