# 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
# Example 1:
# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
         #PYTHON SPECIFIC CODE
        currSum=sum(nums[:k])
        maxSum=currSum
        for i in range(k,len(nums)):
            currSum=currSum+nums[i]-nums[i-k]
            if currSum>maxSum:
                maxSum=currSum
        return maxSum/k
        #BRUTE-FORCE LOGIC
        # maxval=float(-inf)
        # n=len(nums)
        # for i in range(n-k+1):
        #     sum=0
        #     for j in range(i,i+k):
        #         sum+=nums[j]
        #     val=sum/k
        #     maxval=max(maxval,val)
        # return maxval

        #SLIDING WINDOW LOGIC
        # l, r, num_sum = 0, 0, 0
        # maxval = float('-inf')  # Correct indentation
        # n = len(nums)
        # for r in range(n):
        #     num_sum+=nums[r]
        #     if r-l+1==k:
        #         avg=num_sum/k
        #         maxval=max(maxval,avg)
        #         num_sum-=nums[l]
        #         l+=1
        #     r+=1
        # return maxval

       

