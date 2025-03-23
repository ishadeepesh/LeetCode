# 27. Remove Element

## Problem Statement  
Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` **in-place**. The order of the elements may be changed. Then return the number of elements in `nums` which are **not equal** to `val`.  

Consider the number of elements in `nums` which are **not equal** to `val` be `k`. To get accepted, you need to do the following things:  
1. Change the array `nums` such that the first `k` elements of `nums` contain the elements which are **not equal** to `val`.  
2. The remaining elements of `nums` are not important as well as the size of `nums`.  
3. Return `k`.  

---

## Example 1:
#### **Input:**  
#### **nums = [3,2,2,3], val = 3** 
#### **Output: 2, nums = [2,2,_,_]** 
#### **Explanation: The first two elements are not equal to val, and we ignore the rest.** 

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
