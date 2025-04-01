### 977. Squares of a Sorted Array

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

#### Example 1:

**Input:**  
`nums = [-4,-1,0,3,10]`  

**Output:**  
`[0,1,9,16,100]`  

**Explanation:**  
After squaring, the array becomes `[16,1,0,9,100]`.  
After sorting, it becomes `[0,1,9,16,100]`.

```python

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        return nums
```
#### **Two Pointers Approach**
```python

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        squares = [0] * n  # Initialize an array with the same size, filled with 0s
        highest_square_index = n - 1  # Start filling from the end
        start, end = 0, n - 1  # Two pointers

        while start <= end:
            start_square = nums[start] ** 2
            end_square = nums[end] ** 2

            if start_square > end_square:
                squares[highest_square_index] = start_square
                start += 1
            else:
                squares[highest_square_index] = end_square
                end -= 1
        
            highest_square_index -= 1  # Move the index for the next largest square
    
        return squares
