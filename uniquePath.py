class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1: return 0
        dp = [[1 for i in range(n)] for j in range(m)]
        
        for i in range(1, m ):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]
    def uniquePathsWithObstacles1(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m < 1 or n < 1: return 0
        dp = [[0 for i in range(n)] for j in range(m)]
        for j in range(0,n):
            if obstacleGrid[0][j] == 0:
                    dp[0][j] = 1
            else: break
        
        for i in range(0,m):
            if obstacleGrid[i][0] == 0:
                    dp[i][0] = 1
            else: break
                
        for i in range(1, m ):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m-1][n-1]
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m < 1 or n < 1: return 0
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
       # if obstacleGrid[0][0] == 1: return 0


        #dp[1][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if obstacleGrid[i-1][j-1] == 1:
                    dp[i][j] = 0
                else:
                    if i == 1 and j == 1:
                        dp[i][j] = 1    #Mistake reset dp[1][1] to 0 after init; and i==0 j ==0
                    else:
                      dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[m][n]
s = Solution() 
print s.uniquePathsWithObstacles([[0]])
#print s.uniquePaths(2,3)
