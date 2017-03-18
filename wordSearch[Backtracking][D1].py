# /*
#  Author:     King, wangjingui@outlook.com
#  Date:       Dec 20, 2014
#  Problem:    Word Search
#  Difficulty: Easy
#  Source:     https://oj.leetcode.com/problems/word-search/
#  Notes:
#  Given a 2D board and a word, find if the word exists in the grid.
#  The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are
#  those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#  For example,
#  Given board =
#  [
#   ["ABCE"],
#   ["SFCS"],
#   ["ADEE"]
#  ]
#  word = "ABCCED", -> returns true,
#  word = "SEE", -> returns true,
#  word = "ABCB", -> returns false.

#  Solution: DFS.
#  */
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #search in 4 direction
        #mark visited
        #back tracking until all word 
        
        def dfs(pos, i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            
            if not visited[i][j] and word[pos] == board[i][j]:
                if pos == len(word)-1:
                    return True
                else:
                    visited[i][j] = True #Mistake forget the visited and not test (["aa"], "aaa"
                    if dfs(pos+1, i, j+1) or dfs(pos+1, i, j-1) or dfs(pos+1, i+1, j) or dfs(pos+1, i-1, j):
                        return True
                    else:
                        visited[i][j] = False
            return False
        
        if word == []: return True
        
        n = len(board)
        m = len(board[0])
        visited = [[False for j in range(m)] for i in range(n)]
        for i in range(0, n):
            for j in range(0, m):
                if dfs(0, i , j):
                    return True
                    
        return False
                

s = Solution() 
print s.exist(["aa"], "aaa")
print s.exist([["aa"]], "aaa")
