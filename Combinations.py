# /**
#  * Given two integers n and k, return all possible combinations of k numbers
#  * out of 1 ... n.
#  * 
#  * For example,
#  * If n = 4 and k = 2, a solution is:
#  * [
#  *   [2,4],
#  *   [3,4],
#  *   [2,3],
#  *   [1,2],
#  *   [1,3],
#  *   [1,4],
#  * ]
#  * 
#  * Tags: Backtracking
#  */


 class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def dfs(n, k, lst,pos):
            if k == 0:  #Note easier to do the k, instead of position check
                res.append(lst[:])
                return
            i = pos
            for i in range(pos, n+1): 
                lst.append(i)
                dfs(n, k-1, lst, i+1)
                lst.pop()
        def dfs1(n, k, lst, pos):
     
      
            if len(lst) == k:
                res.append(lst[:])
                return
            if pos > n: return # has to be here, [1,4] pos = 5 and 3,4 too for 3 can't let pos =n,
            i = pos
            for i in range(pos, n+1): #Mistake no need to optimize here n-k...,optimize cause problem
                lst.append(i)
                dfs1(n, k, lst, i+1)
                lst.pop()
        res = []
        dfs(n, k, [] , 1) #Mistake pos start from 1
        return res
s = Solution() 
print s.combine(20,16)

from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1, n+1), k))
But doing it yourself is more interesting, and not that hard. Here's a recursive version.

class Solution:
    def combine(self, n, k):
        if k == 0:
            return \[\[\]\]
        return [pre + [i] for i in range(1, n+1) for pre in self.combine(i-1, k-1)]
Iterative - AC in 76 ms

And here's an iterative one.

class Solution:
    def combine(self, n, k):
        combs = \[\[\]\]
        for _ in range(k):
            combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
        return combs
Reduce - AC in 76 ms

Same as that iterative one, but using reduce instead of a loop:

class Solution:
  def combine(self, n, k):
    return reduce(lambda C, _: [[i]+c for c in C for i in range(1, c[0] if c else n+1)],
                  range(k), \[\[\]\])