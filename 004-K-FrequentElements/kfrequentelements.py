'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        output = []

        if len(nums) <= 1:
            return False

        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        
        for j in range(k):
            mostFrequent = max(dic.values())
            value = dic.keys()[dic.values().index(mostFrequent)]
            output.append(value)
            dic.pop(value)

        return output
