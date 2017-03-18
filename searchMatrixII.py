https://leetcode.com/problems/search-a-2d-matrix-ii/?tab=Description
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.


l, the idea is to search from the top-right element and then reduce the range for further searching by comparisons between target and the current element.

Let's take the matrix in the problem statement as an example.

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19], 
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
] 
Suppose we want to search for 12. We first initialize r = 0 and c = 4. We compare 12 with matrix[r][c] = matrix[0][4] = 15 and 12 < 15, so 12 cannot appear in the column of 15 since all elements below 15 are not less than 15. Thus, we decrease c by 1 and reduce the search range by a column. Now we compare 12 with matrix[r][c] = matrix[0][3] = 11 and 12 > 11, so 12 cannot appear in the row of 11 since all elements left to 11 are not greater than 11. Thus, we increase r by 1 and reduce the search range by a row. Then we reach matrix[1][3] = 12 = target and we are done (return true). If we have moved beyond the matrix and have not found the target, return false.

Putting these together, we will have the following short codes.




class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        m, n, r, c = len(matrix), len(matrix[0]), 0, n - 1
        while r < m and c >= 0:
            if matrix[r][c] == target:
                return True
            if matrix[r][c] > target:
                c -= 1
            else: 
                r += 1
        return False