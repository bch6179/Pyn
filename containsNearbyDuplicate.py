import collections

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash = {}
        
        for i in range(len(nums)):
            if nums[i] in hash:
                if i - hash[nums[i]] <= k:
                    return True
            hash[nums[i]] = i
        return False

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if not nums:
            return False
        pos = set()
        for i,v in enumerate(nums):
            if len(pos) > k:
                pos.remove(nums[i-k-1])
            if nums[i] in pos:
                return True
            else:
                pos.add(nums[i])
        return False