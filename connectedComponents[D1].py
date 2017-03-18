class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def dfs(self, x, tmp):
        self.v[x.label] = True
        tmp.append(x.label)
        for node in x.neighbors:
            if not self.v[node.label]:
                self.dfs(node, tmp)
            
    def connectedSet(self, nodes):
        # Write your code here
        self.v = {}
        for node in nodes:
            self.v[node.label] = False
        ret = []
        for node in nodes:
            if not self.v[node.label]:
                tmp = []
                self.dfs(node, tmp)
                ret.append(sorted(tmp))
        return ret

#quick union
public int countComponents(int n, int[][] edges) {
    int[] roots = new int[n];
    for(int i = 0; i < n; i++) roots[i] = i; 

    for(int[] e : edges) {
        int root1 = find(roots, e[0]);
        int root2 = find(roots, e[1]);
        if(root1 != root2) {      
            roots[root1] = root2;  // union
            n--;
        }
    }
    return n;
}

public int find(int[] roots, int id) {
    while(roots[id] != id) { //find root of id
        roots[id] = roots[roots[id]];  // optional: path compression
        id = roots[id];
    } //https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
    return id;
}
public class QuickUnion
{
private int[] id;
public QuickUnion(int N)
{
 id = new int[N];
for (int i = 0; i < N; i++) id[i] = i;
}
private int root(int i)
{
while (i != id[i]) i = id[i];
return i;
}
public boolean find(int p, int q)
{
return root(p) == root(q);
}
public void unite(int p, int q)
{
int i = root(p);
 int j = root(q);
 id[i] = j;
}
}
FS:

def countComponents(n, edges):
        def dfs(n, g, visited):
            if visited[n]:
                return
            visited[n] = 1
            for x in g[n]:
                dfs(x, g, visited)
                
        visited = [0] * n
        g = {x:[] for x in xrange(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ret = 0
        for i in xrange(n):
            if not visited[i]:
                dfs(i, g, visited)     #dfs mark connected points as visited
                ret += 1               
                
        return ret
BFS:

def countComponents(n, edges):
        g = {x:[] for x in xrange(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ret = 0
        for i in xrange(n):
            if not g: break
            queue = [i]
            ret += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]

        return ret
Union Find:

def countComponents(n, edges):
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(xy):
            x, y = map(find, xy)
            if rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1
        
        parent, rank = range(n), [0] * n
        map(union, edges)
        return len({find(x) for x in parent})
