#  consider all possible choices of final balloon to pop
#             int bestCoins = 0;
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note: 
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
   
class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in xrange(n)]

        for k in xrange(2, n):
            for left in xrange(0, n - k):
                right = left + k
                for i in xrange(left + 1,right): # i as final
                    dp[left][right] = max(dp[left][right],
                        nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]
s = Solution() 
print s.maxCoins([3, 1, 5, 8])

class Solution(object):
 
        
    def maxCoinsDFS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(nums, mem, l, r):
            if l+1== r:
                return 0
            if mem[l][r] >0: 
                return mem[l][r]
            res = 0
            for i in range(l+1, r):
                res = max(res, nums[l]*nums[i]*nums[r] + dfs(nums, mem, l, i) + dfs(nums,mem,i, r))
            mem[l][r] = res
            
            return res
        if not nums or len(nums)==0: return 0
        
        nums = [1] + [i for i in nums if i > 0] + [1]
        n = len(nums)
        mem = [[-1] * n for i in range(n)]
        
   
        

            
        dfs(nums, mem, 0, n-1)
        return mem[0][n-1]
            
#Mistake
# dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + nums[left][i] + nums[i][right]) 
# dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])

# Knote:
# backtracking->n!->subproblems not rely , with DP or mem c(n,k)*k worse than n^2 -> d&d : first or the last nums[i-1]*nums[i]*nums[i+1] for the last we have nums[-1]*nums[i]*nums[n]
#  ans = Math.max(ans, nums[left] * nums[i] * nums[right]       + burst(memo, nums, left, i) + burst(memo, nums, i, right))
# mistake:  left right is dummy border , always there , not included by the subproblem , or not diminished after solving the subproblems
#  from this POV, the two subsections are divided : result smaller since left could also be burst
#should be i as the border of left and right sections, i will be the remaining togerther with l and r
# 参考peisi的答案：https://leetcode.com/discuss/72216/share-some-analysis-and-explanations

# 以最后被爆破的气球m为界限，把数组分为左右两个子区域

# 状态转移方程：

# dp[l][r] = max(dp[l][r], nums[l] * nums[m] * nums[r] + dp[l][m] + dp[m][r])
# dp[l][r]表示扎破(l, r)范围内所有气球获得的最大硬币数，不含边界；

# l与r的跨度k从2开始逐渐增大；

# 三重循环依次枚举范围跨度k，左边界l，中点m；右边界r = l + k；

# 状态转移方程在形式上有点类似于Floyd最短路算法。

# Java代码：
# This is the kind of problem we use dynamic programming. WHY? it's very challenging to figure out what's the pattern of optimal burst order. In fact, there's no clear rule that makes sense. Shall we burst the balloon with maximum coins? Or shall we burst the one with least. This is the time we introduce Dynamic Programming, as we want to solve the big problem from small subproblem. It is clear that the amount of coins you gain relies on your previous steps. This is a clear signal of using DP.

# The hard part is to define the subproblem. Think out what is clear in this problem? Let's scale this problem down. What is the fact you know for sure? Say if the array has only 1 balloon. The maximum coin would be the coin inside this ballon. This is the starting point! So let's move on to array with 2 balloons. Here, we have 2 cases, which of the balloon is the last one. The last one times the coins in boundary is the gain we get in the end. That is to say, last balloon is the key. Since we don't know the pattern of optimal. We just blindly iterate each balloon and check what's total gain if it's the last ballon.

# Let's use dp[i][j] to denote maximum gain from balloon range i to j. We try out each balloon as last burst in this range. Then the subproblem relation would be:

# foreach k in j to i:
# dp[j][i] = max(array[j-1]*array[k]*array[i+1] + dp[j][k-1] + dp[k+1][i], dp[j][i]);

# public class Solution {
# public int maxCoins(int[] nums) {
#     // Extend list with head and tail (both are 1), index starts at 1
#     int array[] = new int[nums.length + 2];
#     array[0] = 1;
#     array[array.length-1] = 1;
#     for (int i = 0; i < nums.length; i++) {
#         array[i+1] = nums[i];
#     }

#     // Initialize DP arrays, 1 index based
#     int dp[][] = new int[array.length][array.length]; //dp[i][j] stands for max coins at i step, burst j
#     for (int i =0; i < array.length; i++) {
#         for (int j = 0; j < array.length; j++) {
#             dp[i][j] = 0;
#         }
#     }

#     for (int i=1; i< array.length-1; i++) {
#         for (int j=i; j >=1; j--) {
#             // k as last
#             for (int k=j; k <= i; k++) {
#                 dp[j][i] = Math.max(array[j-1]*array[k]*array[i+1] + dp[j][k-1] + dp[k+1][i], dp[j][i]);
#             }
#         }
#     }

