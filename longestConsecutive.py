# /**
#  * Given an unsorted array of integers, find the length of the longest
#  * consecutive elements sequence.
#  * 
#  * For example,
#  * Given [100, 4, 200, 1, 3, 2],
#  * The longest consecutive elements sequence is [1, 2, 3, 4]. Return its
#  * length: 4.
#  * 
#  * Your algorithm should run in O(n) complexity.
#  * 
#  * Tags: Array, HashTable
#  */

import collections
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        map = {} #collections.defaultdict(lambda: int)
        res = 0
        for num in nums:
            if num in map: continue #Mistake if not skip, it will overwrite in map[num]=num
            low = map.get(num-1,  num)
            high = map.get(num+1,  num)
            res = max(res, high-low+1)
            map[num]=num
            map[low] = high
            map[high] = low
        return res   
s = Solution() 
print s.longestConsecutive([-2,-3,-3,7,-3,0,5,0,-8,-4,-1,2])


# irst turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.

# Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set. The length of the streak is then simply y-x and we update our global best with that. Since we check each streak only once, this is overall O(n). This ran in 44 ms on the OJ, one of the fastest Python submissions.

# def longestConsecutive(self, nums):
#     nums = set(nums)
#     best = 0
#     for x in nums:
#         if x - 1 not in nums:
#             y = x + 1
#             while y in nums:
#                 y += 1
#             best = max(best, y - x)
#     return best