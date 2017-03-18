
https://leetcode.com/problems/range-sum-query-immutable/?tab=Description

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.


class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        
        self.dp = [[0]*len(nums)]*len(nums) #Mistake 
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if j > 0 and i !=j:
                    self.dp[i][j] = self.dp[i][j-1]+nums[j] 
                else:   self.dp[i][j] = nums[j]
                
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[i][j]
#  class NumArray(object):
#     def __init__(self, nums):
#         self.dp = nums
#         for i in xrange(1, len(nums)):
#             self.dp[i] += self.dp[i-1]

#     def sumRange(self, i, j):
#         return self.dp[j] - (self.dp[i-1] if i > 0 else 0)       
# class NumArray(object):
#     def __init__(self, nums):
#         """
#         initialize your data structure here.
#         :type nums: List[int]
#         """
#         self.accu = [0]
#         for num in nums: 
#             self.accu += self.accu[-1] + num,

#     def sumRange(self, i, j):
#         """
#         sum of elements nums[i..j], inclusive.
#         :type i: int 
#         :type j: int
#         :rtype: int 
#         """
#         return self.accu[j + 1] - self.accu[i]

# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)

numArray = NumArray([-2,0,3,-5,2,-1])
print (numArray.sumRange(0,2)) #,sumRange(2,5),sumRange(0,5))