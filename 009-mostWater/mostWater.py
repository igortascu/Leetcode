'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height) - 1
        maxArea = 0

        while start < end:
            if height[start] < height[end]:
                maxArea = max(maxArea, height[start] * (end - start))
                start += 1
            else:
                maxArea = max(maxArea, height[end] * (end - start))
                end -= 1
        
        return maxArea

        