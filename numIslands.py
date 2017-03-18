import collections
class Solution(object):
    def numIslands(self, grid):
        def bfs(i,j):
         
            q = collections.deque([(i,j)])
            
            while q:
                x,y = q.popleft()
                visited[x][y] = True

                for dx,dy in zip((1,-1,0,0),(0,0,1,-1)):
                    if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and not visited[x+dx][y+dy] and grid[x+dx][y+dy] == '1':
                        q.append([x+dx, y+dy])
            
        
        visited = [ [False for j in range(len(grid[0]))] for i in range(len(grid)) ]
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(i,j)
                    count += 1
                    
        return count  
    def numIslandsdfs(self, grid):
      
        def dfs(i,j):
            
            grid[i][j] = '0'
            
            for dx,dy in zip((1,-1,0,0), (0,0,1,-1)):
                if i+dx < 0 or i+dx >= len(grid) or j+dy < 0 or j+dy >= len(grid[0]) or grid[i+dx][j+dy] == '0':
                    continue
                dfs(i+dx, j+dy)
        count  = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        return count
    def numIslandsBFS(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        import collections
        
        def bfs(i,j):
            q = collections.deque([(i,j)])
            visited[i][j] = True
            #grid[i][j] = '0'
            while q:
                x,y = q.popleft()
                visited[x][y] = True
               
                for nx, ny in [(x+1,y), (x-1,y), (x,y+1) ,(x,y-1)]:
                    if   0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1' and not visited[nx][ny]:
                        q.append((nx,ny))
                        #visited[nx][ny] = True
                        #grid[nx][ny] = '0'

                        
                
        if len(grid)==0 or len(grid[0]) == 0: return 0
        visited = [[False]*len(grid[0])]*len(grid)
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if  grid[i][j] == '1' and not visited[i][j]:
                    bfs(i,j)
                    count += 1
        return count
    
s= Solution()
input3 = ["111","010"]
input =  ['1011',
      #    "10101",
          '1110']
input2 = [list("11110"),list("11010"),list("11000"),list("00000")]
print s.numIslands(input2)

#  StefanPochmann  
# Reputation:  13,541
# Sink and count the islands.

# Python Solution

# def numIslands(self, grid):
#     def sink(i, j):
#         if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
#             grid[i][j] = '0'
#             map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
#             return 1
#         return 0
#     return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

#     public int numIslands(char[][] grid) {
#     int count = 0;
#     n = grid.length;
#     if (n == 0) return 0;
#     m = grid[0].length;
#     for (int i = 0; i < n; i++){
#         for (int j = 0; j < m; j++)
#             if (grid[i][j] == '1') {
#                 DFSMarking(grid, i, j);
#                 ++count;
#             }
#     }    
#     return count;
# }

# private void DFSMarking(char[][] grid, int i, int j) {
#     if (i < 0 || j < 0 || i >= n || j >= m || grid[i][j] != '1') return;
#     grid[i][j] = '0';
#     DFSMarking(grid, i + 1, j);
#     DFSMarking(grid, i - 1, j);
#     DFSMarking(grid, i, j + 1);
#     DFSMarking(grid, i, j - 1);
# }