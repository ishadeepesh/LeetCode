# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Approach1
        # d=defaultdict(int)
        # if len(s)!=len(t):
        #     return False
        # for i in s:
        #     d[i]+=1
        # for j in t:
        #     d[j]-=1
        # for k in d.keys():
        #     if d[k]!=0:
        #         return False
        # return True  


        #Approach 2
        if len(s) != len(t): 
            return False
            
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        
        return True          
