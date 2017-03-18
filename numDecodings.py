
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) == 0): return 0
        pre = 27
        first, second = 1,1
        answer = 0
        
        for c  in reversed(s):
            digit = int(c)
            if digit == 0: answer = 0
            else: 
                answer = first +(second if digit*10 + pre < 27 else 0) #Mistake  () for if sentence 
            second = first
            first = answer
            pre = digit 
        return answer
s = Solution() 
print s.numDecodings("1")