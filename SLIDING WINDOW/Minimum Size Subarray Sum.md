# 209. Minimum Size Subarray Sum

## Problem Statement
Given an array of positive integers `nums` and a positive integer `target`, return the **minimal length** of a subarray whose sum is greater than or equal to `target`.  
If there is no such subarray, return `0` instead.

### **Example**
#### **Input**
```python
target = 7
nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowSum = 0
        windowStart = 0
        minlength = float('inf')

        for windowEnd in range(len(nums)):
            windowSum += nums[windowEnd]
            while windowSum >= target:
                minlength = min(minlength, windowEnd - windowStart + 1)
                windowSum -= nums[windowStart]
                windowStart += 1

        return minlength if minlength < float('inf') else 0
