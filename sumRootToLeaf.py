https://leetcode.com/problems/sum-root-to-leaf-numbers/?tab=Description
 
 Sum Root to Leaf Numbers Add to List
Description  Submission  Solutions
Total Accepted: 101791
Total Submissions: 287022
Difficulty: Medium
Contributors: Admin
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.res = 0
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
    
        def dfs(root, pv):
            if not root: return 
            if not root.left and not root.right:
                self.res +=  pv*10+root.val 
                return
            dfs(root.left, pv*10+root.val)
            dfs(root.right, pv*10+root.val)
            
        dfs(root, 0)
        return self.res
        
        