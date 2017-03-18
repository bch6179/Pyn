"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        stack = []
        res = []
        cur = root
        prev = None
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                peek = stack[len(stack) - 1]
                #if peek and (peek.left != prev):
                if (peek.right != None) and (peek.right != prev):
                    cur = peek.right
                else:
                    res.append(peek.val)
                    stack.pop()
                    prev = peek
                    