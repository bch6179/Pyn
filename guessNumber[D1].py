class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n 
        while start <= end:
            
            m = 1 + (n-1)/2  #Mistake
            
            k = guess(m)
            if k == 0:
                return m
            elif k == 1:
                end = m -1
            elif k == -1:
                start = m + 1
        return -1


