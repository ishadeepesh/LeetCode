# 26. Remove Duplicates from Sorted Array

## Problem Statement  
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates **in-place** such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.  

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:  
1. Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially.  
2. The remaining elements of `nums` are not important as well as the size of `nums`.  
3. Return `k`.  

### Example 1:
#### **Input:**  
#### **nums = [1,1,2]**
#### **Output:**
#### **2, nums = [1,2,_]**
#### **Explanation: The first two elements are unique, and we ignore the rest.**

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r, num in enumerate(nums):
            if r > 0 and nums[r] > nums[l - 1]:  
                nums[l] = nums[r]
                l += 1
        return l
