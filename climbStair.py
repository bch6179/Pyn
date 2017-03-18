class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n < 0: return 0
        # if n <= 1: return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        if n <= 0: return
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n < 0: return 0
        # if n <= 1: return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        if n <= 2: return n
        dp = [1,1]
        for i in range(n-2):
            dp.append(dp[-1]+dp[-2])
        return dp[-1]
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n < 0: return 0
        # if n <= 1: return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        if n <= 0: return
        dp = [0 for i in range(n+1)]
        a = 1
        b = 1
        for i in range(2, n+1):
            now = a + b
            b = a
            a = now

        return a