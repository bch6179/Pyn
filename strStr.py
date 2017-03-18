class Solution(object):
    def strStr2(self, haystack, needle):
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        #abcxbcddef
        #bcd 
        if haystack is None or needle is None:
           return -1
        i = 0
        j = 0  #Mistake not to use , 
        while i <= len(haystack) - len(needle):# 0 1 2 3 4 [5]   5-3 =2 inclusive, or 5-3+1 not in 
            j = 0                              #     2 3 4
            while j < len(needle):
                if (i+j) >= len(haystack) or needle[j] != haystack[i+j]:
                    break
                j += 1
            if j == len(needle):
                return i
            i = i + 1  #Mistake issip missi[ssip] i + j + 1 will skip , 
            #it doesn't mean it won't success if back step one which is equal
        return -1 #i if j == len(needle) else -1, not necessarily "" "" already considered
          #for "" case  #Mistake not define j out
s = Solution() 
print s.strStr("mississippi","issipi")
print s.strStr("mississippi", "issip")
print s.strStr( "issip","mississippi")
print s.strStr("", "")