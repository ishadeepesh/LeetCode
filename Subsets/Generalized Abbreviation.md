# Generalized Abbreviation

# Problem Statement

Given a string `word`, generate **all possible generalized abbreviations** of that word.

A generalized abbreviation replaces **any number of consecutive characters** with the **count of those characters**.

The order of output does not matter.

### Rules

* Any substring of characters can be abbreviated.
* Consecutive abbreviated characters must be represented by **a single number**.
* Numbers represent **how many characters were skipped**.

---

# Example

### Example 1

**Input**

```
word = "BAT"
```

**Output**

```
[
"BAT",
"BA1",
"B1T",
"B2",
"1AT",
"1A1",
"2T",
"3"
]
```

### Explanation

Each abbreviation represents replacing consecutive characters with their count.

Examples:

```
"BA1" → BAT (T abbreviated)
"B1T" → BAT (A abbreviated)
"2T"  → BAT (BA abbreviated)
"3"   → BAT (all characters abbreviated)
```

Total abbreviations for a word of length **n** = **2ⁿ**.

---

# Approach

We solve the problem using **Depth First Search (DFS) / Backtracking**.

At each character we have **two choices**:

### 1. Abbreviate the character

* Skip the character.
* Increase a counter representing how many characters have been abbreviated consecutively.

### 2. Keep the character

* If there is a pending abbreviation count, append it to the result.
* Append the current character.
* Reset the count.

---

## Key Idea

We maintain three variables during recursion:

| Variable | Meaning                                      |
| -------- | -------------------------------------------- |
| `index`  | Current position in the word                 |
| `abb`    | Current abbreviation string being built      |
| `count`  | Number of consecutive abbreviated characters |

When we reach the end of the word:

* If `count > 0`, append the count.
* Store the abbreviation.

---

# Code (Python)

```python
from typing import List

class Solution:
    def generate_abbreviations(self, word: str) -> List[str]:

        def dfs(index: int, abb: str, count: int):
            if index == len(word):
                if count:
                    abb += str(count)
                res.append(abb)
                return

            # Choice 1: Abbreviate the current character
            dfs(index + 1, abb, count + 1)

            # Choice 2: Keep the current character
            if count:
                dfs(index + 1, abb + str(count) + word[index], 0)
            else:
                dfs(index + 1, abb + word[index], 0)

        res = []
        dfs(0, "", 0)
        return res
```

---

# Dry Run (Example: `"BAT"`)

```
Start: index=0, abb="", count=0
```

Choices at each character:

```
Skip B → count=1
Skip A → count=2
Skip T → count=3 → "3"

Skip B → count=1
Skip A → count=2
Keep T → "2T"

Skip B → count=1
Keep A → "1A"
Skip T → "1A1"

Keep B → "B"
Skip A → "B1"
Keep T → "B1T"
```

All possible abbreviations are generated.

---

# Time Complexity

```
O(n * 2^n)
```

Explanation:

* Each character has **2 choices** (abbreviate or keep).
* Total combinations = **2ⁿ**.
* Constructing each string can take up to **O(n)**.

---

# Space Complexity

```
O(n * 2^n)
```

Explanation:

* We store up to **2ⁿ abbreviations**.
* Each abbreviation can have length up to **n**.

Recursion depth is **O(n)**.

---

# Key Takeaways

* This is a **DFS + state tracking problem**.
* The important trick is **delaying the addition of abbreviation counts** until necessary.
* Always track:

  * current index
  * current abbreviation string
  * consecutive abbreviation count.

---
