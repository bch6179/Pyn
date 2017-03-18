class Solution(object):
    def getCS(self, prev):      
        m = len(prev)
        count = 1
        i = 0
        prev = '#'
        res = ''  #Mistake Need to init here, so that the temp not get from previous ones
        for cur in prev:
            if cur == prev:
                count += 1
            else:
                if cur != '#': 
                    res+= str(count)+prev
                count = 1
                prev = cur
            i += 1
        res+=str(count)+prev #last one
        return res
    def getCS(self, prev):      
        m = len(prev)
        count = 1
        i = 0
        res = ''  #Mistake Need to init here, so that the temp not get from previous ones
        while i < m-1:
            if prev[i] == prev[i+1]:
                count += 1
            else:
                res+= str(count)+prev[i]
                count = 1
            i += 1
        res+=str(count)+prev[i] #last one
        return res
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        #1211  111221 
        if n <= 0: return -1
        prev = '1'
        
        while n > 1:
            prev = self.getCS(prev)
            n -= 1
        return prev
s = Solution() 
print s.countAndSay(4)