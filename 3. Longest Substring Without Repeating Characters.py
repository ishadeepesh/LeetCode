# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      seen={}
        count=0
        l=0
        for r in range(len(s)):
            if s[r] not in seen:
                count=max(count,r-l+1)
            else:
                if seen[s[r]]<l:
                    count=max(count,r-l+1)
                else:
                    l=seen[s[r]]+1
            seen[s[r]]=r
        return count
