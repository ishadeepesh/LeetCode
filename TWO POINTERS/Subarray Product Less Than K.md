# 713. Subarray Product Less Than K

## Problem Statement
Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.

### Example 1:
**Input:**  
#### **nums = [10,5,2,6], k = 100**
#### **Output**
#### **8**
#### **Explanation:**
#### **The 8 subarrays that have product less than 100 are:**
#### **[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]**

#### **Note that [10, 5, 2] is not included as the product is 100, which is not strictly less than k.**

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l, count, pdt = 0, 0, 1
        for r in range(len(nums)):
            pdt *= nums[r]

            while pdt >= k:
                pdt //= nums[l]
                l += 1

            count += r - l + 1 
        return count
