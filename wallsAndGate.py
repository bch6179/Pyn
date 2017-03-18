# https://leetcode.com/problems/walls-and-gates/?tab=Description

# Problem Description:

# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
# For example, given the 2D grid:
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:
#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

class Solution(object):
    def wallsAndGates(self, a):
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == 0:
                    stack = [
                        (i + 1, j, 1),
                        (i - 1, j, 1),
                        (i, j + 1, 1),
                        (i, j - 1, 1)
                    ]
                    while stack:
                        ii, jj, dist = stack.pop()
                        if ii < 0 or jj < 0 or ii >= len(a) or jj >= len(a[0]) or a[ii][jj] < dist:
                            continue
                        a[ii][jj] = dist
                        stack.append((ii + 1, jj, dist + 1))
                        stack.append((ii - 1, jj, dist + 1))
                        stack.append((ii, jj + 1, dist + 1))
                        stack.append((ii, jj - 1, dist + 1))
 def wallsAndGatesTimeOut(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """ 
       for i,row in enumerate(a):
            for j, cell in enumerate(row):
                if cell == 0:
                    stack = [(i+dx,j+dy, 1) for dx,dy in zip([1,-1,0,0], [0,0,1,-1])] 
                    while stack:
                        ii, jj, dist = stack.pop()
                        if not ( 0 <= ii < len(a) and 0 <= jj < len(a[0]) and a[ii][jj] > dist):
                            continue
                        a[ii][jj] = dist
                        for dx,dy in zip([1,-1,0,0], [0,0,1,-1]) :
                            stack.append((ii+dx,jj+dy, dist+1) )
    
       def wallsAndGates(self, rooms):
            """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        def dfs(i,j, k):
            if not (0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] > k+1):
                return 
            rooms[i][j] = min(rooms[i][j], k)
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                 
                    dfs(x,y,k+1)
            
        for i,row in enumerate(rooms):
            for j, cell in enumerate(row):
                if cell == 0:
                    dfs(i,j,0)
# Python's default sys.setrecursionlimit is too low to pass all the tests.
public void wallsAndGates(int[][] rooms) {
    for (int i = 0; i < rooms.length; i++)
        for (int j = 0; j < rooms[0].length; j++)
            if (rooms[i][j] == 0) dfs(rooms, i, j, 0);
}

private void dfs(int[][] rooms, int i, int j, int d) {
    if (i < 0 || i >= rooms.length || j < 0 || j >= rooms[0].length || rooms[i][j] < d) return;
    rooms[i][j] = d;
    dfs(rooms, i - 1, j, d + 1);
    dfs(rooms, i + 1, j, d + 1);
    dfs(rooms, i, j - 1, d + 1);
    dfs(rooms, i, j + 1, d + 1);
}