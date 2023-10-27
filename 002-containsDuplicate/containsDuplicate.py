'''
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.
'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        mySet = set()

        for i in range(len(nums)):
            if nums[i] in mySet:
                return True
            else:
                mySet.add(nums[i])

        return False
    
