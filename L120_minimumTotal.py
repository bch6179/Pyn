# https://leetcode.com/problems/triangle/?tab=Description
# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).



class Solution(object):
    _staticBest = 0
    def __init__(self):
       self.best = 1 << 31 - 1
    def minimumTotal1(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if m <= 0: return 0

        n = len(triangle[m-1])
        if n <= 0: return 0
        dp = [[0 for j in range(n)] for i in range(m)]

        for j in range(n):
            dp[m-1][j]  = triangle[m-1][j]
        
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])-1, -1, -1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        
        return dp[0][0]
    def minimumTotal2(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if m <= 0: return 0

        n = len(triangle[m-1])
        if n <= 0: return 0
        dp = triangle[m-1]

        for i in range(m-2, -1, -1):
            for j in range(0,len(triangle[i])):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]
        
        return dp[0]
    def minimumTotal7(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        m = len(triangle)
        if m <= 0: return 0

        n1 = len(triangle[m-1])
        if n1 <= 0: return 0
        dp = triangle

        for i in range(1, m):
            dp[i][0] =dp[i-1][0]+triangle[i][0]
            n=len(triangle[i])
            dp[i][n-1] = dp[i-1][n-2]+triangle[i][n-1]
            for j in range(1,len(triangle[i])-1):
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
        
        return min(dp[n-1])

    def minimumTotal_DFS_DivideConquer(self, triangle):
        m = len(triangle)
        n = len(triangle[m-1])
        mem = [[-1 for j in range(n)] for i in range(m)]       
        return self.dfs(triangle,mem, 0,0)


    def dfs(self, triangle, mem, i, j):
        if i >= len(triangle) or j >= len(triangle[i]): return 0
        if (mem[i][j] != -1): return mem[i][j]
        mem[i][j] = min(self.dfs(triangle,mem, i+1,j), self.dfs(triangle, mem,i+1, j+1)) + triangle[i][j]
        return mem[i][j]
 
    def minimumTotal(self, triangle):        
        self.dfs2(triangle,0,0,0 )
        return self.best
    @classmethod
    def xxfn(cls):
        print(cls._staticBest)
    def dfs2(self, triangle, i,j,  sum):
        if i == len(triangle):
            if sum < self.best:
                self.best = sum
            return
        self.dfs2(triangle, i+1,j, sum+triangle[i][j])
        self.dfs2(triangle, i+1, j+1, sum+triangle[i][j])
        
 
s = Solution() 
s.xxfn()
#from numpy import matrix
M = []
M.append([2])
M.append([3,4])
M.append([6,5,7])
M.append([4,1,8,3])
M.append([4,1,8,3,9])
M.append([4,1,8,3,9,10])

# M=matrix([
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ])

print s.minimumTotal(M)