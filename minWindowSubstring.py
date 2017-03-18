https://leetcode.com/problems/minimum-window-substring/

# 1. Use two pointers: start and end to represent a window.
# 2. Move end to find a valid window.
# 3. When a valid window is found, move start to find a smaller window.
# To check if a window is valid, we use a map to store (char, count) for chars in t. And use counter for the number of chars of t to be found in s. The key part is m[s[end]]--;. We decrease count for each char in s. If it does not exist in t, the count will be negativ

# orderdedDict 可以用一个类似LRU的结构，通过Queue的首尾来记录窗口大小, pop left

# 1. actively pop left, to find another smaller window
# 2. lazy, until find another letter a in the pattern, start to shrink left window, since now counter[a] is already negative


iven a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
from collections import Counter

class Solution(object):
# The current window is s[i:j] and the result window is s[I:J]. In need[c] I store how many times I need character c (can be negative) and missing tells how many characters are still missing. In the loop, first add the new character to the window. Then, if nothing is missing, remove as much as possible from the window start and then update the result.

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        pattern = Counter(t)
        start, end = 0, 0
        minStart, minEnd = 0, 0
        count = len(t)
        
        for end, c in enumerate(s, 1):
            if pattern[c] > 0 :
                count -= 1  # c exist in t
            pattern[c] -= 1
            
            while count == 0:
                if minEnd == 0 or end - start < minEnd - minStart:
                    minStart = start
                    minEnd = end
                pattern[s[start]]+= 1
                if pattern[s[start]] > 0: 
                    count += 1
                start += 1
        return s[minStart:minEnd]

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        pattern = Counter(t)
        start, end = 0, 0
        minStart, minEnd = 0, 0
        count = len(t)
        
        for end, c in enumerate(s, 1):
            count -= (1 if pattern[c] > 0 else 0) # c exist in t
            pattern[c] -= 1
            
            if count == 0:
                while start < end and pattern[s[start]] < 0:
                    pattern[s[start]] += 1            
                    start += 1
                if minEnd == 0 or end - start < minEnd - minStart:
                    minStart = start
                    minEnd = end
        return s[minStart:minEnd]


# def minWindow(self, s, t):  #2
#     need, missing = collections.Counter(t), len(t)
#     i = I = J = 0
#     for j, c in enumerate(s, 1):
#         missing -= need[c] > 0 # reduce the tracking count only when c exist in pattern; so we don't need to reduce when it slided out the window
#         need[c] -= 1
#         if not missing:
#             while i < j and need[s[i]] < 0:
#                 need[s[i]] += 1
#                 i += 1
#             if not J or j - i <= J - I:
#                 I, J = i, j
#     return s[I:J]
#     def minWindow(self, s, t): #1
#         if not t: return ""
#         map = [0 for _ in range(128)]
#         for i in t: map[ord(i)] += 1
#         begin = 0
#         end = 0
#         minbegin = 0
#         minlength = len(s) + 2
#         count = len(t)
#         while end < len(s):
#             if map[ord(s[end])] > 0: count -= 1
#             map[ord(s[end])] -= 1
#             end += 1
#             while count == 0:
#                 if end - begin < minlength:
#                     minbegin = begin
#                     minlength = end - begin
#                 map[ord(s[begin])] += 1
#                 if map[ord(s[begin])] > 0:
#                     count += 1
#                 begin += 1
#         if minlength > len(s): return ""
#         return s[minbegin: minbegin + minlength]

# def minWindow(self, s, t):
#         m = len(s)
#         n = len(t)
#         if m < n:
#             return ''
#         lt = {}
#         for i in t:
#             if i not in lt:
#                 lt[i] = 1
#             else:
#                 lt[i] += 1
#         missing = n
#         i = I = J = 0
#         for j, c in enumerate(s, 1):    
#             if c in lt and lt[c] > 0:
#                 missing -= 1
#             if c in lt:
#                 lt[c] -= 1

#             while i < j and not missing:
#                 if not J or j-i < J-I:
#                     I, J = i, j
#                 if s[i] not in lt:
#                     i += 1
#                     continue
#                 else:
#                     lt[s[i]] += 1
#                     if lt[s[i]] > 0:
#                         missing += 1
#                     i += 1
#         return s[I:J]

# def minWindow(self, s, t):
#     need, missing = collections.Counter(t), len(t)
#     i = I = J = 0
#     for j, c in enumerate(s, 1):
#         missing -= need[c] > 0
#         need[c] -= 1
#         if not missing:
#             while i < j and need[s[i]] < 0:
#                 need[s[i]] += 1
#                 i += 1
#             if not J or j - i <= J - I:
#                 I, J = i, j
#     return s[I:J]