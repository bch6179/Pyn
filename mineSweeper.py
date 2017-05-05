# Maintain a todo list (stack) of squares left to reveal. For each square S to be revealed, if S contains a mine, put an X in it. If there are mines adjacent to S, then put that number of mines in it. If there are no mines adjacent to S, then put a B in it, and add adjacent squares to S that are unrevealed (in 'ME') that were not previously added (nei not in seen) to your todo list.
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        # def getNeighbors(i,j):
            
        #     for dx in [-1,1]:
        #         for dy in [-1,1]:
        #             if (dx or dy ) and 0 <= dx+i < nr and 0 <= dy+j < nc:
        #                 yield i+dx,j+dy
            
        
        click = tuple(click)
        R, C = len(board), len(board[0])
    
        def getNeighbors(r, c):
            for dr in xrange(-1, 2):
                for dc in xrange(-1, 2):
                    if (dr or dc) and 0 <= r + dr < R and 0 <= c + dc < C:
                        yield r + dr, c + dc
                    
        nr = len(board)
        nc = len(board[0])
        seen = {tuple(click)}
        q = [click]
        while q:
            r, c = q.pop()
            if board[r][c] == 'M':
               board[r][c] = 'X'
            else:
                mcount = sum(board[nr][nc] in 'MX' for nr, nc in getNeighbors(r, c))  #        sum(board[r][c] in 'MX' for x,y in getNeighbors(r,c ))
                if mcount != 0:
                    board[r][c] = str(mcount)
                else:
                    board[r][c] = 'B'
                    seen.add((r,c))
                    for nei in getNeighbors(r, c):
                        if board[nei[0]][nei[1]] == 'E':
                            q.append(nei)
                            board[nei[0]][nei[1]] = 'B'
        
        return board
                    
    def updateBoardOk(self, A, click):
        click = tuple(click)
        R, C = len(A), len(A[0])
        
        def neighbors(r, c):
            for dr in xrange(-1, 2):
                for dc in xrange(-1, 2):
                    if (dr or dc) and 0 <= r + dr < R and 0 <= c + dc < C:
                        yield r + dr, c + dc
        
        stack = [click]
        seen = {click}
        while stack:
            r, c = stack.pop()
            if A[r][c] == 'M':
                A[r][c] = 'X'
            else:
                mines_adj = sum( A[nr][nc] in 'MX' for nr, nc in neighbors(r, c) )
                if mines_adj:
                    A[r][c] = str(mines_adj)
                else:
                    A[r][c] = 'B'
                    for nei in neighbors(r, c):
                        if A[nei[0]][nei[1]] in 'E' and nei not in seen:
                            stack.append(nei)
                            seen.add(nei)
        return A
s= Solution()
board = [list("EEEEE"),list("EEMEE"),list("EEEEE"),list("EEEEE")]
print s.updateBoard(board,[3,0])
#     s is a typical Search problem, either by using DFS or BFS. Search rules:

# If click on a mine ('M'), mark it as 'X', stop further search.
# If click on an empty cell ('E'), depends on how many surrounding mine:
# 2.1 Has surrounding mine(s), mark it with number of surrounding mine(s), stop further search.
# 2.2 No surrounding mine, mark it as 'B', continue search its 8 neighbors.
# DFS solution.

# public class Solution {
#     public char[][] updateBoard(char[][] board, int[] click) {
#         int m = board.length, n = board[0].length;
#         int row = click[0], col = click[1];
        
#         if (board[row][col] == 'M') { // Mine
#             board[row][col] = 'X';
#         }
#         else { // Empty
#             // Get number of mines first.
#             int count = 0;
#             for (int i = -1; i < 2; i++) {
#                 for (int j = -1; j < 2; j++) {
#                     if (i == 0 && j == 0) continue;
#                     int r = row + i, c = col + j;
#                     if (r < 0 || r >= m || c < 0 || c < 0 || c >= n) continue;
#                     if (board[r][c] == 'M' || board[r][c] == 'X') count++;
#                 }
#             }
            
#             if (count > 0) { // If it is not a 'B', stop further DFS.
#                 board[row][col] = (char)(count + '0');
#             }
#             else { // Continue DFS to adjacent cells.
#                 board[row][col] = 'B';
#                 for (int i = -1; i < 2; i++) {
#                     for (int j = -1; j < 2; j++) {
#                         if (i == 0 && j == 0) continue;
#                         int r = row + i, c = col + j;
#                         if (r < 0 || r >= m || c < 0 || c < 0 || c >= n) continue;
#                         if (board[r][c] == 'E') updateBoard(board, new int[] {r, c});
#                     }
#                 }
#             }
#         }
        
#         return board;
#     }
# }
# BFS solution. As you can see the basic logic is almost the same as DFS. Only added a queue to facilitate BFS.

# public class Solution {
#     public char[][] updateBoard(char[][] board, int[] click) {
#         int m = board.length, n = board[0].length;
#         Queue<int[]> queue = new LinkedList<>();
#         queue.add(click);
        
#         while (!queue.isEmpty()) {
#             int[] cell = queue.poll();
#             int row = cell[0], col = cell[1];
            
#             if (board[row][col] == 'M') { // Mine
#                 board[row][col] = 'X';
#             }
#             else { // Empty
#                 // Get number of mines first.
#                 int count = 0;
#                 for (int i = -1; i < 2; i++) {
#                     for (int j = -1; j < 2; j++) {
#                         if (i == 0 && j == 0) continue;
#                         int r = row + i, c = col + j;
#                         if (r < 0 || r >= m || c < 0 || c < 0 || c >= n) continue;
#                         if (board[r][c] == 'M' || board[r][c] == 'X') count++;
#                     }
#                 }
                
#                 if (count > 0) { // If it is not a 'B', stop further DFS.
#                     board[row][col] = (char)(count + '0');
#                 }
#                 else { // Continue BFS to adjacent cells.
#                     board[row][col] = 'B';
#                     for (int i = -1; i < 2; i++) {
#                         for (int j = -1; j < 2; j++) {
#                             if (i == 0 && j == 0) continue;
#                             int r = row + i, c = col + j;
#                             if (r < 0 || r >= m || c < 0 || c < 0 || c >= n) continue;
#                             if (board[r][c] == 'E') {
#                                 queue.add(new int[] {r, c});
#                                 board[r][c] = 'B'; // Avoid to be added again.
#                             }
#                         }
#                     }
#                 }
#             }
#         }
        
#         return board;
#     }
# }