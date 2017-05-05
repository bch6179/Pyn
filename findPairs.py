class Solution(object):
    def findPairs(self, nums, k):
        dict = {}
        for i,c in enumerate(nums):
            dict[c+k] = (i,c)
            
        count = 0
        for i,c in enumerate(nums):
            if c in dict and i != dict[c][0]:
                count += 1
                del dict[c]
        return count
    def findPairsBad(self, nums, k):
        dict = {}
        for c in nums:
            dict[c+k] = c
            
        count = 0
        for c in nums:
            if c in dict:
                count += 1
                del dict[c]
        return count
    def findPairs2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        begin = 0
        end = 1
        count = 0
        while begin < end and end < len(nums):
            diff = nums[end] - nums[begin]
            if diff < k:
                end += 1
            elif diff > k:
                begin += 1
                end = begin+ 1
            else:
                begin += 1
                count += 1
                while begin == 0 or len(nums) > begin > 0 and nums[begin] == nums[begin-1]:
                    begin += 1
                end = begin + 1
            
        return count
s = Solution()

print s.findPairs([1,2,3,4,5], -1)
print s.findPairs([1,3,1,5,4], 0    )