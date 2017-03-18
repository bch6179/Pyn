 https://leetcode.com/problems/word-break-ii/

 Word Break II Add to List
Description  Submission  Solutions
Total Accepted: 80155
Total Submissions: 357234
Difficulty: Hard
Contributors: Admin
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.

Reputation:  12,922
Python:
class Solution(object):
    def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    return self.helper(s, wordDict, {})
    
def helper(self, s, wordDict, memo):
    if s in memo: return memo[s]
    if not s: return []
    
    res = []
    for word in wordDict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(word)
        else:
            resultOfTheRest = self.helper(s[len(word):], wordDict, memo) . #mistake not len(s) but len(word)
            for item in resultOfTheRest:
                item = word + ' ' + item
                res.append(item)
    memo[s] = res
    return res
def wordBreak(self, s, wordDict):
    memo = {len(s): ['']}
    def sentences(i):
        if i not in memo:
            memo[i] = [s[i:j] + (tail and ' ' + tail)
                       for j in range(i+1, len(s)+1)
                       if s[i:j] in wordDict
                       for tail in sentences(j)]
        return memo[i]
    return sentences(0)

class Solution(object):
    def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: Set[str]
    :rtype: List[str]
    """
    return self.helper(s, wordDict, {})
    
def helper(self, s, wordDict, memo):
    if s in memo: return memo[s]
    if not s: return []
    
    res = []
    for word in wordDict:
        if not s.startswith(word):
            continue
        if len(word) == len(s):
            res.append(word)
        else:
            resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
            for item in resultOfTheRest:
                item = word + ' ' + item
                res.append(item)
    memo[s] = res
    return res

T tusizi 
Reputation:  1,324
 class Solution:
# @param s, a string
# @param dict, a set of string
# @return a list of strings
def wordBreak(self, s, dic):
    if not dic:
        return []
    n = max(len(d) for d in dic)
    stack, parents = [0], collections.defaultdict(set)
    while stack:
        parent = stack.pop()
        for child in range(parent+1, parent+n+1):
            if s[parent:child] in dic:
                if child not in parents:
                    stack.append(child)
                parents[child].add(parent)
    stack, res = [[len(s)]], []
    while stack:
        r = stack.pop()
        if r[0] == 0:
            r = [s[i:j] for i, j in zip(r[:-1], r[1:])]
            res.append(' '.join(r))
        for parent in parents[r[0]]:
            stack.append([parent]+r)
    return res
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(0, s, set(wordDict), {})

    def helper(self, k, s, wordDict, cache):
        if k == len(s):
            return []
        elif k in cache:
            return cache[k]
        else:
            cache[k] = []
            for i in range(k, len(s)):
                left = s[k:i+1]
                if left in wordDict:
                    remainder = self.helper(i+1, s, wordDict, cache)
                    if remainder:
                        for x in remainder:
                            cache[k].append(left + " " + x)
                    elif (i == len(s)-1):
                        cache[k].append(left)
            return cache[k]