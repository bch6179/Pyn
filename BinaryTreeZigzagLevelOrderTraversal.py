# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None: return []  #if not check, q will pop None
        q = collections.deque([root]) ##Mistake deque init []
        r2l = False
        
        res = []
        while q:
            n = len(q)
            level = []
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if r2l:
                res.append(list(reversed(level)))
                
            else:
                res.append(list(level))
            r2l = not r2l
                
        return res
    def preorder(self, root, level, res):
        if root:
            if len(res) < level+1: res.append([])
            if level % 2 == 0: 
                res[level].append(root.val)
            else: 
            res[level].insert(0, root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
    def zigzagLevelOrder(self, root):
        self.results = []
        self.preorder(root, 0, self.results)
        return self.results