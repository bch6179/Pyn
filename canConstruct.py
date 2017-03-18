from collections import OrderedDict
class Solution(object):
    def canConstruct2(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict = {}
        
        for c in magazine:
            dict[c] += 1
        
        for c in ransomeNote:
            if c in dict:
                dict[c] -= 1
                if dict[c] == 0:
                    del dict[c] #dict.popitem(c)
            else:
                return False
        return True
    def canConstruct(self, ransomNote, magazine):
        s1, s2, i = sorted(ransomNote), sorted(magazine), 0
        for c in s2:
            if i==len(s1) or c > s1[i]:
                break
            if c==s1[i]:
                i += 1
      
        return i==len(s1)
s = Solution() 
print s.canConstruct("bg","gggggbbbbbba")