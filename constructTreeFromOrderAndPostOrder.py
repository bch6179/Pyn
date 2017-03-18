from base import *
 
class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    # 12:00
 
    def buildTreeMy(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        if len(inorder) == 1 and len(postorder) > 0:
            t = postorder.pop() #Mistake val list, why t.val
            return TreeNode(t)
        v = postorder.pop()
        root = TreeNode(v) #Mistake, why val.right
        i = inorder.index(v)#Mistake, why index a root
        root.right  = self.buildTree(inorder[i+1:], postorder)  #Mistake [:i-1] mistake what are you thinking for the right, and ] right end is not included
        root.left = self.buildTree(inorder[:i], postorder)
        return root  
s = Solution() 
print s.buildTreeMy([1,3,2],[3,2,1])