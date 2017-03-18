https://leetcode.com/problems/alien-dictionary/?tab=Description


There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Example 2:
Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".

Example 3:
Given the following words in dictionary,

[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".

o similar solutions. Both first go through the word list to find letter pairs (a, b) where a must come before b in the alien alphabet. The first solution just works with these pairs, the second is a bit smarter and uses successor/predecessor sets. Doesn't make a big difference here, though, I got both accepted in 48 ms.

Solution 1

def alienOrder(self, words):
    less = []
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                less += a + b,
                break
    chars = set(''.join(words))
    order = []
    while less:
        free = chars - set(zip(*less)[1])
        if not free:
            return ''
        order += free
        less = filter(free.isdisjoint, less)
        chars -= free
    return ''.join(order + list(chars))
Solution 2

def alienOrder(self, words):
    pre, suc = collections.defaultdict(set), collections.defaultdict(set)
    for pair in zip(words, words[1:]):
        for a, b in zip(*pair):
            if a != b:
                suc[a].add(b)
                pre[b].add(a)
                break
    chars = set(''.join(words))
    free = chars - set(pre)
    order = ''
    while free:
        a = free.pop()
        order += a
        for b in suc[a]:
            pre[b].discard(a)
            if not pre[b]:
                free.add(b)
    return order * (set(order) == chars)