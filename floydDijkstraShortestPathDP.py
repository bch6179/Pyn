Floyd-Warshall algorithm in Python

The code below implements the Floyd-Warshall algorithm in Python. As with my Dijkstra post, I tried to write the code as literal to the algorithm and simple as possible. Floyd-Warshall algorithm finds for a graph the shortest path from any vertex to any vertex.


def floydwarshall(graph):
 
    # Initialize dist and pred:
    # copy graph into dist, but add infinite where there is
    # no edge, and 0 in the diagonal
    dist = {}
    pred = {}
    for u in graph:
        dist[u] = {}
        pred[u] = {}
        for v in graph:
            dist[u][v] = 1000
            pred[u][v] = -1
        dist[u][u] = 0
        for neighbor in graph[u]:
            dist[u][neighbor] = graph[u][neighbor]
            pred[u][neighbor] = u
 
    for t in graph:
        # given dist u to v, check if path u - t - v is shorter
        for u in graph:
            for v in graph:
                newdist = dist[u][t] + dist[t][v]
                if newdist < dist[u][v]:
                    dist[u][v] = newdist
                    pred[u][v] = pred[t][v] # route new path through t
 
    return dist, pred
 
 
 
graph = {0 : {1:6, 2:8},
         1 : {4:11},
         2 : {3: 9},
         3 : {},
         4 : {5:3},
         5 : {2: 7, 3:4}}
 
dist, pred = floydwarshall(graph)
print &quot;Predecesors in shortest path:&quot;
for v in pred: print &quot;%s: %s&quot; % (v, pred[v])
print &quot;Shortest distance from each vertex:&quot;
for v in dist: print &quot;%s: %s&quot; % (v, dist[v])
 
 
 
 
 
python floydwarshall.py 
Predecesors in shortest path:
0: {0: -1, 1: 0, 2: 0, 3: 2, 4: 1, 5: 4}
1: {0: -1, 1: -1, 2: 5, 3: 5, 4: 1, 5: 4}
2: {0: -1, 1: -1, 2: -1, 3: 2, 4: -1, 5: -1}
3: {0: -1, 1: -1, 2: -1, 3: -1, 4: -1, 5: -1}
4: {0: -1, 1: -1, 2: 5, 3: 5, 4: -1, 5: 4}
5: {0: -1, 1: -1, 2: 5, 3: 5, 4: -1, 5: -1}
Shortest distance from each vertex:
0: {0: 0, 1: 6, 2: 8, 3: 17, 4: 17, 5: 20}
1: {0: 1000, 1: 0, 2: 21, 3: 18, 4: 11, 5: 14}
2: {0: 1000, 1: 1000, 2: 0, 3: 9, 4: 1000, 5: 1000}
3: {0: 1000, 1: 1000, 2: 1000, 3: 0, 4: 1000, 5: 1000}
4: {0: 1000, 1: 1000, 2: 10, 3: 7, 4: 0, 5: 3}
5: {0: 1000, 1: 1000, 2: 7, 3: 4, 4: 1000, 5: 0}


def popmin(pqueue):
    # A (ascending or min) priority queue keeps element with
    # lowest priority on top. So pop function pops out the element with
    # lowest value. It can be implemented as sorted or unsorted array
    # (dictionary in this case) or as a tree (lowest priority element is
    # root of tree)
    lowest = 1000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest
 
def dijkstra(graph, start):
    # Using priority queue to keep track of minium distance from start
    # to a vertex.
    pqueue = {} # vertex: distance to start
    dist = {}   # vertex: distance to start
    pred = {}   # vertex: previous (predecesor) vertex in shortest path
 
    # initializing dictionaries
    for v in graph:
        dist[v] = 1000
        pred[v] = -1
    dist[start] = 0
    for v in graph:
        pqueue[v] = dist[v] # equivalent to push into queue
 
    while pqueue:
        u = popmin(pqueue) # for priority queues, pop will get the element with smallest value
        for v in graph[u].keys(): # for each neighbor of u
            w = graph[u][v] # distance u to v
            newdist = dist[u] + w
            if (newdist < dist[v]): # is new distance shorter than one in dist?
                # found new shorter distance. save it
                pqueue[v] = newdist
                dist[v] = newdist
                pred[v] = u
 
    return dist, pred
 
graph = {0 : {1:6, 2:8},
1 : {4:11},
2 : {3: 9},
3 : {},
4 : {5:3},
5 : {2: 7, 3:4}}
 
dist, pred = dijkstra(graph, 0)
print "Predecesors in shortest path:"
for v in pred: print "%s: %s" % (v, pred[v])
print "Shortest distance from each vertex:"
for v in dist: print "%s: %s" % (v, dist[v])
 
python dijkstra.py
Predecesors in shortest path:
0: -1
1: 0
2: 0
3: 2
4: 1
5: 4
Shortest distance from each vertex:
0: 0
1: 6
2: 8
3: 17
4: 17
5: 20