import functools
import operator
class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        res = [[] for x in range(numRows)]
        row, step = 0, 1
        for c in s:
            res[row] += c
            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1
            row += step
        print(res)
        return ''.join(functools.reduce(operator.add, res))

s = Solution()
print(s.convert("paypayl", 3))