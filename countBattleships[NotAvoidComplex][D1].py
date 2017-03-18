class Solution(object):
    #    if . : continue
    #         #     if i j-1 == X or i-1 j == X : continue
    #         # otherwise count
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        len1 = len(board)
        if len1 == 0:
            return 0;
        len2 = len(board[0])
        ans = 0 
        for i in range(0, len1):
            for j in range(0,len2):
                if board[i][j] == 'X' and ( i == 0 or board[i-1][j] == '.' )and (j == 0 or board[i][j-1] == '.'):
                    ans += 1
        return ans