# https://leetcode.com/problems/summary-ranges/?tab=Description
# Given a sorted integer array without duplicates, return the summary of its ranges.

# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def summaryRanges2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start , end = 0, 0
        res = []
        n = len(nums)
        for i in range(n):
            end = i
            if (i < n-1 and nums[i]+1 != nums[i+1]) or i == n-1:
                if end > start:
                    res.append(str(nums[start])+'->'+str(nums[end]))
                else:
                    res.append(str(nums[start]))
                start = i+1
                end = i+1
        return res
        
    def summaryRanges(self, nums):
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
#[[0],[2]]
s = Solution()
print s.summaryRanges([0,1,2,4,5,7])