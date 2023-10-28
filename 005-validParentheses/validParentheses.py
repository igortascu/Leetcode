'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''
from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = deque()
        dic = {'(': ')', '{': '}', '[': ']'}

        for bracket in s:
            if bracket in dic:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != dic[stack.pop()]:
                return False
        
        return len(stack) == 0
