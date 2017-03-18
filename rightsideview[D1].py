from base import *
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs1(root):
            if root == None:
                return
            res.append(root.val)
            if root.right:
                dfs(root.right)
            else:
                dfs(root.left)  #Mistake overlook the case of lower level of left tree [1 2 3 4]
        def dfs(root, level):
            if root == None:
                return
            res[level] = root.val
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        # res = collections.defaultdict(lambda:0)
        # dfs(root,0)
        # return list(res.itervalues())          
        def bfs(root):
            if root == None:
                return
            list = [root]
            next = []
            
            while list:
                res.append(list[-1].val)
                next = []
                for n in list:#Mistake why use root for n  [1 2]
                    if n.left:
                        next.append(n.left)
                    if n.right:
                        next.append(n.right)
                list = next
            
        res = []
        bfs(root)
        return res

s = Solution() 
print s.rightSideView(TreeNode(1, left=TreeNode(2)))