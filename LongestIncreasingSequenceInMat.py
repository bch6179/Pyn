/**
 * Find the longest increasing(increasing means one step) sequence in an
 * integer matrix in 4 directions (up down left right), return the sequence
 *
 * For Example:
 * |1 2 3 4|
 * |8 7 6 5|
 *
 * Output:
 * [1, 2, 3, 4, 5, 6, 7, 8]
 *
 * Tags: DP, DFS
 */
 
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, matrix):
            if dp[i][j]: return dp[i][j]
            for dx,dy in zip([0,-1,0,1],[-1,0,1,0]):
                if 0 <= (i+dx) <= M-1 and 0 <= (j+dy) <= N-1 and matrix[i][j]< matrix[i+dx][j+dy]:
                    dp[i][j] = max(dp[i][j], dfs(i+dx, j+dy, matrix))
            # return dp[i][j]+1 #Mistake
            dp[i][j] += 1
            return dp[i][j]
                    
        if not matrix or not matrix[0]: return 0
        M = len(matrix)
        N = len(matrix[0])
        dp =[[0]*N for i in range(M)]
        res = 0
        for i in range(M):
            for j in range(N):
                res = max(res, dfs(i,j,matrix))
        return res

We can find longest decreasing path instead, the result will be the same. Use dp to record previous results and choose the max dp value of smaller neighbors.

def longestIncreasingPath(self, matrix):
    def dfs(i, j):
        if not dp[i][j]:
            val = matrix[i][j]
            dp[i][j] = 1 + max(
                dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                dfs(i + 1, j) if i < M - 1 and val > matrix[i + 1][j] else 0,
                dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0)
        return dp[i][j]

    if not matrix or not matrix[0]: return 0
    M, N = len(matrix), len(matrix[0])
    dp = [[0] * N for i in range(M)]
    return max(dfs(x, y) for x in range(M) for y in range(N))