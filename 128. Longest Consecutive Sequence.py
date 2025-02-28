# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcnt=0
        num_set=set(nums)
        for i in num_set:
            if i-1 not in num_set:
                count=1
                while i+1 in num_set:
                    count+=1
                    i+=1
                maxcnt=max(count,maxcnt)
        return maxcnt
