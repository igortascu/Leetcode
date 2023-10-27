'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
'''
class Solution(object):
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        dic2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 0

        for i in range(len(t)):
            if t[i] in dic2:
                dic2[t[i]] += 1
            else:
                dic2[t[i]] = 0
        
        return dic == dic2

        