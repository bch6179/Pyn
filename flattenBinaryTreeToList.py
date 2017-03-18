
# each branch return . [root, right], connect right to left branch's returning head
# reverse thinking , do right first, return the head of right in self.prev, the left will connect it to its' right

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

from base import *
 
class Solution(object):
    def __init__(self):
        self.prev = None
    def flatten1(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return  
            
        self.flatten(root.right)    
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None #Mistake root.left = root.right
        self.prev = root
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None 
            
        left = root.left
        right = root.right
        self.flatten(left)
        self.flatten(right)   
        t = root.right
        root.right = root.left
        root.left = None

        prev = None 
        while  root.right:
            root = root.right
        root.right = t
 
s = Solution() 
root = TreeNode(1, left=TreeNode(2))
s.flatten(root)
print root

# class Solution {
# public:
#     void flatten(TreeNode *root) {
# 		TreeNode*now = root;
# 		while (now)
# 		{
# 			if(now->left)
# 			{
#                 //Find current node's prenode that links to current node's right subtree
# 				TreeNode* pre = now->left;
# 				while(pre->right)
# 				{
# 					pre = pre->right;
# 				}
# 				pre->right = now->right;
#                 //Use current node's left subtree to replace its right subtree(original right 
#                 //subtree is already linked by current node's prenode
# 				now->right = now->left;
# 				now->left = NULL;
# 			}
# 			now = now->right;
# 		}
#     }
# };

# se a pointer "pre", then pre order the tree.

# void flatten(TreeNode* root) {
#     if (!root) return;
#     TreeNode dummy(-1), *pre = &dummy;
#     flatten(root, pre);
# }

# void flatten(TreeNode* root, TreeNode* &pre) {
#     if (!root) return;
#     TreeNode *rightChild = root->right;
#     pre->right = root;
#     pre->left = NULL;
#     pre = root;
#     flatten(root->left, pre);
#     flatten(rightChild, pre);
# }

# it is DFS so u need a stack. Dont forget to set the left child to null, or u'll get TLE. (tricky!)

#    public void flatten(TreeNode root) {
#         if (root == null) return;
#         Stack<TreeNode> stk = new Stack<TreeNode>();
#         stk.push(root);
#         while (!stk.isEmpty()){
#             TreeNode curr = stk.pop();
#             if (curr.right!=null)  
#                  stk.push(curr.right);
#             if (curr.left!=null)  
#                  stk.push(curr.left);
#             if (!stk.isEmpty()) 
#                  curr.right = stk.peek();
#             curr.left = null;  // dont forget this!! 
#         }
#     }