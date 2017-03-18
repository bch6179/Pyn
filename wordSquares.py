#Note preorder traverse in words tree, which is maintained through Trie or map indexi through prefix
# Map va
# 目描述：
# LeetCode 425. Word Squares

# Given a set of words (without duplicates), find all word squares you can build from them.

# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

# For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

# b a l l
# a r e a
# l e a d
# l a d y
# Note:

# There are at least 1 and at most 1000 words.
# All words will have the exact same length.
# Word length is at least 1 and at most 5.
# Each word contains only lowercase English alphabet a-z.
# Example 1:

# Input:
# ["area","lead","wall","lady","ball"]

# Output:
# [
#   [ "wall",
#     "area",
#     "lead",
#     "lady"
#   ],
#   [ "ball",
#     "area",
#     "lead",
#     "lady"
#   ]
# ]

# Explanation:
# The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
# Read and learned from other posts. Basic idea is use trie + backtrack. Trie related functions are 'build_trie', 'add_str', 'search_str'. And backtrack function is just 'find_word_squares'. Hope it's more understandable. Leave comments if you have any thoughts.

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        trie = {}
        self.build_trie(words, trie)
        
        size = len(words[0])
        
        result = []
        self.find_word_squares(trie, size, [], result)
        return result
        
    def build_trie(self, words, trie):
        for word in words:
            self.add_str(word, trie)
            
    def add_str(self, string, root):
        node = root
        for letter in string:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['#'] = string
    
    def search_prefix(self, node, prefix, candidates):
        if '#' in node:
            candidates.append(node['#'])
            return
        
        for letter in prefix:
            if letter not in node:
                return
            node = node[letter]
        
        for letter in node:
            self.search_prefix(node[letter], '', candidates)
        
    def find_word_squares(self, trie, size, cur, result):
        if len(cur) == size:
            result.append(cur[:])
            return
            
        candidates = []
        prefix = ''.join([string[len(cur)] for string in cur])
        self.search_prefix(trie, prefix, candidates)

        for candidate in candidates:
            self.find_word_squares(trie, size, cur + [candidate], result)


            def wordSquares(self, words):
    n = len(words[0])
    fulls = collections.defaultdict(list)
    for word in words:
        for i in range(n):
            fulls[word[:i]].append(word)
    def build(square):
        if len(square) == n:
            squares.append(square)
            return
        for word in fulls[''.join(zip(*square)[len(square)])]:
            build(square + [word])
    squares = []
    for word in words:
        build([word])
    return squares
Explanation
I try every word for the first row. For each of them, try every fitting word for the second row. And so on. The first few rows determine the first few columns and thus determine how the next row's word must start. For example:

wall      Try words      wall                     wall                      wall
a...   => starting  =>   area      Try words      area                      area
l...      with "a"       le..   => starting  =>   lead      Try words       lead
l...                     la..      with "le"      lad.   => starting   =>   lady
                                                            with "lad"
For quick lookup, my fulls dictionary maps prefixes to lists of words who have that prefix.

