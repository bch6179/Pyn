from collections import defaultdict

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # def dfs(s):
        #     n = len(s)
            
        #     res = []
        #     for i in reversed(range(n-1)):
        #         if s[i:] in wordDict:
        #             p = dfs(s[:i])
        #             for k in p:
        #                 res.append(k+' '+s[:i])
                     
        #     return res
        def dfs(s, memo):
            if s in memo: return memo[s]
            if not s: return []

            res = []
            for w in  wordDict:
                if   s.startswith(w):
                    if len(s) == len(w): 
                        res.append(w)
                    else:
                        pre = dfs(s[len(w):], memo)
                        for p in pre :
                            res.append(w + ' ' + p)
            memo[s] = res
            return res
            
       
        return dfs(s,{})
s= Solution()
print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])