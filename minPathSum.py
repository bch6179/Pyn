#[Note]
#=====
#i start from 1 by handling i = 1 specially, in the same pass, since row by row initing won't affect following lines
#otherwise, 0 need int_max
class Solution(object):
    def minPathSum2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for x in range(n+1)] for y in range(m+1)]

        for x in range(1, n+1):
            for y in range(1, m+1):
                if x == 1 :
                    dp[x][y] = dp[x][y-1] + grid[x-1][y-1]  
                if y == 1:
                    dp[x][y] = dp[x-1][y] + grid[x-1][y-1]
                if x >1 and y > 1:
                    dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + grid[x-1][y-1]
        return dp[n][m]

    def minPathSum3(self, grid):

        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        dp = [[0 for x in range(n)] for y in range(m)]
        dp[0][0] = grid[0][0]
        for x in range(n):
            for y in range(m):
                if x == 0 and y >= 1:
                    dp[x][y] = dp[x][y-1] + grid[0][y]  
                if y == 0 and x >= 1:
                    dp[x][y] = dp[x-1][y] + grid[x][0]
                if x >= 1 and y >= 1:
                    dp[x][y] = min(dp[x-1][y], dp[x][y-1]) + grid[x][y]
        return dp[n-1][m-1]

    def minPathSum(self, grid):
        
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        rowSum = [0 for j in range(m)]
        #rowSum[0] = grid[0][0]

        # for j in range(1,m):
        #     rowSum[j] = rowSum[j-1] + grid[0][j]

        for x in range(0,n):
            for y in range(m):
                if x == 0 and y >=1 :
                    rowSum[y] = rowSum[y-1] + grid[0][y]
                elif y == 0:
                    rowSum[y] = rowSum[y] + grid[x][0] #rowSum y is the value in previous row
                elif y >= 1:
                    rowSum[y] = min( rowSum[y-1], rowSum[y]) + grid[x][y]  #rowSum y-1 is already updated with current line value == x, y-1
        return rowSum[m-1]


    def minPathSum5(self, grid):
    
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])


        for x in range(n):
            for y in range(m):
                if x == 0 and y >= 1:
                    grid[x][y] = grid[x][y-1] + grid[0][y]  
                if y == 0 and x >= 1:
                    grid[x][y] = grid[x-1][y] + grid[x][0]
                if x >= 1 and y >= 1:
                    grid[x][y] = min(grid[x-1][y], grid[x][y-1]) + grid[x][y]
        return grid[n-1][m-1]
s = Solution()

print s.minPathSum([[1,1,2],[1,2,1],[1,1,1]])

