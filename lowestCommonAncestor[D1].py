  def lowestCommonAncestor(self, root, A, B):
        if root is None:
            return None
            
        if root is A or root is B:
            return root
            
        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)
        
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right
        return None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None or p == None or q == None: return None
        if(root.val > p.val and root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)
            elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root;
        
    
        # if p.val > q.val: 
        #     self.lowestCommonAncestor(root, q, p)
            
        # if root.val == p.val or root.val == q.val: return root
        
        # if root.val > p.val and root.val < q.val: #Not identify the BST property #Mistake > <, not test [2,1,3] # not identify the other way of comparing
        #     return root
        # elif root.val > q.val:
        #     return self.lowestCommonAncestor(root.left, q, p)
        # elif root.val < p.val:
        #     return self.lowestCommonAncestor(root.right, q, p)
        