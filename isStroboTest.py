class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(m,n):
            if m == 0: return ['']
            if m == 1: return list('018')
            
            return [ a+g+b for a,b in '00 11 88 69 96'.split()[m==n:] for g in dfs(m-2, n) ]
            
        if n == 0: return []
        return dfs(n,n)
s= Solution()
print s.findStrobogrammatic(2)