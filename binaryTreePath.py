# Given a binary tree, return all root-to-leaf paths.

# For example, given the following binary tree:

#    1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:

# ["1->2->5", "1->3"]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from base import *
 
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        def dfs(root, path):
            if root == None:
                return   
            if not root.left and not root.right:
                res.append( path+str(root.val))
                return  
            dfs(root.left, path+str(root.val)+'->' ) 
            dfs(root.right, path+str(root.val)+'->' )
   
        dfs(root, '')
        return res
    # dfs + stack
def binaryTreePaths1(self, root):
    if not root:
        return []
    res, stack = [], [(root, "")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.right:
            stack.append((node.right, ls+str(node.val)+"->"))
        if node.left:
            stack.append((node.left, ls+str(node.val)+"->"))
    return res
    
# bfs + queue
def binaryTreePaths2(self, root):
    if not root:
        return []
    res, queue = [], collections.deque([(root, "")])
    while queue:
        node, ls = queue.popleft()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.left:
            queue.append((node.left, ls+str(node.val)+"->"))
        if node.right:
            queue.append((node.right, ls+str(node.val)+"->"))
    return res
    
# dfs recursively
def binaryTreePaths(self, root):
    if not root:
        return []
    res = []
    self.dfs(root, "", res)
    return res

def dfs(self, root, ls, res):
    if not root.left and not root.right:
        res.append(ls+str(root.val))
    if root.left:
        self.dfs(root.left, ls+str(root.val)+"->", res)
    if root.right:
        self.dfs(root.right, ls+str(root.val)+"->", res)
    def binaryTreePaths-Mybad(self, root):
        res = []
        def dfs(root):
            if root == None:
                return   
            if not root.left and not root.right:
                res.append( str(root.val)) #Mistake each leaf nodes will be extended later event not on the same path
                return  
            dfs(root.left ) 
            dfs(root.right )
            for e in res:
                 res.append(str(root.val)+'->'+e)  # #Mistake res will infinitely be extended
        dfs(root)
        return res
s = Solution() 
root = TreeNode(1, left=TreeNode(2), right=TreeNode(3, right=TreeNode(5)))
print s.binaryTreePaths(root)