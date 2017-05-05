import sys    

# only one index is needed
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = sys.maxint
        n = sys.maxint
        res = len(words)
        for i,w in enumerate(words):
            if w == word1:
                m = i
            if w == word2:
                n = i
            
            res = min(res, abs(m-n))
        return res
            
    def shortestDistance2(self, words, word1, word2):
        ans = len(words)
        current_word, current_index = None, 0
        for index, word in enumerate(words):
            if word != word1 and word != word2: continue
            if current_word and word != current_word:
                ans = min(ans, index - current_index)
            current_word, current_index = word, index
        return ans
s= Solution()
print s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"]
,"makes",
"coding")