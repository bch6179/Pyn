class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        n = len(str)
        #if n%2 == 1: return False
        previous = ""
        for ws in range(1, n/2+1):
            k = ws
            previous = str[:k]
            while k < n: #Mistake why k < n -ws , the last one would be k = n after adding ws, so as long as k < n, k+ws would be fine
                if str[k:k+ws] != previous:  # prev mode, or m * xx
                    break      
                k+=ws       
            if k== n:
                return True
        return False
        
    def repeatedSubstringPattern2(self, str): #bad one
        """
        :type str: str
        :rtype: bool
        """
        n = len(str)
        #if n%2 == 1: return False
        
        for ws in range(1, n+1):
            end = ws
            for i in range(n/end-1):
                if str[end*i:end*(i+1)] != str[end*(i+1):end*(i+2)]: #Mistake my bad
                    break               
            if i == n/end-1:
                return True
        return False
s = Solution() 
print s.repeatedSubstringPattern("abab")

print "True" if s.repeatedSubstringPattern("aba") else "False"
print s.repeatedSubstringPattern("aaaaaa")
#print s.repeatedSubstringPattern("aabaabaabaab")