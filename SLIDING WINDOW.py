643. Maximum Average Subarray I
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

209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.
# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        windowSum=0
        windowStart=0
        minlength=float('inf')

        for windowEnd in range(len(nums)):
            windowSum+=nums[windowEnd]
            while windowSum>=target:
                minlength=min(minlength,windowEnd-windowStart+1)
                windowSum-=nums[windowStart]
                windowStart+=1

        return minlength if minlength<float('inf') else 0


Longest Substring with K Uniques
# Given a string s, you need to print the size of the longest possible substring with exactly k unique characters. If no possible substring exists, print -1.
# Examples:
# Input: s = "aabacbebebe", k = 3
# Output: 7
# Explanation: "cbebebe" is the longest substring with 3 distinct characters.
class Solution:

    def longestKSubstr(self, s, k):
        # code here
        start=0
        d={}
        maxlength=0
        
        for r in range(len(s)):
            if s[r] not in d:
                d[s[r]]=0
            d[s[r]]+=1
            while len(d)>k:
                l=s[start]
                d[l]-=1
                if d[l]==0:
                    del d[l]
                start+=1
        
            if r-start+1>maxlength and len(d)==k:
                maxlength=r-start+1
        return -1 if maxlength==0 else maxlength

       

