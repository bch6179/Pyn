[LeetCode]Range Sum Query 2D - Immutable
作者是 在线疯狂 发布于 2015年11月12日 在 LeetCode.
题目描述：
Given a 2D matrix, find the sum of the elements inside the rectangle defined by (row1, col1), (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:

You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
题目大意：
给定一个二维矩阵，计算从(row1, col1) 到 (row2, col2)的子矩阵的和。

测试用例见题目描述。

注意：

你可以假设矩阵不会改变
sumRegion函数会调用很多次
你可以假设row1 ≤ row2， 并且 col1 ≤ col2。
解题思路：
构造辅助二维数组sums

sums[x][y]表示从0,0到x,y的子矩阵的和

利用容斥原理，可知：

sumRange(row1, col1, row2, col2) = sums[row2][col2] + sums[row1 - 1][col1 - 1] - sums[row1 - 1][col2] - sums[row2][col1 - 1]
将辅助矩阵的行数和列数+1，可以简化对矩阵边界的处理。

Python代码：
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        self.sums = [[0] * (n + 1) for x in range(m + 1)]
        for x in range(1, m + 1):
            rowSum = 0
            for y in range(1, n + 1):
                self.sums[x][y] += rowSum + matrix[x - 1][y - 1]
                if x > 1:
                    self.sums[x][y] += self.sums[x - 1][y]
                rowSum += matrix[x - 1][y - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sums[row2 + 1][col2 + 1] + self.sums[row1][col1] \
                 - self.sums[row1][col2 + 1] - self.sums[row2 + 1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)