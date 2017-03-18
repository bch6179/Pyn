# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        def isValidBST(self, root):
            """
            :type root: TreeNode
            :rtype: bool
            """

        def isValidBST2(self, root):
            self.lastVal = None
            self.isBST = True
            self.validate(root)
            return self.isBST

        def validate2(self, root):
            if root is None:
                return   # Travese mode, set global res, no return
            self.validate(root.left)
            if self.lastVal is not None and self.lastVal >= root.val:
                self.isBST = False
                return
            self.lastVal = root.val  #Mistake fogot set lastVal
            self.validate(root.right)
            
        def dfs(root, low, high):
            if root == None:
                return True
            if low != None or high != None:
                if high != None and root.val >= high.val or low != None and root.val <= low.val:
                    return False
            
            return dfs(root.left, low, TreeNode(root.val)) and dfs(root.right, TreeNode(root.val), high)
        
        
        maxv = 1 << 31 -1
        minv = -maxv - 1
        return dfs(root, None, None)