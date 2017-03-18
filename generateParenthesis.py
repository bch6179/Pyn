class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []    
        if n == 0: return 
        
        self.dfs(n,n,'', res)
        return res
        
    def dfs(self, l, r, item, res):
        if r < l: return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.dfs(l-1, r, item+'(', res)
        if r > 0:
            self.dfs(l, r-1, item+')', res)    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = set()
        if n == 0: return res.add("")
        else:
            prev = self.generateParenthesis(n-1)
            for p in res:
                for i in range(len(p)):
                    if p[i] == '{':
                        res.add(''.join(p[:i]+'{}'+p[i:]))
                res.add('{}'+p)
        return res
