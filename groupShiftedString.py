# [LeetCode] Group Shifted Strings 群组偏移字符
# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"], 
# Return:

# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

# ython with groupby
import itertools
class Solution():
    def groupStrings(self, strings):
        key = lambda s: [(ord(c) - ord(s[0])) % 26 for c in s]
        temp = itertools.groupby(sorted(strings, key=key), key)
        res = []
        for _, g in temp:
            t = list(g)
            res.append(t)
        return res

s= Solution()
print s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
# Old solution:

# def groupStrings(self, strings):
#     key = lambda s: [(ord(c) - ord(s[0])) % 26 for c in s]
#     return [sorted(g) for _, g in itertools.groupby(sorted(strings, key=key), key)]
# Solution 3: Python with defaultdict

# def groupStrings(self, strings):
#     groups = collections.defaultdict(list)
#     for s in strings:
#         groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,
#     return groups.values()
# Old solution:

# def groupStrings(self, strings):
#     groups = collections.defaultdict(list)
#     for s in strings:
#         groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,
#     return map(sorted, groups.values())

# class Solution(object):
#     def groupStrings(self, strings):
#         """
#         :type strings: List[str]
#         :rtype: List[List[str]]
#         """
#         dictionary = {}
#         for i in strings:
#             hs = self.strHash(i)
#             if hs not in dictionary.keys():
#                 dictionary[hs] = [str(i)]
#             else:
#                 self.insertStr(dictionary[hs],str(i))
#         return [dictionary[key] for key in dictionary.keys()]
    
#     def strHash(self,astring):
#         hslist = [(ord(i)-ord(astring[0])) % 26 for i in astring]
#         return tuple(hslist)
    
#     def insertStr(self, alist, astring):
#         i = 0
#         while i < len(alist) and ord(astring[0]) > ord(alist[i][0]):
#             i += 1
#         if i == len(alist):
#             alist.append(astring)
#         else:
#             alist[:] = alist[0:i] + [astring] + alist[i:]
# Note: For the return value, each inner list's elements must follow the lexicographic order.
# 这道题让我们重组偏移字符串，所谓偏移字符串，就是一个字符串的每个字符按照字母顺序表偏移相同量得到的另一个字符串，两者互为偏移字符串，注意相同字符串是偏移字符串的一种特殊情况，因为偏移量为0。现在给了我们一堆长度不同的字符串，让我们把互为偏移字符串的归并到一起，我最开始想的是建立字符度和该长度的所有偏移字符串的映射，但是很明显的错误是相同长度的不一定都是偏移字符串，比如'ab'和'ba‘，所以只能用哈希表来建立一个字符串和所有和此字符串是偏移字符串的集合之间的映射，由于题目要求结果是按字母顺序的，所以用multiset来保存结果，一来可以保存重复字符串，二来可以自动排序。然后我还写了一个判断二个字符串是否互为偏移字符串的函数，注意在比较两个字母距离时采用了加26，再对26取余的trick。我们遍历给定字符串集，对于遍历到的字符串，我们再遍历哈希表，和每个关键字调用isShifted函数来比较，如果互为偏移字符串，则加入其对应的字符串集，并标记flag，最后遍历完哈希表，没有跟任何关键字互为偏移，那么就新建一个映射，最后要做的就是把multiset转换为vector即可，参见代码如下：