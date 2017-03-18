# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from base import *
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None: return False  #don't worry about root.right == None but sum is 0
            # if sum == 0:
            #     return True
            # else: return False
        elif  root.left == None and root.right == None:
            return sum == root.val 
        # elif  root.left == None:
        #     return hasPathSum(root.right, sum - root.val)
        # elif root.right == None:
        #     return hasPathSum(root.left, sum - root.val) 
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
s = Solution() 
node = TreeNode(1, left=TreeNode(1, right=TreeNode(1,left=TreeNode(3))), right=TreeNode(3))
print node
print s.hasPathSum(node, 3)