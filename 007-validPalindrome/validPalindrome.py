'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
'''
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = re.sub(r'[^0-9a-zA-Z]', '', s).lower()
        s = s.lower()
        s = s.strip()

        start = 0
        end = len(s) - 1

        print(s)
        while start < end:
            if  s[start] != s[end]:
                return False
            start += 1
            end -= 1
        
        return True 