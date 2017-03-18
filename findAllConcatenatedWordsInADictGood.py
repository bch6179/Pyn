class Solution(object):
 
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        def canBreak(s, words):
            if words == []: return False

            dp = [True] + [False]*len(s)
            for i in range(1, len(s)+1):
                for j in range(i):
                    if dp[j] and s[j:i] in words:
                        dp[i] = True
                        break
            return dp[-1]
         
        def wordBreak( s, words):
            ok = [True]
            for i in range(1, len(s)+1):
                ok += any(ok[j] and s[j:i] in words for j in range(i)),
            return ok[-1]
        
        if len(words) < 3: return []         
        words = sorted(words, key=lambda(w): len(w))
        previous = []
        res = []
        for w in words:
            if wordBreak(w, previous):
                res.append(w)
            previous.append(w)
        return res
s= Solution()
data = ['bad','badreal','realbad','a','r','e','ae','real']
print s.findAllConcatenatedWordsInADict(data)