class Solution(object):
    def __init__(self):
        self.res = 1 << 31 - 1
    def minCut1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1: return 0
        self.dfs(s, 0, 0)
        return self.res
    

        
    def dfs(self, s, pos,  cut):
        if pos == len(s)-1:
            self.res = min(self.res, cut)
            return
        for i in range(pos+1, len(s)):
            if self.isPalindrome(s[pos:i]):
                self.dfs(s, i, cut+1)
                
    def isPalindrome(self, s):
        return s == s[::-1]
    # @param s, a string
    # @return an integer
    # @dfs time out
    # @dp is how many palindromes in the word
    def minCut3(self, s):
        dp = [0 for i in range(len(s)+1)]
        p = [[False for i in range(len(s))] for j in range(len(s))]  #isPalindromes
        for i in range(len(s)+1):
            dp[i] = len(s) - i
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (((j - i) < 2) or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(1+dp[j+1], dp[i])
        return dp[0]-1
    def minCut(self, s): #Best
        n = len(s)
        f = []
        p = [[False for i in range(n)] for j in range(n)]
        for i in range(n+1):
            f.append(n-1-i)

        for i in reversed(range(n)):
            for j in range(i, n):
                if s[i]==s[j] and (j-i < 2 or p[i+1][j-1]):
                    p[i][j] = True
                    f[i] = min(f[i], f[j+1]+1)
        return f[0]
    def minCut4(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0: return 0
        isPalindrome = self.getIsPalindrome(s)
        f = [i for i in range(len(s)+1)]
        f[0] = 0
        for i in range(1, len(s)+1):
            for j in range(i):
                if isPalindrome[j][i-1]:
                    f[i] = min(f[i], f[j]+1)
        return f[len(s)]-1
        
        
    def getIsPalindrome(self, s):
        isPalindrome = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            isPalindrome[i][i] = True 
        for i in range(len(s)-1):
            isPalindrome[i][i+1] = (s[i] == s[i+1]) #Mistake not s[j]
        
        for length in range(2, len(s)):
            for start in range(0,  len(s)-length):
                isPalindrome[start][start+length] = isPalindrome[start+1][start+length-1] and s[start] == s[start+length]
        return isPalindrome    
if __name__ == "__main__":
    print Solution().minCut("aab")