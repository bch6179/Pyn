#       class Solution(object):
#           he game ends when a person can no longer make a move and therefore the other person will be the winner.

# Write a function to compute all possible states of the string after one valid move.
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        moves, n, s = [], len(s), list(s)
        for i in xrange(n - 1):
            if s[i] == s[i + 1] == '+':
                s[i] = s[i + 1] = '-'
                moves += ''.join(s),
                s[i] = s[i + 1] = '+' 
        return moves

        he idea is quite straightforward: just traverse s and each time when we see two consecutive+s, convert them to -s and add the resulting string to the final result moves. But remember to recover the string after that.

        Well I also try to write a Python solution since Python supports sequential comparisons, which is quite convenient. But Python does not support modifying a string and I can only use list and join to do the same thing.