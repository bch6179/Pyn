class Solution(object):
    def expandAroundCenter(self, s, i, j):
        l, r = i,j
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]
           
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s
            
        res = ""
        for i in range(len(s)):
            res1 = self.expandAroundCenter(s, i, i)
            if len(res1) > len(res): 
                res = res1
            res2 = self.expandAroundCenter(s, i, i+1)
            if len(res2) > len(res):
                res = res2
                
        return res

s = Solution()
print(s.longestPalindrome("baMistake"))