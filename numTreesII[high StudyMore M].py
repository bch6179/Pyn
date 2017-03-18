# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        return self.dfs(1, n)
    
    
    def dfs(self, start, end): 
        #rtype: return list of Nodes
        if start > end: return [None] # Great
        res = []
        for rootval in range(start, end+1):
            res1 = self.dfs(start, rootval-1)
            res2 = self.dfs(rootval+1, end)
            for left in res1:
                for right in res2:
                    node = TreeNode(rootval) #Mistake new node should be here, otherwise creating only one
                    node.left = left
                    node.right = right
                    res.append(node)
        return res
        