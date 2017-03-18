if input is a graph node already, dfs is best, dfs all the neighbors, add to path for each node, and set visited
otherwise, form a graph from the edges[]
  #dfs mark connected points as visited
  #if isolated new point, add 1 for next dfs

* quick union
s is 1D version of Number of Islands II. For more explanations, check out this 2D Solution.

n points = n islands = n trees = n roots.
With each edge added, check which island is e[0] or e[1] belonging to.
If e[0] and e[1] are in same islands, do nothing.
Otherwise, union two islands, and reduce islands count by 1.
Bonus: path compression can reduce time by 50%.
Hope it helps!

The complexity for M quick union + path compression on N objects should be N + MlgN, I think in this problem, M = 2E, N = V, so O(V + 2ElgV), correct me if this is wrong @yavinci