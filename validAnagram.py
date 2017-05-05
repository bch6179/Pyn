# iven two strings s and t, write a function to determine if t is an anagram of s. For example, s = "anagram", t = "nagaram", return tr

# dict  = {}
# for c in s:
#     dict[c] = dict.get(c, 0) + 1

# for c in t:
#     if t not in dict:
#         return False
#     else:
#         if dict[c] == 1:
#             del dict[c]
#         else dict[c] = dict[c]-1
# return not dict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict  = {}
        for c in s:
            dict[c] = dict.get(c, 0) + 1
        
        for c in t:
            if c not in dict:
                return False
            else:
                if dict[c] <= 1:
                    del dict[c]
                else:
                    dict[c] = dict[c]-1
        return not dict

s= Solution()
print s.isAnagram('ab', 'ba')





