#     return dp[1][array.length-2];
# }
#     // build up from shorter ranges to longer ranges
#     for (int len = 1; len <= N; ++len) {
#         for (int start = 1; start <= N - len + 1; ++start) {
#             int end = start + len - 1;
#             // calculate the max # of coins that can be obtained by
#             // popping balloons only in the range [start,end].
#             // consider all possible choices of final balloon to pop
#             int bestCoins = 0;
#             for (int final = start; final <= end; ++final) {
#                 int coins = rangeValues[start][final-1] + rangeValues[final+1][end]; // coins from popping subranges
#                 coins += nums[start-1] * nums[final] * nums[end+1]; // coins from final pop
#                 if (coins > bestCoins) bestCoins = coins;
#             }
#             rangeValues[start][end] = bestCoins;
#         }
#     }
#     return rangeValues[1][N];
# }


# int maxCoins(vector<int>& nums) {
#     int N = nums.size();
#     nums.insert(nums.begin(), 1);
#     nums.insert(nums.end(), 1);

#     // rangeValues[i][j] is the maximum # of coins that can be obtained
#     // by popping balloons only in the range [i,j]
#     vector<vector<int>> rangeValues(nums.size(), vector<int>(nums.size(), 0));
    

# See here for a better view

# Be Naive First

# When I first get this problem, it is far from dynamic programming to me. I started with the most naive idea the backtracking.

# We have n balloons to burst, which mean we have n steps in the game. In the i th step we have n-i balloons to burst, i = 0~n-1. Therefore we are looking at an algorithm of O(n!). Well, it is slow, probably works for n < 12 only.

# Of course this is not the point to implement it. We need to identify the redundant works we did in it and try to optimize.

# Well, we can find that for any balloons left the maxCoins does not depends on the balloons already bursted. This indicate that we can use memorization (top down) or dynamic programming (bottom up) for all the cases from small numbers of balloon until n balloons. How many cases are there? For k balloons there are C(n, k) cases and for each case it need to scan the k balloons to compare. The sum is quite big still. It is better than O(n!) but worse than O(2^n).

# Better idea

# We then think can we apply the divide and conquer technique? After all there seems to be many self similar sub problems from the previous analysis.

# Well, the nature way to divide the problem is burst one balloon and separate the balloons into 2 sub sections one on the left and one one the right. However, in this problem the left and right become adjacent and have effects on the maxCoins in the future.

# Then another interesting idea come up. Which is quite often seen in dp problem analysis. That is reverse thinking. Like I said the coins you get for a balloon does not depend on the balloons already burst. Therefore
# instead of divide the problem by the first balloon to burst, we divide the problem by the last balloon to burst.

# Why is that? Because only the first and last balloons we are sure of their adjacent balloons before hand!

# For the first we have nums[i-1]*nums[i]*nums[i+1] for the last we have nums[0]*nums[i]*nums[n].

# OK. Think about n balloons if i is the last one to burst, what now?

# We can see that the balloons is again separated into 2 sections. But this time since the balloon i is the last balloon of all to burst, the left and right section now has well defined boundary and do not affect each other! Therefore we can do either recursive method with memoization or dp.

# Final

# Here comes the final solutions. Note that we put 2 balloons with 1 as boundaries and also burst all the zero balloons in the first round since they won't give any coins.
# The algorithm runs in O(n^3) which can be easily seen from the 3 loops in dp solution.

# Java D&C with Memoization

# public int maxCoins(int[] iNums) {
#     int[] nums = new int[iNums.length + 2];
#     int n = 1;
#     for (int x : iNums) if (x > 0) nums[n++] = x;
#     nums[0] = nums[n++] = 1;


#     int[][] memo = new int[n][n];
#     return burst(memo, nums, 0, n - 1);
# }

# public int burst(int[][] memo, int[] nums, int left, int right) {
#     if (left + 1 == right) return 0;
#     if (memo[left][right] > 0) return memo[left][right];
#     int ans = 0;
#     for (int i = left + 1; i < right; ++i)
#         ans = Math.max(ans, nums[left] * nums[i] * nums[right] 
#         + burst(memo, nums, left, i) + burst(memo, nums, i, right));
#     memo[left][right] = ans;
#     return ans;
# }
# // 12 ms
# Java DP

# public int maxCoins(int[] iNums) {
#     int[] nums = new int[iNums.length + 2];
#     int n = 1;
#     for (int x : iNums) if (x > 0) nums[n++] = x;
#     nums[0] = nums[n++] = 1;


#     int[][] dp = new int[n][n];
#     for (int k = 2; k < n; ++k)
#         for (int left = 0; left < n - k; ++left) {
#             int right = left + k;
#             for (int i = left + 1; i < right; ++i)
#                 dp[left][right] = Math.max(dp[left][right], 
#                 nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]);
#         }

#     return dp[0][n - 1];
# }
# // 17 ms

# Python DP



# 528ms