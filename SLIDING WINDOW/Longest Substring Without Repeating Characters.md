# 3. Longest Substring Without Repeating Characters

## 📌 Problem Statement

Given a string `s`, find the length of the **longest substring** without **duplicate characters**.

A substring is a contiguous sequence of characters within a string.

---

## 🧠 Example

**Input:**

```text
s = "abcabcbb"
```

**Output:**

```text
3
```

**Explanation:**
The longest substring without repeating characters is `"abc"`, which has a length of `3`.
Other valid substrings with the same length include `"bca"` and `"cab"`.

---

## 🚀 Approach (Sliding Window)

This solution uses the **sliding window technique**, which allows us to solve the problem efficiently in **O(n)** time.

### Key Ideas:

* Use two pointers (`l` and `r`) to represent the window.
* Maintain a `set` to track characters currently in the window.
* Expand the window by moving the right pointer.
* If a duplicate character is found, shrink the window from the left until the duplicate is removed.
* Track the maximum window size during the process.

---

## 🧪 Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxlength = 0, 0
        arr = set()
        
        for r in range(len(s)):
            while s[r] in arr:
                arr.remove(s[l])
                l += 1
            
            arr.add(s[r])
            maxlength = max(maxlength, r - l + 1)
        
        return maxlength
```

---

## ⏱️ Complexity Analysis

* **Time Complexity:** `O(n)`
  Each character is added and removed from the set at most once.

* **Space Complexity:** `O(min(n, m))`
  Where `m` is the size of the character set (e.g., 26 for lowercase English letters).

---
