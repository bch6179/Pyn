
from base import *
 
class Solution(object):
    def buildTree( self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            rootVal = preorder.pop()
            root=TreeNode(rootVal)
            i = inorder.index(rootVal)
            root.left = self.buildTree(preorder, inorder[:i])
            root.right = self.buildTree(preorder, inorder[(i+1):]
            return root
s = Solution() 
print s.buildTree([],[])