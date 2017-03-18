
https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
Adjacency matrices

For a graph with |V| ∣V∣vertical bar, V, vertical bar vertices, an adjacency matrix is a   ∣V∣×∣V∣  matrix of 0s and 1s, 
uery whether edge (i,j) (i,j)left parenthesis, i, comma, j, right parenthesis is in the graph by looking at graph[i][j]. So what's the disadvantage of an adjacency matrix? Two things, actually. First, it takes (V^2)  space
Second, if you want to find out which vertices are adjacent to a given vertex i ii, you have to look at all |V|   entries in row i ii, even if only a small number of vertices are adjacent to vertex i ii.
Adjacency lists

ypically have an array of |V|  adjacency lists, one adjacency list per vertex. 
[ [1, 6, 8],
  [0, 4, 6, 9],
  [4, 6],
  [4, 5, 8],
  . To find out whether an edge (i,j) is present in the graph, 
  The answer is  Θ(d), where d   is the degree of vertex i 
V∣ lists, and although each list could have as many as |V|-1   vertices, in total the adjacency lists for an undirected graph contain 2|E| Why 2|E|  ? Each edge (i,j) (i,j)  appears exactly twice in the adjacency lists, once in i ii's list and once in j jj's list, and there are |E|  edges. For a directed graph, the adjacency lists contain a total of |E|   one element per directed edge.
var vertex = graph[i];
for (var j = 0; j < vertex.length; j++) {
    doStuff(vertex[j]);
}

undirected graph contain 2|E|  elements.