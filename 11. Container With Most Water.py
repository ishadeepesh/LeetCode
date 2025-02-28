# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        max_vol=0
        while i<j:
            mini=min(height[i],height[j])
            max_vol=max(max_vol,(j-i)*mini)
            if height[i]<=height[j]:
                i+=1
                while height[i]<height[i-1] and i<j:
                    i+=1
            else:
                j-=1
                while height[j+1]>height[j] and i<j:
                    j-=1
        return max_vol
