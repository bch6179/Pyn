  he algorithm runs in O((M+N) log* N) where M is the number of operations ( unite and find ), N is the number of objects, log* is iterated logarithm while the naive runs in O(MN).

For our problem, If there are N positions, then there are O(N) operations and N objects then total is O(N log*N), when we don't consider the O(mn) for array initialization.
log2(2^65536) = 65536 = 2^16
log2(65536) = 16
log2(16) = 4
log2(4) = 2
log2(2) = 1
So log*(2^65536) = 5.
ave the same concern as you. In Introduction to Algorithm, they use weighting (or more precisely, rank) as the height of tree. Here, the size of the set is used.

In Introduction to Algorithm, the complexity is stated as O(m\alpha(n)), where alpha(n) is a very slowly growing function that its value will not exceed 4 in practice purpose (Page 574).
Note that log*N is almost constant (for N = 265536, log*N = 5) in this universe, so the algorithm is almost linear with N.

However, if the map is very big, then the initialization of the arrays can cost a lot of time when mn is much larger than N. In this case we should consider using a hashmap/dictionary for the underlying data structure to avoid this overhea

Python (using dict)

class Solution(object):
    def numIslands2(self, m, n, positions):
        ans = []
        islands = Union()
        for p in map(tuple, positions):
            islands.add(p)
            for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in islands.id:
                    islands.unite(p, q)
            ans += [islands.count]
        return ans

class Union(object):
    def __init__(self):
        self.id = {}
        self.sz = {}
        self.count = 0

    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1

    def root(self, i):
        while i != self.id[i]:
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return
        if self.sz[i] > self.sz[j]:
            i, j = j, i
        self.id[i] = j
        self.sz[j] += self.sz[i]
        self.count -= 1

        e, we can put all the functionality into the Solution class which will make the code a lot shorter. But from a design point of view a separate class dedicated to the data sturcture is more readable and reusable.
        onfused on log*: it means the number of times that we need to take log (base 2) on a number to make it become 1

        It is N = 2**65536, log*N = 5
log*(n) is the function that counts the times it takes doing log() to get to 1.
Here when N = 2**65536, log(log(log(log(log(N)))))=1, it takes 5 log functions, so log*N = 5
  
   int rootNb = findIsland(roots, idNb);
    root = findIsland(roots, root);
    if(root != rootNb) {        // if neighbor is in another island
        roots[root] = rootNb;   // union two islands 
        count--;               
    }
This will make your program much faster, since before this it could easily make depth very large

There can be at least two improvements: union by rank & path compression. However I suggest first finish the basis, then discuss the improvements.

Cheers!

int[][] dirs = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};

public List<Integer> numIslands2(int m, int n, int[][] positions) {
    List<Integer> result = new ArrayList<>();
    if(m <= 0 || n <= 0) return result;

    int count = 0;                      // number of islands
    int[] roots = new int[m * n];       // one island = one tree
    Arrays.fill(roots, -1);            

    for(int[] p : positions) {
        int root = n * p[0] + p[1];     // assume new point is isolated island
        roots[root] = root;             // add new island
        count++;

        for(int[] dir : dirs) {
            int x = p[0] + dir[0]; 
            int y = p[1] + dir[1];
            int nb = n * x + y;
            if(x < 0 || x >= m || y < 0 || y >= n || roots[nb] == -1) continue;
            
            int rootNb = findIsland(roots, nb);
            if(root != rootNb) {        // if neighbor is in another island
                roots[root] = rootNb;   // union two islands 
                root = rootNb;          // current tree root = joined tree root
                count--;               
            }
        }

        result.add(count);
    }
    return result;
}

public int findIsland(int[] roots, int id) {
    while(id != roots[id]) id = roots[id];
    return id;
}
PATH COMPRESSION (BONUS)

If you have time, add one line to shorten the tree. The new runtime becomes: 19ms (95.94%).

public int findIsland(int[] roots, int id) {
    while(id != roots[id]) {
        roots[id] = roots[roots[id]];   // only one line added
        id = roots[id];
    }
    return id;
}

h just Wikipedia's Disjoint-set forests, using "union by rank" and "path compression". I don't see the point of m and n, so I ignore them.

def numIslands2(self, m, n, positions):
    parent, rank, count = {}, {}, [0]
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            if rank[x] < rank[y]:
                x, y = y, x
            parent[y] = x
            rank[x] += rank[x] == rank[y]
            count[0] -= 1
    def add((i, j)):
        x = parent[x] = i, j
        rank[x] = 0
        count[0] += 1
        for y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if y in parent:
                union(x, y)
        return count[0]
    return map(add, positions)
Too bad Python 2 doesn't have nonlocal yet, hence the somewhat ugly count[0] "hack". Here's a different way:

def numIslands2(self, m, n, positions):
    parent, rank = {}, {}
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        x, y = find(x), find(y)
        if x == y:
            return 0
        if rank[x] < rank[y]:
            x, y = y, x
        parent[y] = x
        rank[x] += rank[x] == rank[y]
        return 1
    counts, count = [], 0
    for i, j in positions:
        x = parent[x] = i, j
        rank[x] = 0
        count += 1
        for y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if y in parent:
                count -= union(x, y)
        counts.append(count)
    return counts

     island has a main position. For a position p of some island, main[p] tells that main position. And for a main position p, land[p] tells all positions of that island. When combining islands, always add the smaller to the larger. I think this makes it O(P log P), where P is the number of positions. With about 230 ms, it is a bit faster than my union+find solutions.

def numIslands2(self, m, n, positions):
    counts, main, land = [], {}, {}
    for i, j in positions:
        p = i, j
        main[p], land[p] = p, [p]
        for q in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if q in main:
                p, q = main[p], main[q]
                if p != q:
                    if len(land[p]) < len(land[q]):
                        p, q = q, p
                    land[p] += land[q]
                    for l in land.pop(q):
                        main[l] = p
        counts += len(land),
    return counts