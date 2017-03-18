
# https://leetcode.com/problems/bomb-enemy/?tab=Description


# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.

# Example:
# For the given grid

# 0 E 0 0
# E 0 W E
# 0 E 0 0

# return 3. (Placing a bomb at (1,1) kills 3 enemies)

# #it will recalculate sub row and col after walls on the fly

# Because I go through the matrix row by row. So at any point I'm only working on one row (the current one) but working on all columns (in round-robin fashion).

# streak:  row and another vertical col

# he algorithm is O(mn). Let's say we are currently at one position, the worst case is that we need to traverse both its row and its column (i.e., execute the two inner for loops), but that also means for other positions that belong to the same row/column, you don't need to do the inner for loop any more. You can interpret this process as amortization.

# The space complexity can be O(min(m, n)).

# hly O(3mn), one to iterate through elements, one to scan rows, one to scan columns
# 361. Bomb Enemy Add to List
# Description  Submission  Solutions
# Total Accepted: 12617 Total Submissions: 32928 Difficulty: Medium Contributors: Admin
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
# Note that you can only put the bomb at an empty cell.

# Example:
# For the given grid

# 0 E 0 0
# E 0 W E
# 0 E 0 0

# return 3. (Placing a bomb at (1,1) kills 3 enemies)

# his solution is O(mn).

class Solution(object):
    def maxKilledEnemiesMyTimeout(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def BFSCount(i,j):
            for x,y in [(-1,0),(1,0), (0,-1),(0,1)]:
                for k in range(1,max(m,n)):
                    nx = i+x*k
                    ny = j+y*k
                    if 0 <= nx < m and 0 <= ny< n :
                        if grid[nx][ny] == '0':
                            count[nx][ny] += 1
                        if grid[nx][ny] == 'W':
                            break
        if len(grid) == 0 or len(grid[0]) == 0: return 0
        m = len(grid)
        n = len(grid[0])
        count = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'E':
                    BFSCount(i,j)
    
                            
        return max([max(row) for row in count])
    def maxKilledEnemiesOri(self, grid):
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        result = 0
        colhits = [0] * n
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if j == 0 or row[j-1] == 'W':
                    rowhits = 0
                    k = j
                    while k < n and row[k] != 'W':
                        rowhits += row[k] == 'E'
                        k += 1
                if i == 0 or grid[i-1][j] == 'W':
                    colhits[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        colhits[j] += grid[k][j] == 'E'
                        k += 1
                if cell == '0':
                    result = max(result, rowhits + colhits[j])
        return result
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid: 
            return 0
        m = len(grid)
        n = len(grid[0])
        coles = [0 for _ in range(n)]
        res = 0
        for i,row in enumerate(grid):
            for j,cell in enumerate(row):
                if j == 0 or row[j-1] == 'W':
                    rowes = 0
                    k = j
                    while k < n and row[k] != 'W': #Mistake not cell
                        rowes += row[k] == 'E'
                        k += 1                
                if i == 0 or grid[i-1][j] == 'W':  #Mistake should not be  grid[j][i-1]
                    coles[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W': #Mistake not cell
                        coles[j] += grid[k][j] == 'E'
                        k += 1
                if cell == '0':
                    res = max(res, rowes + coles[j])
                    
            return res  #Mistake here indent
        
s= Solution()
grid= ["0E00",
       "E0WE",
       "0E00"]
print s.maxKilledEnemies(grid)