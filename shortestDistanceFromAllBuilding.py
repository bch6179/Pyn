https://leetcode.com/problems/shortest-distance-from-all-buildings/#/description
ou want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.

Show Company Tags
Show Tags
Show Similar Problems


also tested the other three C++ solutions posted so far, they took 340-1812 ms. I think mine is faster because I don't use a fresh "visited" for each BFS. Instead, I walk only onto the cells that were reachable from all previous buildings. From the first building I only walk onto cells where grid is 0, and make them -1. From the second building I only walk onto cells where grid is -1, and I make them -2. And so on.

Good idea and very easy to understand,
and you can add only one line to improve your performance!

after each check of if(grid[i][j]==1){ } block
just add: if(mindist==-1) return -1; Because you don't have to traverse every block as long as you've already found some block that is not reachable.
And it only takes 20 ms.

I'd also say time complexity O(kmn), but space complexity can be regarded as O(mn). That's the most I ever use at any point in time. Otherwise, i.e., if you add up all memory ever possibly used, then for example traversals in a balanced binary search tree might not be O(log n) space but only O(n) space (there probably are better examples, it's just the first that came to my mind).

It could easily be made clearly O(mn) space, but that would just make the code uglier and not be interesting, in my opinion.

 

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
                        for i1,j1 in range((x+1,y),(x-1,y), (x,y-1),(x,y+1)):
                            if 0 <= i1 < nrow and grid[[i1][j1] == 0 and (i1,j1) not in visited:
                                dists[(i1, j1)] = dists.get((i1,j1), 0) + dist + 1
                                visited_nums[(i1,j1)] = visited_nums.get((i1,j1), 0) + 1
                                visited[(i1,j1)] = True
                                queue.append((i1,j1, dist+1))
                         
        
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
from collections import deque


class Solution(object):
    def shortestDistance(self, grid):
        def is_vaild(position):
            i, j = position
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == target

        def next(i, j):
            return filter(is_vaild, [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)])
            
        total = [row[:] for row in grid]  # Total distance accumlated for all buildings
        target = 0
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 1:
                    min_dist = -1
                    dist = [[0] * len(grid[0]) for _ in range(len(grid))]

                    queue = deque([(i, j)])
                    while queue:
                        r, c = queue.popleft() 
                        valids = next(r, c)

                        for nr, nc in valids:
                            grid[nr][nc] -= 1
                            dist[nr][nc] = dist[r][c] + 1
                            total[nr][nc] += dist[nr][nc]

                            # min_dist has to be a valid one
                            if min_dist == -1 or min_dist > total[nr][nc]:
                                min_dist = total[nr][nc]

                        queue.extend(valids)

                    # End of a visit from a building. Next time we will only visit the following target.
                    target -= 1
        return min_dist
3 months ago reply quote 

htly modified the code to copy input only once and use level in bfs. 22ms C++

    int shortestDistance(vector<vector<int>>& grid) {
        int m = grid.size(); 
        int n = grid[0].size();

        int mindist = INT_MAX;
        vector<vector<int>> distance(m, vector<int>(n,0));
        
        int target = 0;
        
        vector<vector<int>> dir {{1,0},{0,1}, {-1,0},{0,-1}};
        
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(grid[i][j] != 1) continue;
                
                mindist = INT_MAX;
                queue<pair<int,int>> q;
                q.emplace(i,j);
                int level = 1;
                while(!q.empty())
                {
                    int sz = q.size();
                    for(int k = 0; k < sz; k++)
                    {
                        auto curr = q.front();
                        q.pop();
                        for(auto &d : dir)
                        {
                            int a = curr.first+d[0];
                            int b = curr.second+d[1];
                            
                            if(a == m || b == n || a == -1 || b == -1) continue;
                            
                            if(grid[a][b] == target)
                            {
                                q.emplace(a,b);
                                grid[a][b]--;
                                distance[a][b] += level;
                                mindist = min(mindist, distance[a][b]);
                            }
                        }
                    }
                    level++;
                }
                target--;
            }
        }
        
        return mindist == INT_MAX ? -1 : mindist;
        
    }