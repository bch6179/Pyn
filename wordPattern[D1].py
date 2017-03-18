from collections import *
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        #pattern a:(0,3) b:(1,2)
        pmap = defaultdict(lambda: [])
        map = defaultdict(lambda:[])
        
        #pmap.setdefault([])
        for i, c in enumerate(list(pattern)):
            pmap[c].append(i)
        for i,word in enumerate(str.split(' ')):
            map[word].append(i)
        i = 0
        while i < min(len(pmap),len(map)):
            if map.values()[i]  != pmap.values()[i]:  #dog: 0,3, cat: 1,2
                return False
            i+=1
        return i == len(map)
s = Solution() 
print s.wordPattern("abba","dog cat cat dog")

#  wordList = str.split()
#     n1 = len(pattern)
#     n2 = len(wordList)
#     if (n1 != n2):
#         return False
#     else:
#         wordList = str.split()
#         # wordList = [s.encode('ascii') for s in wordList]
#         # pattern = [s.encode('ascii') for s in pattern]
#         mydict = {}
#         result = True
#         for i in range(len(pattern)):
#             if (pattern[i] not in mydict):
#                 if wordList[i] not in mydict.values():
#                     mydict[pattern[i]] = wordList[i]
#                 else:
#                     result = False
#                     break
#             else:
#                 if (mydict[pattern[i]] != wordList[i]):
#                     result = False
#                     break
#         return result

# class Solution(object):
#     def wordPattern(self, pattern, word_str):
#         """
#         :type pattern: str
#         :type str: str
#         :rtype: bool
#         """
#         words = word_str.split(" ")
#         if len(pattern) != len(words):
#             return False

# 		# use two dictionaries, mapping character / string with index
#         pattern_map, word_map = {}, {}
#         for i in xrange(len(pattern)):
#             if pattern_map.get(pattern[i], -1) != word_map.get(words[i], -1):
#                 return False
#             pattern_map[pattern[i]] = word_map[words[i]] = i

#         return True