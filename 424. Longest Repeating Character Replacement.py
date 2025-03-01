# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        maxCount = 0
        rem = k
        # longestSubstring = 0
        start = 0
        
        for char in s:
            counts[char] += 1
            if counts[char] > maxCount:
                maxCount = counts[char]
            else:
                rem -= 1
                if rem < 0:
                    counts[s[start]] -= 1
                    start += 1
                    rem = 0

        return maxCount + k - rem
         
            
