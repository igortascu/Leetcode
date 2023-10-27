'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = {}
        output = []

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dic:
                output.append(i)
                output.append(dic[difference])
            else:
                dic[nums[i]] = nums.index(nums[i])
        
        return output