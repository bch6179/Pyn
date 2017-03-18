
# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum

# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.

#not avoid the complexity of getting start and end, while only asking for length
#should merge two loops by one together
#should sum -nums[i] inside the loop and check to save overhead
#greedy get min len before shrinking the left border
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        sum = 0
        res = (1 << 31) -1
        while i < len(nums):
            sum+=nums[i]
            while j < len(nums) and sum >= s:
                res = min(res, i-j+1)
                sum-=nums[j]
                j+=1
            i+=1 #Mistake not increasing literally, when checking lower a bit 
        return 0 if res == (1 << 31) -1 else res #Mistake not checking 1 << 31 , for [] return max,
            