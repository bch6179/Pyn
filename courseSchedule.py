There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

from collections import defaultdict
#from set import Set
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, num_courses, prereq):
        if num_courses < 2:
            return True
        
        path = (list)
        for c in prereq:
            path[c[0]].append(c[1]) 
            #convert to adjacy list (not care topo at list moment)

        searched = set()
        for start in path.keys():
            if not self.dfs(path, set(), start, searched):
                return False
        return True

    def dfs(self, path, seen, curr, searched):
        if curr in searched:
            return True

        for x in path[curr]:
            if x in seen:
                return False

            seen.add(x)
            if not self.dfs(path, seen, x, searched):
                return False

            seen.remove(x)

        searched.add(curr)
        return True
        
def canFinish(self, numCourses, prerequisites):
    graph = [[] for _ in xrange(numCourses)]
    visit = [0 for _ in xrange(numCourses)]
    for x, y in prerequisites:
        graph[x].append(y)
    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True
    for i in xrange(numCourses):
        if not dfs(i):
            return False
    return True
if node v has not been visited, then mark it as 0.
if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.

def canFinish(self, n, pres):
    from collections import deque
    ind = [[] for _ in xrange(n)]  # indegree
    oud = [0] * n  # outdegree
    for p in pres:
        oud[p[0]] += 1
        ind[p[1]].append(p[0])
    dq = deque()
    for i in xrange(n):
        if oud[i] == 0:
            dq.append(i)
    k = 0
    while dq:
        x = dq.popleft()
        k += 1
        for i in ind[x]:
            oud[i] -= 1
            if oud[i] == 0:
                dq.append(i)
    return k == n


# 34 / 34 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# 99.68%
The topological sort is natural for this problem. We always take the courses with no unstudied prereqs and so on until no more courses we can take. The oud[i] is the number of prereqs for course i and indegree keep a list of courses require course i.