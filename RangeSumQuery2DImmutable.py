LeetCode] Range Sum Query 2D - Mutable 二维区域和检索 - 可变
 

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).


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
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
 

这道题让我们求二维区域和检索，而且告诉我们数组中的值可能变化，这是之前那道Range Sum Query 2D - Immutable的拓展，由于我们之前做过一维数组的可变和不可变的情况Range Sum Query - Mutable和Range Sum Query - Immutable，那么为了能够通过OJ，我们还是需要用到树状数组Binary Indexed Tree(参见Range Sum Query - Mutable)，其查询和修改的复杂度均为O(logn)，那么我们还是要建立树状数组，我们根据数组中的每一个位置，建立一个二维的树状数组，然后还需要一个getSum函数，以便求得从(0, 0)到(i, j)的区间的数字和，然后在求某一个区间和时，就利用其四个顶点的区间和关系可以快速求出，参见代码如下：

 

解法一：

复制代码
// Binary Indexed Tree 
class NumMatrix {
public:
    NumMatrix(vector<vector<int>> &matrix) {
        if (matrix.empty() || matrix[0].empty()) return;
        mat.resize(matrix.size() + 1, vector<int>(matrix[0].size() + 1, 0));
        bit.resize(matrix.size() + 1, vector<int>(matrix[0].size() + 1, 0));
        for (int i = 0; i < matrix.size(); ++i) {
            for (int j = 0; j < matrix[i].size(); ++j) {
                update(i, j, matrix[i][j]);
            }
        }
    }

    void update(int row, int col, int val) {
        int diff = val - mat[row + 1][col + 1];
        for (int i = row + 1; i < mat.size(); i += i&-i) {
            for (int j = col + 1; j < mat[i].size(); j += j&-j) {
                bit[i][j] += diff;
            }
        }
        mat[row + 1][col + 1] = val;
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        return getSum(row2 + 1, col2 + 1) - getSum(row1, col2 + 1) - getSum(row2 + 1, col1) + getSum(row1, col1);
    }
    
    int getSum(int row, int col) {
        int res = 0;
        for (int i = row; i > 0; i -= i&-i) {
            for (int j = col; j > 0; j -= j&-j) {
                res += bit[i][j];
            }
        }
        return res;
    } 
    
private:
    vector<vector<int>> mat;
    vector<vector<int>> bit;
};
复制代码

 

我在网上还看到了另一种解法，这种解法并没有用到树状数组，而是利用了列之和，所谓列之和，就是(i, j)就是(0, j) + (1, j) + ... + (i, j) 之和，相当于把很多个一维的区间之和拼到了一起，那么我们在构造函数中需要建立起这样一个列之和矩阵，然后再更新某一个位置时，我们只需要将该列中改变的位置下面的所有数字更新一下即可，而在求某个区间和时，只要将相差的各列中对应的起始和结束的行上的值的差值累加起来即可，参见代码如下：

 

解法二：

复制代码
// Column Sum
class NumMatrix {
public:
    NumMatrix(vector<vector<int>> &matrix) {
        if (matrix.empty() || matrix[0].empty()) return;
        mat = matrix;
        colSum.resize(matrix.size() + 1, vector<int>(matrix[0].size(), 0));
        for (int i = 1; i < colSum.size(); ++i) {
            for (int j = 0; j < colSum[0].size(); ++j) {
                colSum[i][j] = colSum[i - 1][j] + matrix[i - 1][j];
            }
        }
    }

    void update(int row, int col, int val) {
        for (int i = row + 1; i < colSum.size(); ++i) {
            colSum[i][col] += val - mat[row][col];
        }
        mat[row][col] = val;
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        int res = 0;
        for (int j = col1; j <= col2; ++j) {
            res += colSum[row2 + 1][j] - colSum[row1][j];
        } 
        return res;
    }

private:
    vector<vector<int>> mat;
    vector<vector<int>> colSum;
};
