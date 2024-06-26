'''
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead.
'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        stack = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if len(stack) == 0:
                stack.append(temperatures[i])

            
            elif temperatures[i] > stack.pop():
                output.append(i - stack[-1:][0])
            

