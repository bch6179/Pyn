# Definition for a undirected graph node
from collections import deque
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return None
        
        q= deque() #can't put node into deque init, not iterable
        q.append(node) 
        head = UndirectedGraphNode(node.label)
        map = {}
        map[node] = head
        while q:
            node = q.popleft()
            for n in node.neighbors:
                if n not in map:
                    map[n] = UndirectedGraphNode(n.label)
                    q.append(n)
                map[node].neighbors.append(map[n])
                        
        return head
    def cloneGraphBad(self, node):
            if not node: return None       
        q= deque() #can't put node into deque init, not iterable
        q.append(node) 
        map = {}
        head = node
        while q:
            node = q.popleft()
            if node not in map:  #bad here 
                copy = UndirectedGraphNode(node.label)
                map[node] = copy
                for n in node.neighbors:
                    if n not in map:
                      map[n] = UndirectedGraphNode(n.label)
                    copy.neighbors.append(map[n])
                    q.append(n)
        return map[head]
    # def cloneGraphDFS(self, node):
    #     def dfs(node, dict):
            
    #         if not node:
    #             return None
                
    #         copy = None
    #         if node not in dict:    
    #             copy = UndirectedGraphNode(node.label)
    #             dict[node] = copy
    #             for n in node.neighbors:
    #                 copy.neighbors.append(dfs(n, dict))
    #         else:
    #             copy = dict[node]
    #         return copy
    #     dict = {}
    #     return dfs(node, dict)


    
   def cloneGraph(self, node):
         
        def dfs(node, dict):
            
            if not node:
                return None
                
            copy = None
            if node not in dict:    
                copy = UndirectedGraphNode(node.label)
                dict[node] = copy
                for n in node.neighbors:
                    copy.neighbors.append(dfs(n, dict))
            else:
                copy = dict[node]
            return copy
        dict = {}
        return dfs(node, dict)    