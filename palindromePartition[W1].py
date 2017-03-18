# Palindrome Partitioning II
# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(s, 0, res, [])
        print(res)
    # a b c 
    # a 
    #   b  c
    #   bc
    #ab 
    #   c 
    def helper(self, s, pos, res, mylist):
        if pos == len(s) and mylist: 
            res.append(mylist[:]) 
            #Mistake need a copy; otherwise, the same object
            return
        for i in range(pos+1, len(s)+1):
            if self.isPalindrome(s, pos, i-1):
                mylist.append(s[pos:i] )
                self.helper(s, i, res, mylist)
                mylist.pop()
    
                #self.dfs(s[i:], stringlist+[s[:i]])
    def isPalindrome2(self, s):
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False 
            start+=1
            end-=1
        return True
    def isPalindrome(self, s, start,end):
        while start < end:
            if s[start] != s[end]:
                return False 
            start+=1
            end-=1
        return True
                
    def partition2(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        result = []
        for i in range(len(s)):
            if self.isPalindrome(s[:i + 1]):
                for r in self.partition(s[i + 1:]):
                    result.append([s[:i + 1]] + r)
        return result

    def isPalindrome3(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    assert Solution().partition("aab") == [
        ["a", "a", "b"],
        ["aa", "b"]
    ]
    # s=Solution()
    # s.partition("abc")