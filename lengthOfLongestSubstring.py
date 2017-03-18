https://leetcode.com/submissions/detail/84200701/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
            
        left = 0
        ans = 0 
        found = {}
        
        for i in range(len(s)):
            if s[i] in found and found[s[i]] >= left:
                left = found[s[i]]+1
            else: ans = max(i-left+1, ans)
            found[s[i]] = i
        
        return ans
        
        