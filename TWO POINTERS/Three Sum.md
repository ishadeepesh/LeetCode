# 15. 3Sum

## Problem Statement
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:  
- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`

**Note:** The solution set must not contain duplicate triplets.

### Example 1:
#### **Input:**
nums = [-1, 0, 1, 2, -1, -4]
#### **Output:**
[[-1, -1, 2], [-1, 0, 1]]

---

## Solution in Python
```python
from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        negative = defaultdict(int)
        positive = defaultdict(int)
        zeros = 0
        for num in nums:
            if num < 0:
                negative[num] += 1
            elif num > 0:
                positive[num] += 1
            else:
                zeros += 1
        
        result = []
        if zeros:
            for n in negative:
                if -n in positive:
                    result.append((0, n, -n))       
            if zeros > 2:
                result.append((0,0,0))

        for set1, set2 in ((negative, positive), (positive, negative)):
            set1Items = list(set1.items())
            for i, (j, k) in enumerate(set1Items):
                for j2, k2 in set1Items[i:]:
                    if j != j2 or (j == j2 and k > 1):
                        if -j-j2 in set2:
                            result.append((j, j2, -j-j2))
        return result
