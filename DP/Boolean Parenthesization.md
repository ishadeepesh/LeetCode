# 🔗 Boolean Parenthesization

## 🧩 Problem Statement

Given a boolean expression `s` containing:

- `'T'` → True  
- `'F'` → False  

Operators:
- `&` → AND  
- `|` → OR  
- `^` → XOR  

👉 Count the number of ways to parenthesize the expression such that it evaluates to **True**

---

## 📌 Example

### Input:
s = "T|T&F^T"

### Output:
4  

### 💡 Explanation:

Valid ways:
```
((T|T)&(F^T))
(T|(T&(F^T)))
(((T|T)&F)^T)
(T|((T&F)^T))
```

---

## 🧠 Key Idea

👉 This is a **Partition DP problem (like MCM)**

But with an extra dimension:
```
(i, j, isTrue)
```

---

# 🚀 Approach 1: Recursion (Brute Force)

## 💡 Idea

- Try all partition points `k`
- Calculate:
  - Left True / False
  - Right True / False
- Combine based on operator

---

## 🧾 Code

```python
class Solution:
    def countWays(self, s):
        return self.solve(s, 0, len(s) - 1, True)

    def solve(self, s, i, j, isTrue):
        if i > j:
            return 0

        if i == j:
            if isTrue:
                return 1 if s[i] == 'T' else 0
            else:
                return 1 if s[i] == 'F' else 0

        ans = 0

        for k in range(i + 1, j, 2):
            lT = self.solve(s, i, k - 1, True)
            lF = self.solve(s, i, k - 1, False)
            rT = self.solve(s, k + 1, j, True)
            rF = self.solve(s, k + 1, j, False)

            if s[k] == '&':
                if isTrue:
                    ans += lT * rT
                else:
                    ans += lT*rF + lF*rT + lF*rF

            elif s[k] == '|':
                if isTrue:
                    ans += lT*rT + lT*rF + lF*rT
                else:
                    ans += lF*rF

            elif s[k] == '^':
                if isTrue:
                    ans += lT*rF + lF*rT
                else:
                    ans += lT*rT + lF*rF

        return ans
```

---

## ⏱️ Complexity

- Time: Exponential ❌  
- Space: recursion stack  

👉 Will TLE

---

# ⚡ Approach 2: Memoization (Top-Down DP)

## 💡 Idea

Store results for:
```
(i, j, isTrue)
```

---

## 🧾 Code

```python
class Solution:
    def countWays(self, s):
        self.dp = {}
        return self.solve(s, 0, len(s) - 1, True)

    def solve(self, s, i, j, isTrue):
        if i > j:
            return 0

        if i == j:
            if isTrue:
                return 1 if s[i] == 'T' else 0
            else:
                return 1 if s[i] == 'F' else 0

        key = (i, j, isTrue)

        if key in self.dp:
            return self.dp[key]

        ans = 0

        for k in range(i + 1, j, 2):
            lT = self.solve(s, i, k - 1, True)
            lF = self.solve(s, i, k - 1, False)
            rT = self.solve(s, k + 1, j, True)
            rF = self.solve(s, k + 1, j, False)

            if s[k] == '&':
                if isTrue:
                    ans += lT * rT
                else:
                    ans += lT*rF + lF*rT + lF*rF

            elif s[k] == '|':
                if isTrue:
                    ans += lT*rT + lT*rF + lF*rT
                else:
                    ans += lF*rF

            elif s[k] == '^':
                if isTrue:
                    ans += lT*rF + lF*rT
                else:
                    ans += lT*rT + lF*rF

        self.dp[key] = ans
        return ans
```

---

## ⏱️ Complexity

- Time: `O(n^3)` ⚠️  
- Space: `O(n^2)`  

---

# 🔥 Summary

| Approach | Time | Space | Status |
|--------|------|------|--------|
| Recursion | Exponential ❌ | Stack | TLE |
| Memoization | O(n³) ⚠️ | O(n²) | Accepted |

---

# 🧠 Core Transition Logic

| Operator | True Ways | False Ways |
|--------|----------|-----------|
| `&` | lT * rT | lT*rF + lF*rT + lF*rF |
| `|` | lT*rT + lT*rF + lF*rT | lF*rF |
| `^` | lT*rF + lF*rT | lT*rT + lF*rF |

---

# ⚠️ Common Mistakes

- Mixing boolean with counts ❌  
- Forgetting `(i, j, isTrue)` state ❌  
- Wrong operator conditions ❌  
- Missing memoization ❌  

---

# 💬 Interview Tip

👉 If you say:
> “This is MCM with an extra boolean state”

That’s exactly what interviewer expects.

---

# 🧠 Final Insight

👉 Pattern = Partition DP  
👉 State = `(i, j, isTrue)`  

---

## 🚀 One-Line Memory Trick

> “Split at operator, count left/right true/false, combine based on operator”
