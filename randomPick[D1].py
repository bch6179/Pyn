import random

class Solution(object):
    def __init__(self, nums):
        self.nums = nums
        
    def pick(self, target):
        count = 1
        res = None
        for index, num in enumerate(self.nums):
            if num == target:
                if random.randint(1, count) == 1:
                    res = index
                count += 1
        return res

s = Solution([1,2,3,3,3])
print s.pick(3)
print s.pick(3)

# eturn random.choice([k for k, v in enumerate(self.nums) if v == target])
# public int pick(int target) {
# int result = -1;
# int count = 0; // to record how many targets in the array
# for (int i = 0; i < nums.length; i++) {
# if (nums[i] != target)
# continue;
# /*
# For the nth target, ++count is n. Then the probability that rnd.nextInt(++count)==0 is 1/n. Thus, the probability that return nth target is 1/n.
# For (n-1)th target, the probability of returning it is (n-1)/n * 1/(n-1)= 1/n.
# */
# if (rnd.nextInt(++count) == 0)
# result = i;
# }
# return result;
# }
#   nextInt(int n) method is used to get a pseudorandom, uniformly distributed int value between 0 (inclusive) and the specified value (exclusive), drawn from this random number generator's sequence.
# Reservoir Sampling".

# Reservoir sampling is a family of randomized algorithms for randomly choosing a sample of k items from a list S containing n items, where n is either a very large or unknown number. Typically n is large enough that the list doesn't fit into main memory.
#  we know the total number of items (n), then the solution is easy: select an index i between 1 and n with equal probability, and keep the i-th element. The problem is that we do not always know n in advance. A possible solution is the following:

# Keep the first item in memory.
# When the i-th item arrives (for {\displaystyle i>1} i>1):
# with probability {\displaystyle 1/i} 1/i, keep the new item (discard the old one)
# with probability {\displaystyle 1-1/i} {\displaystyle 1-1/i}, keep the old item (ignore the new one)
# So:
# n-1/n * 1/n-1 = 1/n each  item is kept with 1/n
# when there is only one item, it is kept with probability 1;
# when there are 2 items, each of them is kept with probability 1/2;
# when there are 3 items, the third item is kept with probability 1/3, and each of the previous 2 items is also kept with probability (1/2)(1-1/3) = (1/2)(2/3) = 1/3;
# by induction, it is easy to prove that when there are n items, each item is kept with probability 1/n.

# from random import randrange
# class Solution(object):

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         :type numsSize: int
#         """
#         self.memoCounts = {}
#         self.nums = nums

#     def getCount(self, target):
#         # O(n)
#         if target in self.memoCounts:
#             return self.memoCounts[target]
            
#         count = 0
#         for el in self.nums:
#             if el == target:
#                 count += 1
#         self.memoCounts[target] = count
#         return count
        
#     def pick(self, target):
#         """
#         :type target: int
#         :rtype: int
#         """
#         count = self.getCount(target)
#         randIndex = randrange(count) # [0...count)
#         targetIndex = 0

#         for i in xrange(len(self.nums)):
#             if self.nums[i] == target:
#                 if targetIndex == randIndex:
#                     return i
#                 targetIndex += 1
        
#         return "bla"


o those who don't understand why it works. Consider the example in the OJ
{1,2,3,3,3} with target 3, you want to select 2,3,4 with a probability of 1/3 each.

2 : It's probability of selection is 1 * (1/2) * (2/3) = 1/3
3 : It's probability of selection is (1/2) * (2/3) = 1/3
4 : It's probability of selection is just 1/3

So they are each randomly selected.

/*
For the nth target, ++count is n. Then the probability that rnd.nextInt(++count)==0 is 1/n. Thus, the probability that return nth target is 1/n.
For (n-1)th target, the probability of returning it is (n-1)/n * 1/(n-1)= 1/n.
*/
if (rnd.nextInt(++count) == 0)
result = i;
}
return result;
}