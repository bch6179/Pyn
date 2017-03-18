# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from base import *
class Solution(object):
    def pathSum(self, root, sum):
        def dfs(root, sum,  list):
            if root != None: 
                sum -= root.val
                if root.left == None and root.right == None:
                    list.append(root.val) #Mistake this should be out of if sum ==0, so other branch 4
                    if sum == 0:                  
                        res.append(list[:])
                    list.pop() #Mistake list can only pop here, other wise [1,[2, [None, [3,[4],None]]]],  1,2 3 is skiped
                    return
                list.append(root.val)
                dfs(root.left, sum,   list)
                #Mistake no pop here
                dfs(root.right, sum,   list)
                if list: 
                    list.pop()
                    
        res = []
        dfs(root, sum, [])
        return res
    def pathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, sum, list, res):
            if root != None: 
                if root.left == None and root.right == None:
                    if sum == root.val:
                        list.append(root.val)
                        res.append(list)
                else:
                    dfs(root.left, sum-root.val, list+[root.val], res)
                    dfs(root.right, sum-root.val, list+[root.val], res)
                    
        res = []
        dfs(root, sum, [], res)
        return res
s = Solution() 
node = TreeNode(1, left=TreeNode(2, right=TreeNode(3,left=TreeNode(4))), right=TreeNode(6, right=TreeNode(6)))
nb =   TreeNode(1, left=TreeNode(2, right=TreeNode(3, left=TreeNode(4))), right=TreeNode(5, right=TreeNode(6)))
print s.pathSum(nb, 12)
print s.pathSum(nb, 12)