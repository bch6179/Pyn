class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        sum = map[s[-1]] #Mistake map is not callable
        
        index = len(s)-2
        cur = 0
        while index >= 0:
            if map[s[index]] >= map[s[index+1]]:
                sum += map[s[index]]
            else:
                sum -= map[s[index]]
            index -= 1
      
        return sum
        
    def romanToInt2(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        sum = 0
        prev = 0
        for n in reversed(s):
            cur = map[n]
            sum += -1*cur if cur < prev else cur
            prev = cur
        return sum