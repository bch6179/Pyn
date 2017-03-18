class Solution(object):
    def isSubsequence(self, s, t):
        charPos = dict()
        for pos, char in enumerate(t):
            charPos.setdefault(char, [])
            charPos.append(pos)
        
        lowerBound = 0
        for char in s:
            if char not in charPos:
                return False
            else:
                firstPos = self.findFirstPos(charPos[char], lowerBound)
                if firstPos == -1:
                    return False
                else:
                    lowerBound = firstPos + 1
        return True
                
                
    def findFirstPos(self, poses, lowerBound):
        low = 0
        high = len(poses) - 1
        while low < high:
            mid = (high - low) / 2 + low
            if poses[mid] >= lowerBound:
                high = mid
            else:
                low = mid + 1
        if poses[low] >= lowerBound:
            return poses[low]
        else:
            return -1
s = Solution() 
s.isSubsequence("abc", "adbce")

For the follow-up question, however, this solution is not efficient as we need to compare s with t every time. For example, if we have k=1B, len(s) = 100, len(t)=500,000, the total complexity will be O(10^9*(100+500,000)). So the tricky is we don't want to scan t every time as it costs too much.

Here is solution 2, check comments for a brief explanation. The idea is to scan t once and save the index (as a sorted list) of each letter.

The running time is 525 ms. Although this one-time run cost of solution 2 is bigger than solution 1, if we have many s, we can save a lot of time by avoid comparing s with t every time.

    def isSubsequence(self, s, t):
        # create a list to save the index of each letter in t
        listt = [[] for _ in range(26)]
        
        for i in range(len(t)):
            listt[ord(t[i])- 97].append(i)
        # create a list to find the index of each letter of s in t    
        lists = [0 for _ in range(len(s))]
        
        if not s: return True
        if not listt[ord(s[0])-97]: return False # if first letter of s is not in t
        lists[0] = listt[ord(s[0])-97].pop(0) # min. value for first letter
                
        for i in range(1,len(s)):
            if not listt[ord(s[i])-97]: return False # if the letter is not in t
            index, value = self.helper(listt[ord(s[i])-97],lists[i-1])
            if index == -1: return False
            lists[i],listt[ord(s[i])-97]= value, listt[ord(s[i])-97][index+1:]
                    
        return lists == sorted(lists)
      # a helper function to find the index   
    def helper(self, nums, value):
        if value > nums[-1]: return (-1,-1)
        else:
            temp, i = nums[0], 0
            while value > temp and i < len(nums):
                i+=1
                temp = nums[i]
        return (i,temp)

     Trade space for time and with binary search

0
A asv325 
Reputation:  5
For follow-up. Trade space for time. Store char positions for t.
s = aabac,
t = aaabaac.
{a: [0,1,2,4,5],
b: [3],
c: [6]}
Initialize lowerBound = 0. Iterate over s, binary search the first position of the current char satisfying position >= lowerBound, update lowerBound with the found position + 1.
Of course, you may use bisect instead of implementing findFirstPos https://docs.python.org/2/library/bisect.html
Please let me know if there is any mistake. Thanks.

