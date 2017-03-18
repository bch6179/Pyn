#Double end BFS works because 2*2 = 4 complexity in the case of one end, 4path*len, 
# but for two end, divided to len/2 * 2  + len/2*2 = 2 path * len, that when you conquer, to merge the path, effort is saved by the merging in sorted 
import collections
import string
class Solution:
# @param start, a string
# @param end, a string
# @param dict, a set of string
# @return a list of lists of string
    def findLadders(self, start, end, dic):
        dic.append(end)
        level = {start}
        parents = collections.defaultdict(set)
        while level and end not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(start)):
                        n = node[:i]+char+node[i+1:]
                        if n in dic and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[end]]
        while res and res[0][0] != start:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res
s = Solution()
print s.findLadders("hit","cog",["hot","dot","dog","lot","log","cog", "dom"])
# Every level we use the defaultdict to get rid of the duplicate

#  know source and destination, we can build the word tree by going forward in one direction 
# and backwards in the other. We stop when we have found that a word in the next level of BFS
#  is in the other level, but first we need to update the tree for the words in the current level.

# Then we build the result by doing a DFS on the tree constructed by the BFS.

# The difference between normal and double BFS is that the search changes from O(k^d) to O(k^(d/2) + k^(d/2)). Same complexity class, right? Yeah, tell it to the Facebook guys that have to search in graphs with hundreds of thousands of nodes.

# class Solution(object):
    
#     # Solution using double BFS

#     def findLadders(self, begin, end, words_list):
        
#         def construct_paths(source, dest, tree):
#             if source == dest: 
#                 return [[source]]
#             return [[source] + path for succ in tree[source]
#                                     for path in construct_paths(succ, dest, tree)]

#         def add_path(tree, word, neigh, is_forw):
#             if is_forw: tree[word]  += neigh,
#             else:       tree[neigh] += word,

#         def bfs_level(this_lev, oth_lev, tree, is_forw, words_set):
#             if not this_lev: return False
#             if len(this_lev) > len(oth_lev):
#                 return bfs_level(oth_lev, this_lev, tree, not is_forw, words_set)
#             for word in (this_lev | oth_lev):
#                 words_set.discard(word)
#             next_lev, done = set(), False
#             while this_lev:
#                 word = this_lev.pop()
#                 for c in string.ascii_lowercase:
#                     for index in range(len(word)):
#                         neigh = word[:index] + c + word[index+1:]
#                         if neigh in oth_lev:
#                             done = True
#                             add_path(tree, word, neigh, is_forw)                
#                         if not done and neigh in words_set:
#                             next_lev.add(neigh)
#                             add_path(tree, word, neigh, is_forw)
#             return done or bfs_level(next_lev, oth_lev, tree, is_forw, words_set)
                            
#         tree, path, paths = collections.defaultdict(list), [begin], []
#         is_found = bfs_level(set([begin]), set([end]), tree, True, words_list)
#         return construct_paths(begin, end, tree)


#         t's call k the max number of neighbors of a node, and d is the distance from start to end. In traditional BFS, we explore k nodes at each BFS level, each one generating in the worst case k neighbors till we find end. So the maximum number of nodes we explore till we reach end is k*k*k...*k, d times. So it's O(k^d).

# In double-ended BFS we finish when the forward and backward searches collide. Where do they collide? Approximately at d/2 distance. Let's call this point mid. So it's O(k^(d/2)) (start to mid) + O(k^(d/2)) (end to mid), yielding O(k^(d/2)). Yes, it's the same class of complexity of standard BFS, but for large graphs double-ended BFS may give you the right result waaaaaaay faste


he trick is use set to save the words at each level because different words could ladder to the same word. It was 2580ms using list.

alphabet = set('abcdefghijklmnopqrstuvwxyz')
def findLadders(self, start, end, dict):
    dict.add(end)
    level_tracker = collections.defaultdict(set)
    self.parents_tracker = {}
    last = {start}
    while last and end not in level_tracker:
        current = set([])
        level_tracker.clear()
        for word in last:
            for next_word in self.ladder(word, dict):
                if next_word not in self.parents_tracker:
                    current.add(next_word)
                    level_tracker[next_word].add(word)
        self.parents_tracker.update(level_tracker)
        last = current
    return [] if not last else self.generate_paths(start, end)
    
def ladder(self, word, dict):
    for i in xrange(len(word)):
        for letter in self.alphabet - {word[i]}:
            new_word = word[:i] + letter + word[i + 1:]
            if new_word in dict:
                yield new_word

def generate_paths(self, start, end):
    ret = [[end]]
    while ret[-1][0] != start:
        new_ret = []
        for path in ret:
            for parent in self.parents_tracker[path[0]]:
                new_ret.append([parent] + path)
        ret = new_ret
    return ret