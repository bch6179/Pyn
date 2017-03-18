def reverse(nums, start, end):
    while start < end:
        temp = nums[end]
        nums[end] = nums[start]
        nums[start] = temp
        start+=1
        end-=1
def swap(a, b):
    temp = a
    a = b
    b = temp

class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reversewords2Str(self,s):
        s = s.strip().split()
        res = []
        for str in s:
            if len(res) > 0: res.append(' ')
            if str != ' ':
                res.append(str)
                 
        return ''.join(list(reversed(res)))
    def reversewords2Str2(self,s):
        s = s.strip().split()
        res = []
        for i in range(len(s)-1, -1, -1):
            if len(res) > 0: res.append(' ')
            if str != ' ':
                res.append(s[i])
                 
        return ''.join(res)
    def reverseWordsStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None or len(s) <= 1: return s
        n = len(s)
        
        start,end =0, n-1
        i = n-1
        res = []
        while i >= 0:
            end = i
            while i >= 0 and s[i] != ' ':
               i -= 1   
            start = i+1

            res.append(s[start:end+1]) #Mistake end+1
            res.append(' ')
            i -= 1
        return ''.join(res)
    def reverseWords(self, s):
        start = 0
        end = 0
        i = 0
        while i < len(s): #Mistake for i in
            start = i
            while i < len(s) and s[i] != ' ':
                i += 1             
            end = i-1
            reverse(s, start, end)
            i += 1
        reverse(s, 0, len(s)-1)
s = Solution() 
# input = list('hello world')
# s.reverseWords(input)
# print ''.join(input)
print s.reverseWordsStr('hello world')
