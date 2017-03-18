# Analysis of this problem:
# Apparently, this is a optimization problem, which can be usually solved by DP. So when it comes to DP, the first thing for us to figure out is the format of the sub problem(or the state of each sub problem). The format of the sub problem can be helpful when we are trying to come up with the recursive relation.

# At first, I think the sub problem should look like: maxSubArray(int A[], int i, int j), which means the maxSubArray for A[i: j]. In this way, our goal is to figure out what maxSubArray(A, 0, A.length - 1) is. However, if we define the format of the sub problem in this way, it's hard to find the connection from the sub problem to the original problem(at least for me). In other words, I can't find a way to divided the original problem into the sub problems and use the solutions of the sub problems to somehow create the solution of the original one.

# So I change the format of the sub problem into something like: maxSubArray(int A[], int i), which means the maxSubArray for A[0:i ] which must has A[i] as the end element. Note that now the sub problem's format is less flexible and less powerful than the previous one because there's a limitation that A[i] should be contained in that sequence and we have to keep track of each solution of the sub problem to update the global optimal value. However, now the connect between the sub problem & the original one becomes clearer:

# maxSubArray(A, i) = maxSubArray(A, i - 1) > 0 ? maxSubArray(A, i - 1) : 0 + A[i]; 

class Solution(object):
    def maxSubArrayWithRange(self, nums):
        # maxint = (1 << 31) -1
        # maxSoFar = - maxint - 1
        maxSoFar = nums[0]
        maxEndingHere = 0
        a=b=s=0
        for i, num in enumerate(nums):
            maxEndingHere += num
            if maxEndingHere < 0:
                maxEndingHere = 0
                s = i + 1
            if maxEndingHere > maxSoFar:
                maxSoFar = maxEndingHere 
                a = s 
                b = i 
        return a,b
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = nums[0]
        maxEndingHere = nums[0]
        
        for num in nums[1:]:
            maxEndingHere = max(num, num+maxEndingHere)
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSoFar = nums[0]
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(nums[i], nums[i]+dp[i-1])
            maxSoFar = max(maxSoFar, dp[i])
        return maxSoFar
s = Solution() 
print s.maxSubArrayWithRange([ -1, 2 , -5,3,4,-1, -5])