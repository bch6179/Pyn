class Solution(object):
    def lengthOfLastWord(self, s):
        end = len(s)
        count = 0
        if end == 0: return 0
        for i in range(end-1, -1, -1):#reversed(range(end)) : #range(end-1, -1, -1)
            if s[i] != ' ':
                break
            
        for i in range(i, -1, -1):
            if s[i] != ' ':
                count += 1
            else:
                break
                 # if start == end:  this won't work
                #     lastcount = count
 
        return count
    def lengthOfLastWord5(self, s):
        end = len(s)
        count = 0
        for start in range(end):
            if start >0 and s[start-1] == ' ' and s[start] != ' ':
                count = 1
            elif s[start] != ' ':
                count += 1
                 # if start == end:  this won't work
                #     lastcount = count
 
        return count
    def lengthOfLastWord3(self, s):
        start = 0 
        end = len(s)-1
        count = 0
        while start <= end:
            if start >0 and s[start-1] == ' ' and s[start] != ' ':
                count = 1
                start+=1
            elif s[start] != ' ':
                count += 1
                start+=1
                # if start == end:  this won't work
                #     lastcount = count
            
            else:
                start += 1 
        return count

                
    def lengthOfLastWord2(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0 
        end = len(s)-1
        count = 0
        while start <= end: # If check, use while i
            while start <= end and s[start] == ' ':
                # abd  dc
                count = 0
                start += 1
            if start > end: 
                break
            while start <= end and s[end] == ' ':
                end -= 1
            if start > end:
                break
            if s[start] != ' ':
                count += 1
            start += 1
        return count
s = Solution() 
print s.lengthOfLastWord("a ")