Home   OJ   Sparse Matrix Multiplication   Python solution with detailed explanation 
New users please read the instructions to format your code properly. Discuss is a place to post interview questions or share solutions / ask questions related to OJ problems.
Python solution with detailed explanation

0
G gabbu 
Reputation:  72
Solution

Sparse Matrix Multiplication https://leetcode.com/problems/sparse-matrix-multiplication/

Algorithm

Preprocess matrix A to produce a dictionary cache such that cache[i] = [j1,j2,j3] such that A[i,j1] is not zero. Then use this cache while doing dot product of row of A with column of B so that only non zero values of A are multiplied.
from collections import defaultdict
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        M,N = len(A), len(A[0])
        cache = defaultdict(list)
        for i in range(M):
            for j in range(N):
                if A[i][j] != 0:
                    cache[i].append(j)
        
        K = len(B[0])
        result = [[0]*K for _ in range(M)]
        for i in range(M):
            for k in range(K):
                val = 0
                for col in cache[i]:
                    val = val + A[i][col]*B[col][k]
                result[i][k] = val
        return result
Optimized Solution

Merge construction of cache with multiplication.
from collections import defaultdict
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        M, N, K = len(A), len(A[0]), len(B[0])
        result, cache = [[0]*K for _ in range(M)], defaultdict(list)
        for i in range(M):
            for j in range(N):
                if A[i][j] != 0:
                    cache[i].append(j)
            for k in range(K):
                val = 0
                for col in cache[i]:
                    val = val + A[i][col]*B[col][k]
                result[i][k] = val
        return result

blic class Solution {
    public int[][] multiply(int[][] A, int[][] B) {
        int m = A.length, n = A[0].length, nB = B[0].length;
        int[][] C = new int[m][nB];

        for(int i = 0; i < m; i++) {
            for(int k = 0; k < n; k++) {
                if (A[i][k] != 0) {
                    for (int j = 0; j < nB; j++) {
                        if (B[k][j] != 0) C[i][j] += A[i][k] * B[k][j];
                    }
                }
            }
        }
        return C;   
    }
}
The followings is the original 75ms solution:

The idea is derived from a CMU lecture.

A sparse matrix can be represented as a sequence of rows, each of which is a sequence of (column-number, value) pairs of the nonzero values in the row.
So let's create a non-zero array for A, and do multiplication on B.

Hope it helps!

public int[][] multiply(int[][] A, int[][] B) {
    int m = A.length, n = A[0].length, nB = B[0].length;
    int[][] result = new int[m][nB];

    List[] indexA = new List[m];
    for(int i = 0; i < m; i++) {
        List<Integer> numsA = new ArrayList<>();
        for(int j = 0; j < n; j++) {
            if(A[i][j] != 0){
                numsA.add(j); 
                numsA.add(A[i][j]);
            }
        }
        indexA[i] = numsA;
    }

    for(int i = 0; i < m; i++) {
        List<Integer> numsA = indexA[i];
        for(int p = 0; p < numsA.size() - 1; p += 2) {
            int colA = numsA.get(p);
            int valA = numsA.get(p + 1);
            for(int j = 0; j < nB; j ++) {
                int valB = B[colA][j];
                result[i][j] +=valA * valB;

                def multiply(self, A, B):
        cols = [[(j, b) for j, b in enumerate(col) if b]
            for col in zip(*B)]
    return [[sum(row[j]*b for j, b in col)
             for col in cols]
            for row in A]