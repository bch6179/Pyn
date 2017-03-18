from base import *
from collections import deque

class Solution(object):
    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        prevQ = [root]
        res = []
        curQ = []
        while prevQ:
            list = []
            curQ = [] #Mistake both list and curQ should reset for next line
            for node in prevQ:
                list.append( node.val)
                if node.left:
                    curQ.append(node.left) #Mistake  not += 
                if node.right:
                    curQ.append(node.right)
            res.append(list)
            prevQ = curQ
        return res
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []
        queue = deque([root])
        res = []
        while queue:
            list = []
            num = len(queue)
            for i in range(num):
                node = queue.popleft()
                list.append( node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(list)
        return res
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(root, pos):
            if root == None: return
                
            res[h-pos-1].append(root.val)
            dfs(root.left, pos+1)
            dfs(root.right, pos+1)
        
        def getMaxDepth(root):
            if root == None: return 0
            return max(getMaxDepth(root.left), getMaxDepth(root.right)) + 1
        
        
        h = getMaxDepth(root)
        res = [[] for i in range(h)]
        dfs(root, 0)
        return res
s = Solution() 
print s.levelOrder(TreeNode(1,TreeNode(2), TreeNode(3)))