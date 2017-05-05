
def findLWA(root, l, r):
    if not root or root == l or root == r:
        return root
    
    n1 = findLWA(root.left, l,r)
    n2 = findLWA(root.right,l,r)

    if n1 and n2:
        return root
    elif n1:
        return n1
    else:
        return n2
        





























        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4


题目大意：
给定一棵二叉树，寻找其中两个给定节点的最近公共祖先（LCA）。

根据维基百科对LCA的定义：“节点v与w的最近公共祖先是树T上同时拥有v与w作为后继的最低节点（我们允许将一个节点当做其本身的后继）”

例如，题目描述的样例中，节点5和1的最近公共祖先（LCA）是3。另一个例子，节点5和4的LCA是5，因为根据LCA的定义，一个节点可以是其本身的后继。

解题思路：
迭代法：
后序遍历二叉树，得到从根节点到目标节点的“路径”，两条路径公共部分的末尾节点即为LCA

Python代码：
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        pathP, pathQ = self.findPath(root, p), self.findPath(root, q)
        lenP, lenQ = len(pathP), len(pathQ)
        ans, x = None, 0
        while x < min(lenP, lenQ) and pathP[x] == pathQ[x]:
            ans, x = pathP[x], x + 1
        return ans
        
    def findPath(self, root, target):
        stack = []
        lastVisit = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and lastVisit != peek.right:
                    root = peek.right
                else:
                    if peek == target:
                        return stack
                    lastVisit = stack.pop()
                    root = None
        return stack