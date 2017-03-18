class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
       # if s == "": return False
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and s[l].isalnum() != True:
                l += 1
            while l < r and s[r].isalnum() != True:
                r -= 1
            if l >= r: return True
            if s[l].upper() != s[r].upper():
                return False
            l += 1
            r -= 1
        return True  
        # " 1..1,, "
s = Solution() 
print s.isPalindrome("ab")
print s.isPalindrome("aA")