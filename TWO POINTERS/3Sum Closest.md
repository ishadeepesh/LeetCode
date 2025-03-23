# 16. 3Sum Closest

## Problem Statement

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

### Example 1:
**Input:**
#### **nums = [-1,2,1,-4], target = 1**
**Output:**
#### **2**
**Explanation:**  
The sum that is closest to the target is `2` (`-1 + 2 + 1 = 2`).

---

## Solution

```python


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        mindiff = float('inf')
        minsum = 0
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                num_sum = num + nums[l] + nums[r]
                num_diff = target - num_sum
                
                if abs(num_diff) == 0:
                    return num_sum
                
                if abs(num_diff) < mindiff:
                    mindiff = abs(num_diff)
                    minsum = num_sum
                
                if num_diff > 0:
                    l += 1
                elif num_diff < 0:
                    r -= 1
                
        return minsum
