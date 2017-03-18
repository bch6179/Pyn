https://leetcode.com/problems/binary-tree-upside-down/?tab=Description
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  


from base import *
 
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if not root or root.left == None: return root,root
            lRoot, rMost  =  dfs(root.left)
            rMost.left, rMost.right = root.right, TreeNode(root.val) #Mistake should use copy node,otherwise, 1->3 will hook after 2 right, we only need 1
            
            return lRoot, rMost.right
        res,_= dfs(root)
        return res
s = Solution() 
root = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
print s.upsideDownBinaryTree(root)
        # @param root, a tree node
        # @return root of the upside down tree
#     def upsideDownBinaryTree(self, root):
#         stack = []
#         while root:
#             stack.append(root)
#             root = root.left
#         dummy = TreeNode(None)
#         curr = dummy
#         while stack:
#             node = stack.pop()
#             curr.right = node
#             curr.left = node.right
#             curr = curr.right
#         curr.left = curr.right = None
#         return dummy.right

#         or nt =s .pop()
#  cur = nt
#         while s:
#                 t = poop()
#         def upsideDownBinaryTree(self, root):
#             # take care of the empty case
#             if not root:
#                 return root
#             # take care of the root
#             l = root.left
#             r = root.right
#             root.left = None
#             root.right = None
#             # update the left and the right children, form the new tree, update root
#             while l:
#                 newL = l.left
#                 newR = l.right
#                 l.left = r
#                 l.right = root
#                 root = l
#                 l = newL
#                 r = newR
#             return root
            
# def upsideDownBinaryTree(self, root):
#         if not root or not root.left:
#                 return root
        
#         def updown(root):
#             if not root or not root.left:
#                 return root,root
                
#             lRoot,rMost = updown(root.left)  
        
#             rMost.left  = root.right
#             root.left=None
#             root.right=None
#             rMost.right = root
            
            
#             return lRoot,rMost.right
        
#         result,rMost=updown(root)
#         return result
# 2 months ago reply quote 
# 0
# D daniel   @orbuluh
# Reputation:  -1
# @orbuluh I really like your solution!
# I am just curious about its time complexity.
# I think that the worst time complexity for the recursion part would be O(logN) (where n is the number of nodes) and the while loop part is also O(logN) for the worst case. Therefore, the time complexity is going to be O(logN).
# Am I understanding it correctly?

# need to admit that I totally didn't get how to do the "upside-down"

# After some struggling and googling, I saw the graph in binary tree representation of trees.

# It's not directly the same, but give me a sense of how to do it.

# The transform of the base three-node case is like below:

#                          Root                   L
#                          /  \                  /  \
#                         L    R                R   Root
# You can image you grab the L to the top, then the Root becomes it's right node, and the R becomes its left node.

# Knowing the base case, you can solve it recursively.

# How? You keep finding the left most node, make it upside-down, then make its parent to be its right most subtree recursively.

# Here is a small point to be noticed, when you connect the root to the right subtree, you need to make sure you are not copying the original root, otherwise it will become cyclic!

# def upsideDownBinaryTree(self, root):
#     if not root or not root.left:
#         return root
#     lRoot = self.upsideDownBinaryTree(root.left)
#     rMost = lRoot
#     while rMost.right:
#         rMost = rMost.right
#     root, rMost.left, rMost.right = lRoot, root.right, TreeNode(root.val)
#     return root

#     can also return rMost in each iteration such that you don't need to find rMost from the root every time.

# def upsideDownBinaryTree(self, root):
#         if not root or not root.left:
#                 return root
        
#         def updown(root):
#             if not root or not root.left:
#                 return root,root
                
#             lRoot,rMost = updown(root.left)  
            
#             rMost.left, rMost.right = root.right, TreeNode(root.val)
        #     return lRoot,rMost.right
        
        # result,rMost=updown(root)
        # return result