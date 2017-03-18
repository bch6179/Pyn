class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # 123.1
        # 113.2
        # 112.33.2  #mistake not considering more .
        
        #test "1" "0" and "1.0" "1.2"
        
        i, j= 0,0
        num1, num2 = 0, 0
        len1, len2 = len(version1), len(version2)
        
        while i < len1 or j < len2:
            while i < len1 and version1[i] != '.':
                num1 = num1*10 + int(version1[i]); i+=1 #Mistake forgot i+=1
            while j < len2 and version2[j] != '.':
                num2 = num2*10 + int(version2[j]); j+=1
            
            if num1 != num2:
                return 1 if num1 > num2 else -1
            i += 1
            j += 1
            num1 = 0 #Mistake not reinitialize
            num2 = 0
        return 0     
    def compareVersion2(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        # 123.1
        # 113.2
        # 112.33.2  #mistake not considering more .
        
        #test "1" "0" and "1.0" "1.2"
        lv1 =version1.split('.')
        lv2 = version2.split('.')
        
        length = max(len(lv1), len(lv2))
        for i in range(length):
            #1. more .
            #2. same level, but diff value
            #3. leading 0
            c1 = int(lv1[i]) if i < len(lv1) else 0
            c2 = int(lv2[i]) if i < len(lv2) else 0
            if c1 != c2:
                return 1 if c1 > c2 else -1
            
        return 0    
s = Solution() 
print s.compareVersion("1", "0")
        # def stripZero_badone(version):  #Mistake
        #     for i in range(len(version1)):
        #         if version1[i] == '0':
        #             i+= 1
        #     return ''.join(version1[i:])
        
        # if version1 == '' and version2 == '': return 0
        # elif version1 == '': return -1
        # elif version2 == '': return 1
        
        # version1 = stripZero(version1)
        # version2 = stripZero(version2)
            
        # if len(version1) > len(version2): 
        #     return -1 * self.compareVersion(version2, version1) 
        # i, j =0,0
        # while i < len(version1) and j < len(version2) and version1[i] == version2[j]:
        #     i+=1; j+=1
        # if i == len(version1):
        #     return 0 if j == len(version2) else -1
        # else:
        #     if version1[i] == '.':
        #         return -1
        #     elif version2[j] == '.':
        #         return 1
        #     else:
        #         return -1 if version1[i] < version2[j] else 1
        # return 0