import sys
class Solution(object):
    def __init__(self):
        self.maxSum = -sys.maxsize-1
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if root == None: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            ml = max(0, left )
            mr = max(0, right )
            
        
            self.maxSum = max(self.maxSum,ml+mr+root.val) #no need to compare left, and right, since for leaf node maxSum is already saved
            return  max(ml,mr)+root.val #so the returned value is to compute next connected path
            
            
        dfs(root)
        return self.maxSum
s= Solution()
s.maxPathSum()     
        # test [-1], [1,2,3]