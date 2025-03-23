# 1. Two Sum

## Problem Statement
Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in **any order**.

### **Example**
#### **Input**
#### **nums = [2,7,11,15]**
#### **target = 9**
#### **Output: [0,1]**
#### **Explanation: nums[0] + nums[1] = 2 + 7 = 9**
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], i]
            d[num] = i
        return []
```
Time Complexity: O(N) | Space Complexity: O(N)
