解题思路：
动态规划（Dynamic Programming）
class Solution(object):
    def rob(self, nums):
        n =  len(nums)
        
        b= 0
        a = 0
        res = 0
        for i in range(1, n+1):
            res = max(a, b+nums[i-1])
            b = a
            a = res
        return res
    robii:
    max(rob(nums, 0, n-1), rob(nums,1,n))


  
    def rob(self, nums, lo, hi):
        n =  len(nums)
        
        b= 0
        a = 0
        res = 0
        for i in range(lo, hi+1):
            res = max(a, b+nums[lo])
            b = a #pre not robbed
            a = res # pre robed
        return res

      class Solution(object):
    def rob(self, nums):
        def _rob(nums):
            a, b = 0, 0
            for i in xrange(len(nums)):
                a, b = b, max(a + nums[i], b)   
            return b
        a, b = _rob(nums[:-1]), _rob(nums[1:])
        return max(a, b) if len(nums) is not 1 else nums[0]
    def rob2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #  6 4 3 10 2
        #i 0 1 2
        #  6 6 
        n = len(nums)
        
        if n == 0: return 0
         
        F = [0 for i in range(n+1)]
        
        F[1] = nums[0] #mistake nums[1] for only one digit
        
        for i in range(2, n+1):
            F[i] = max(F[i-1] , F[i-2]+nums[i-1])
            
        return F[n]

状态转移方程：

dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])

其中，dp[i]表示打劫到第i间房屋时累计取得的金钱最大值。

时间复杂度O(n)，空间复杂度O(n)

Python代码：
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        size = len(num)
        dp = [0] * (size + 1)
        if size:
            dp[1] = num[0]
        for i in range(2, size + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])
        return dp[size]

观察可知，上述代码的空间复杂度可以进一步化简为O(1)：

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        size = len(num)
        odd, even = 0, 0
        for i in range(size):
            if i % 2:
                odd = max(odd + num[i], even)
            else:
                even = max(even + num[i], odd)
        return max(odd, even)