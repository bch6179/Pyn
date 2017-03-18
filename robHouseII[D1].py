#[Note]
# #=====
how to break the circle, bu customization
It is because in the simpler question whether to rob num[lo] is entirely our choice. But, it is now constrained by whether num[hi] is robbed.]
# II, Customize, by select one of them, and neighbor not select, instead of all the cases, actually the select would cover other cases being selected




Since you cannot rob both the first and last house, just create two separate vectors, one excluding the first house, and another excluding the last house. The best solution generated from these two vectors using the original House Robber DP algorithm is the optimal on


It is because in the simpler question whether to rob num[lo] is entirely our choice. But, it is now constrained by whether num[hi] is robbed.

This is enough since one  chosen or not means another one in the circle also has been tried both of the opportunities based on the selected vectors

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        if n < 4: return max(nums)

        first, second = 0, 0
        for i in nums[:-1]: first, second = second, max(first + i, second)
        result = second

        first, second = 0, 0
        for i in nums[1:]: first, second = second, max(first + i, second)
        return max(result, second)

Same idea but little bit cleaner

class Solution(object):
    def rob(self, nums):
        def _rob(nums):
            a, b = 0, 0
            for i in xrange(len(nums)):
                a, b = b, max(a + nums[i], b)
            return b
        a, b = _rob(nums[:-1]), _rob(nums[1:])
        return max(a, b) if len(nums) is not 1 else nums[0]
 
 
def rob(self, nums):
        if len(nums) == 1: return nums[0]
        ppa, pa, ppb, pb = 0, 0, 0, 0
        for i in range(len(nums)-1):
            ppa, pa = pa, max(pa, ppa + nums[i])
            ppb, pb = pb, max(pb, ppb + nums[i+1])
        return max(pa, pb)