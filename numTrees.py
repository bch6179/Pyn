class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return n
        
        F = [1,1,2] #Mistake to initlize to 1 but later use that to sum
        F+=[0 for i in range(n-2)]  #append is to embed that in 1, 2, [2, 3],
        
        for i in range(3, n+1):
            for j in range(1,i+1):
                F[i] += F[j-1]*F[i-j]  #Mistake use n instead of i
                #   dp[i] += dp[j-1] * dp[i-j]
        return F[n]


s = Solution() 
print s.numTrees(3)