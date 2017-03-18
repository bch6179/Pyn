class Solution(object):
    def isValidSudokuImp(self, board):
        row = set()
        col = set()
        rec = set()

        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c != '.':
                    if (i,c) not in row and (j,c) not  in col and  (i/3,j/3,c) not in rec:
                        row.add((i,c))
                    
                        col.add((j,c))
                        #   Mistake not calcu in place
                        rec.add((i/3,j/3,c))
                    else:
                        return False
        return True
s= Solution()
ins = ["....5..1.",
       ".4.3.....",
       ".....3..1",
       "8......2.",
       "..2.7....",
       ".15......",
       ".....2...",
       ".2.9.....",
       "..4......"]

print s.isValidSudokuImp(ins)

#     def isValidSudoku1(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: bool
#         """
#         seen = []
#         for i,row in enumerate(board):
#             for j, c in enumerate(row):
#                 if c != '.':
#                     seen+=[(i,c),(c,j),(i/3,j/3,c)]
#         return len(seen) == len(set(seen))
#     def isValidSudoku(self, board):
         
#         def helper(board, x1,y1, x2,y2):
#             s = set()
#             for i in range(x1,x2):
#                 for j in range(y1, y2+1): #Mistake range(3,3) never will run here
#                     val = board[i][j]
#                     if val != '.':
#                         if val not in s:
#                             s.add(val)
#                         else: 
#                             return False
#             return True
        
#         for i in range(0,9):
#             if not helper(board, i,0, i+1,9): return False #Mistake
#             if not helper(board, 0, i, 9, i+1): return False
#         for i in range(0,3):
#             for j in range(0,3):
#                 if not helper(board, i*3, j*3, i*3+3, j*3+3): return False #Mistake not ...

#         #          # 0 => 0, 1 => 3, 2 => 6
#         # # 3 => 0, 4 => 3, 5 => 6
#         # # 6 => 0, 7 => 3, 8 => 6
#         # x = (i % 3) * 3
#         # # 0 => 0, 1 => 0, 2 => 0
#         # # 3 => 3, 4 => 3, 5 => 3
#         # # 6 => 6, 7 => 6, 8 => 6
#         # y = i / 3 * 3
#         # if not self.is_partially_valid(board, x, x + 3, y, y + 3): return False
#         return True
# s = Solution() 
# print s.isValidSudoku(["..4...63.",
#                        ".........",
#                        "5......9.",
#                        "...56....",
#                        "4.3.....1",
#                        "...7.....",
#                        "...5.....",
#                        ".........",
#                        "........."])
# print s.isValidSudoku([".87654321",
#                       "2........",
#                       "3........",
#                       "4........",
#                       "5........",
#                       "6........",
#                       "7........","8........","9........"])        
# class Solution(object):
# def isValidSudoku(self, board):
#     """
#     :type board: List[List[str]]
#     :rtype: bool
#     """

#     map_row = [{} for _ in xrange(9)]
#     map_col = [{} for _ in xrange(9)]
#     map_cell = [[{} for _ in xrange(3)] for __ in xrange(3)]
#     for i in xrange(9):
#         for j in xrange(9):
#             char = board[i][j]
#             if char == '.': continue
#             if char in map_row[i]: return False
#             else: map_row[i][char] = [i,j]
#             if char in map_col[j]: return False
#             else: map_col[j][char] = [i,j]
#             if char in map_cell[i/3][j/3]: return False
#             else: map_cell[i/3][j/3][char] = [i,j]
#     return True
#      bool isValidSudoku(vector<vector<char>>& board) {
#     vector<short> col(9, 0);
#     vector<short> block(9, 0);
#     vector<short> row(9, 0);
#     for (int i = 0; i < 9; i++)
#      for (int j = 0; j < 9; j++) {
#          if (board[i][j] != '.') {
#              int idx = 1 << (board[i][j] - '0');
#              if (row[i] & idx || col[j] & idx || block[i/3 * 3 + j / 3] & idx)
#                 return false;
#             row[i] |= idx;
#             col[j] |= idx;
#             block[i/3 * 3 + j/3] |= idx;
#          }
#      }
#      return true;
#   }

# package com.epi;

# public class SudokuCheck {
#   // @include
#   // Check if a partially filled matrix has any conflicts.
#   public static boolean isValidSudoku(int[][] A) {
#     // Check row constraints.
#     for (int i = 0; i < A.length; ++i) {
#       if (hasDuplicate(A, i, i + 1, 0, A.length, A.length)) {
#         return false;
#       }
#     }

#     // Check column constraints.
#     for (int j = 0; j < A.length; ++j) {
#       if (hasDuplicate(A, 0, A.length, j, j + 1, A.length)) {
#         return false;
#       }
#     }

#     // Check region constraints.
#     int regionSize = (int) Math.sqrt(A.length);
#     for (int I = 0; I < regionSize; ++I) {
#       for (int J = 0; J < regionSize; ++J) {
#         if (hasDuplicate(A, regionSize * I, regionSize * (I + 1),
#                          regionSize * J, regionSize * (J + 1), A.length)) {
#           return false;
#         }
#       }
#     }
#     return true;
#   }

#   // Return true if subarray A[startRow : endRow - 1][startCol : endCol - 1]
#   // contains any duplicates in [1 : numElements]; otherwise return false.
#   private static boolean hasDuplicate(int[][] A, int startRow, int endRow,
#                                       int startCol, int endCol,
#                                       int numElements) {
#     boolean[] isPresent = new boolean[numElements + 1];
#     for (int i = startRow; i < endRow; ++i) {
#       for (int j = startCol; j < endCol; ++j) {
#         if (A[i][j] != 0 && isPresent[A[i][j]]) {
#           return true;
#         }
#         isPresent[A[i][j]] = true;
#       }
#     }
#     return false;
#   }
#   // @exclude
# }
# Valid Sudoku
# // use bit mapping, be careful about operator precedence
# // 56 milli secs pass Judge Large

# class Solution {
#   public:
#   bool isValidSudoku(vector<vector<char> > &board) {
#     // use bit map to mark the apperance of numbers
#     vector<int> row(9, 0);
#     vector<int> col(9, 0);
#     vector<vector<int> > box(3, vector<int>(3, 0));

#     for(int i=0; i<9; ++i)
#       for(int j=0; j<9; ++j)
#         if(board[i][j] != '.') {
#           int digit = board[i][j] - '1'; // convert to 0 ~ 8
#           // check if there is duplicate choice
#           if((row[i] & (1<<digit)) != 0) return false;
#           if((col[j] & (1<<digit)) != 0) return false;
#           if((box[i/3][j/3] & (1<<digit)) != 0) return false;
#           // mark the bit for the appeared number
#           row[i] |= (1<<digit);
#           col[j] |= (1<<digit);
#           box[i/3][j/3] |= (1<<digit);
#         }
#     return true; // return true if no conflict found
#   }
# };