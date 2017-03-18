#[Note]
#=====
# Since stack is used to keep track of the parent of the predecessors, moris traversal reuse the leaf node 's right pointer to point to the parent. so find the predecessort (previous one in order) of the current node and make that link and then go left. Iterate.


from base import * 
# class TreeNode():
#     def __init__(self, val,left=None,right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#     def __repr__(self):
#         return """TreeNode(val=%r, left=%r, right=%r""" % (self.val, self.left, self.right)
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return []

        s = []
        res = []
        while root or s:
            if root:
                s.append(root)
                root = root.left
            elif s:
                root = s.pop()
                res.append(root.val)
                root = root.right
        return res
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def findPre(cur):
            pre = cur.left
            while pre.right and pre.right != cur:
                pre = pre.right
            return pre
                
        if root == None: return []

        res = []
        cur = root
        while cur:
            if not cur.left:  # cur is the leftmost
                res.append(cur.val) #pre is visited here
                cur = cur.right
            else:
                pre = findPre(cur)  # #Mistake when findPre also need to check the loop;
                #connect the rightmost of the left tree to current node for backtracing
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:                  #go back  // left subtree is done
                    pre.right = None
                    res.append(cur.val)  #move to right, after decting already visit the rightmost, move to the right of cur node, visit the cur not the pre
                    cur = cur.right #Mistake not got pre.right

        return res
s = Solution() 
#    1 
#  2
#    3
print s.inorderTraversal(TreeNode(1, left=TreeNode(2, right=TreeNode(3))))
              
            

