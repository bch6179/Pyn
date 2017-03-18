also tested the other three C++ solutions posted so far, they took 340-1812 ms. I think mine is faster because I don't use a fresh "visited" for each BFS. Instead, I walk only onto the cells that were reachable from all previous buildings. From the first building I only walk onto cells where grid is 0, and make them -1. From the second building I only walk onto cells where grid is -1, and I make them -2. And so on.

Good idea and very easy to understand,
and you can add only one line to improve your performance!

after each check of if(grid[i][j]==1){ } block
just add: if(mindist==-1) return -1; Because you don't have to traverse every block as long as you've already found some block that is not reachable.
And it only takes 20 ms.

I'd also say time complexity O(kmn), but space complexity can be regarded as O(mn). That's the most I ever use at any point in time. Otherwise, i.e., if you add up all memory ever possibly used, then for example traversals in a balanced binary search tree might not be O(log n) space but only O(n) space (there probably are better examples, it's just the first that came to my mind).

It could easily be made clearly O(mn) space, but that would just make the code uglier and not be interesting, in my opinion.

I also tested the other three C++ solutions posted so far, they took 340-1812 ms. I think mine is faster because I don't use a fresh "visited" for each BFS. Instead, I walk only onto the cells that were reachable from all previous buildings. From the first building I only walk onto cells where grid is 0, and make them -1. From the second building I only walk onto cells where grid is -1, and I make them -2. And so on.

int shortestDistance(vector<vector<int>> grid) {
    int m = grid.size(), n = grid[0].size();
    auto total = grid;
    int walk = 0, mindist, delta[] = {0, 1, 0, -1, 0};
    for (int i=0; i<m; ++i) {
        for (int j=0; j<n; ++j) {
            if (grid[i][j] == 1) {
                mindist = -1;
                auto dist = grid;
                queue<pair<int, int>> q;
                q.emplace(i, j);
                while (q.size()) {
                    auto ij = q.front();
                    q.pop();
                    for (int d=0; d<4; ++d) {
                        int i = ij.first + delta[d];
                        int j = ij.second + delta[d+1];
                        if (i >= 0 && i < m && j >= 0 && j < n && grid[i][j] == walk) {
                            grid[i][j]--;
                            dist[i][j] = dist[ij.first][ij.second] + 1;
                            total[i][j] += dist[i][j] - 1;
                            q.emplace(i, j);
                            if (mindist < 0 || mindist > total[i][j])
                                mindist = total[i][j];
                        }
                    }
                }
                walk--;
            }
        }
    }
    return mindist;
}


class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or grid[0] is None or len(grid[0]) == 0:
            return -1
        nrow, ncol = len(grid), len(grid[0])
        dists, visited_nums, building_num = {}, {}, 0
        min_dist = float("inf")
        
        for i, row in enumerate(grid):
            for j, ele in enumerate(row):
                if ele == 1:
                    building_num += 1
                    queue = collections.deque()
                    queue.append((i, j, 0))
                    visited = {}
                    while queue:
                        x, y, dist = queue.popleft()
                        if x+1 < nrow and grid[x+1][y] == 0 and (x+1, y) not in visited:
                            dists[(x+1, y)] = dists.get((x+1, y), 0) + dist + 1
                            visited_nums[(x+1, y)] = visited_nums.get((x+1, y), 0) + 1
                            visited[(x+1, y)] = True
                            queue.append((x+1, y, dist+1))
                        if x-1 >= 0 and grid[x-1][y] == 0 and (x-1, y) not in visited:
                            dists[(x-1, y)] = dists.get((x-1, y), 0) + dist + 1
                            visited_nums[(x-1, y)] = visited_nums.get((x-1, y), 0) + 1
                            visited[(x-1, y)] = True
                            queue.append((x-1, y, dist+1))
                        if y+1 < ncol and grid[x][y+1] == 0 and (x, y+1) not in visited:
                            dists[(x, y+1)] = dists.get((x, y+1), 0) + dist + 1
                            visited_nums[(x, y+1)] = visited_nums.get((x, y+1), 0) + 1
                            visited[(x, y+1)] = True
                            queue.append((x, y+1, dist+1))
                        if y-1 >= 0 and grid[x][y-1] == 0 and (x, y-1) not in visited:
                            dists[(x, y-1)] = dists.get((x, y-1), 0) + dist + 1
                            visited_nums[(x, y-1)] = visited_nums.get((x, y-1), 0) + 1
                            visited[(x, y-1)] = True
                            queue.append((x, y-1, dist+1))
        
        
        for x, y in dists:
            if dists[(x, y)] < min_dist and visited_nums[(x, y)] == building_num:
                min_dist = dists[(x, y)]
        
        if min_dist == float("inf"):
            return -1
        
        return min_dist

    
B
 
  1 out of 1   
Home   OJ   Shortest Distance from All Buildings   BFS Python Solution 
New users please read the instructions to format your code properly. Discuss is a place to post interview questions or share solutions / ask questions related to OJ problems.
BFS Python Solution

1
D danyang3 
Reputation:  1
 import sys

__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        acc = [[0 for _ in xrange(n)] for _ in xrange(m)]
        reachable = [[True for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] > 0:
                    reachable[i][j] = False
                    acc[i][j] = sys.maxint

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    self.bfs(grid, acc, reachable, i, j)

        mini = sys.maxint
        for i in xrange(m):
            for j in xrange(n):
                if acc[i][j] < mini and reachable[i][j]:
                    mini = acc[i][j]

        return mini if mini != sys.maxint else -1

    def bfs(self, grid, acc, reachable, x, y):
        d = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]

        q = [(x, y)]
        visited[x][y] = True  # enqueue, then visited
        while q:
            l = len(q)
            for idx in xrange(l):
                i, j = q[idx]
                acc[i][j] += d

                for dir in self.dirs:
                    I = i+dir[0]
                    J = j+dir[1]
                    if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and not visited[I][J]:
                        q.append((I, J))
                        visited[I][J] = True

            d += 1
            q = q[l:]

        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j]:
                    reachable[i][j] = False
about a year ago reply quote 
PYTHON 4.2k 1
POSTS 438
VIEWS Reply Back To Leetcode    Mark unread   Not Watching   Sort by 
