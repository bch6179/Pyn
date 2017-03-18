class Solution:

    def kSum(self, A, k, target):
        ans = [[[0 for i in range(target + 1)] for j in range(k + 1)] for K in range(len(A) + 1)]
        
        ans[0][0][0] = 1
        for I in range(len(A)):
            item = A[I]
            for J in range(target + 1):
                for K in range(k + 1):
                    tk = k - K
                    tj = target - J
                    ans[I + 1][tk][tj] = ans[I][tk][tj]
                    if tk - 1 >= 0 and tj - item >= 0:
                        ans[I + 1][tk][tj] += ans[I][tk - 1][tj - item]
        return ans[len(A)][k][target]

 解题思路

思路一： 迭代，开始时依次选择一个点，然后根据新的target值和新的数组，选择k-1个数，思路直接简单。但是存在重复计算。该算法复杂度为 Nk ,指数递增，所以在lintcode中就计算超时了。
思路二：参考网上解法，还记得我们求解一堆数，任意个数的合为N的组合个数的题吗？当时用一个一维数组来存储可以构成的数，现在我们同样用一个长度为target的数据来存储数据，存的是前j个数中选择i个数，和的构成分布，所以数据就是dp[i][j][target]，加上下届即可。
dp[i][j][v]=dp[i][j-1][v]+dp[i-1][j-1][v-A[i]]
代码

代码一

public class Solution {
    /**
     * @param A: an integer array.
     * @param k: a positive integer (k <= length(A))
     * @param target: a integer
     * @return an integer
     */
    public int kSum(int A[], int k, int target) {
        if (A.length < k || k == 0)
            return 0;

        if(k == 1){
            for(int i=0;i<A.length;i++)
                if(A[i] == target)
                    return 1;
            return 0;
        }
        else  {
            int[] B = new int[A.length - 1];
            if (A.length > 1)
                System.arraycopy(A, 1, B, 0, A.length - 1);
            return kSum(B, k - 1, target - A[0]) + kSum(B, k, target);
        }
    }
}