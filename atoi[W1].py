import sys
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str ==  "":
            return 0
        index = 0
        neg = 1
        res = 0
        MaxInt = (1 << 31)-1
        if str[0] == '-':
            index = 1; neg = -1
        elif str[0] == '+':
            index = 1
        for i in range(index, len(str)):
            if str[i] < '0' or str[i] > '9': break  #Mistake
            res = res*10 + int(str[i])   #Mistake to not convert char to integer
            if res > sys.maxint: break
        res = res * neg
        if res >= MaxInt:
            return MaxInt
        if res < MaxInt*-1:
            return MaxInt*-1-1
        return res

s = Solution() 
print s.myAtoi("   010")