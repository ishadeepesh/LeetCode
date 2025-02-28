# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]. The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst=[]
        lst.append(1)
        mul=nums[0]
        for i in range(1,len(nums)):
            lst.append(mul)
            mul*=nums[i]
        right=1
        for j in range(len(nums)-1,-1,-1):
            lst[j]=right*lst[j]
            right*=nums[j]
        return lst
            
