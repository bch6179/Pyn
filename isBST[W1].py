from collections import namedtuple
Result = namedtuple("Result", "hight isBST")
 
    
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res, _ = self.dfs(root)
        return res 
        
    def dfs(self, root):
        if root == None: 
            return Result(  True, 0)
        
        isBST, h1  = self.dfs(root.left)
        if (not isBST): return False, 0
        isBST, h2  = self.dfs(root.right)
        if (not isBST): return False, 0

        return abs(h1 - h2) <= 1 ,max(h1,h2) + 1