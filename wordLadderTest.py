class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        import collections
        q = collections.deque([[beginWord,1]])
        wordList.append(endWord)
         
        while q:
            w, length = q.popleft()
     
            if w == endWord:
                return length
            for i in range(len(w)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    k = w[:i]+c+w[i+1:]            
                    if k in wordList:
                        #wordList.remove(k)
                        q.append([k,length+1])
        return 0
s= Solution()
print s.ladderLength("hog",
"cog",
["hot","dot","dog","lot","dot","log"])