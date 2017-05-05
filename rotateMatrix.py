class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate1(self, matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

                # e most pythonic solution is a simple one-liner using [::-1] to flip the matrix upside down and then zip to transpose it. It assigns the result back into A, so it's "in-place" in a sense and the OJ accepts it as such, though some people might not.


#     def rotate(self, A):
#         A[:] = zip(*A[::-1])
# public void rotate(int[][] matrix) {
#     int n = matrix.length;
#     int tmp;
#     for(int i = 0; i < Math.ceil((double)n/2); i++){
#       for(int j = i; j < n - 1 - i; j ++){
#         tmp = matrix[i][j];
#         matrix[i][j] = matrix[n-1-j][i];
#         matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
#         matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
#         matrix[j][n-1-i] = tmp;
#       }
#     }
#   }
# A 100% in-place solution. It even reads and writes each matrix element only once and doesn't even use an extra temporary variable to hold them. It walks over the "top-left quadrant" of the matrix and directly rotates each element with the three corresponding elements in the other three quadrants. Note that I'm moving the four elements in parallel and that [~i] is way nicer than [n-1-i].
    def rotate2(self, A): # rotate along each quadrant # circle in for-loop # for odd handling n- n/2, like 5, 0,1,2 cols
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        n = len(A)
        for i in range(n/2):
            for j in range(n-n/2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]
    def rotate(self, A):
        n = len(A)
        for i in range(n/2): 
            for j in range(i, n-1-i):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j]
s = Solution()
s.rotate()
                        #  0,1 <- 2,0
                        #  1,1 < 2,1  above conclude 