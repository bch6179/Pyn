Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:
Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Concatenated Word https://leetcode.com/problems/concatenated-words/

Reuse solution for word-break: ~3000 msec/TLE

Reuse the solution for word-break given here: https://leetcode.com/problems/word-break/
We modify the condition that whole words are breakable to the new definition that a word will be breakable if it would have two or more sub-words. This is done using the following condition where we return mark the whole string length as un-breakable.
left_is_breakable = table[i-1] if i > 0 else (True and j != len(s)-1)
Now iterate every word and test if it could be broken.
class TestBreakable(object):
    def __init__(self, wordDict):
        self.wordDict = wordDict
        return
    
    def wordBreak(self, s):
        table = [False]*(len(s))
        for j in range(len(s)):
            for i in range(j, -1, -1):
                word_so_far = s[i:j+1]
                left_is_breakable = table[i-1] if i > 0 else (True and j != len(s)-1)
                if word_so_far in self.wordDict and left_is_breakable:
                    table[j] = True
                    break
        return table[-1]
        

A word can be decomposed into words smaller than it only. So we sort by length and reduce the size of applicable dictionary in every iteration.
class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        results = []
        words.sort(reverse = True, key=len)
        words_dict = set(words)
        for idx, word in enumerate(words):
            test_breakable = TestBreakable(words_dict)
            if word and test_breakable.wordBreak(word):
                results.append(word)
            words_dict.remove(word)
        return results
Other interesting approaches

Use a Trie and DFS to solve this problem. This solution is like putting two pointers to search through the tree. When find a word, put the other pointer back on root then continue searching.
https://discuss.leetcode.com/topic/72160/simple-java-trie-dfs-solution-144ms
https://discuss.leetcode.com/topic/72098/python-explanation

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        word_set = set(words)
        ans = []
        def helper(w, cur, cnt):
            if cur == len(w):
                if cnt > 1:
                    return True
                else:
                    return False
            for i in xrange(cur + 1, len(w) + 1):
                if w[cur : i] in word_set and helper(w, i, cnt + 1):
                    return True
            return False
        for w in words:
            if helper(w, 0, 0):
                ans.append(w)
        return ans


S = set(words)
ans = []
for word in words:
    if not word: 
        continue
    stack = [0]
    seen = {0}
    M = len(word)
    while stack:
        node = stack.pop()
        if node == M:
             ans.append(word)
             break
         for j in xrange(1, M - node + 1): # just start from 1
             if word[node:node+j] in S and node + j not in seen \
                 and not (node==0 and node+j==M): # that is, the word must be broken but not a complete one
                 stack.append(node + j)
                 seen.add(node + j)
return ans
Actually, the variable node here can be recognised as the length of a matched pattern in stack.