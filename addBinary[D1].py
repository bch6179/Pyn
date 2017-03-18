class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = len(a)
        m = len(b)
        if n > m:
            return self.addBinary(b,a)  #ACTUALLY NOT NEED 
        res = ""
        carry = 0
        i = n -1
        j = m -1
        while i >= 0 or j >=0 or carry == 1: #Mistake reverse the number
            x = int(a[i])if i>=0 else 0  #mistake -'0 not for python Line 15: TypeError: unsupported operand type(s) for -: 'unicode' and 'str'
            y =  int(b[j]) if j >= 0 else 0 #Mistake j should not be i
            t = y + x  + carry  # divmod(5,2)
            res =   str(t % 2)  + res
            carry  = t / 2
            i-=1
            j-=1
    
        return res  # 1 1 , 1, 0, 0 0, 0:11
s = Solution() 
print s.addBinary("101","1011")  #"10000"
#print s.addBinary("11", "1")

def addBinary(self, a, b):
    res, carry = '', 0
    i, j = len(a) - 1, len(b) - 1
    while i >= 0 or j >= 0 or carry:
        curval = (i >= 0 and a[i] == '1') + (j >= 0 and b[j] == '1')
        carry, rem = divmod(curval + carry, 2)
        res = `rem` + res
        i -= 1
        j -= 1
    return res
class Solution:
    def addBinary(self, a, b):
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + str(int(a[-1]) + int(b[-1]))