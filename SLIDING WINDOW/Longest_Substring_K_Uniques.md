# Longest Substring with K Unique Characters

## Problem Statement
Given a string `s`, find the length of the **longest** substring that contains exactly `k` unique characters.  
If no possible substring exists, return `-1`.

### **Example**
#### **Input**
#### **s = "aabacbebebe"**
#### **k = 3**
#### **Output: 7**
#### **Explanation: "cbebebe" is the longest substring with 3 distinct characters.**
```python
class Solution:
    def longestKSubstr(self, s: str, k: int) -> int:
        start = 0
        d = {}
        maxlength = 0

        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            while len(d) > k:
                d[s[start]] -= 1
                if d[s[start]] == 0:
                    del d[s[start]]
                start += 1

            if r - start + 1 > maxlength and len(d) == k:
                maxlength = r - start + 1

        return -1 if maxlength == 0 else maxlength
