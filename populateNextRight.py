# 116. Populating Next Right Pointers in Each Node
# Given a binary tree

#     struct TreeLinkNode {
#       TreeLinkNode *left;
#       TreeLinkNode *right;
#       TreeLinkNode *next;
#     }
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Note:

# You may only use constant extra space.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# For example,
# Given the following perfect binary tree,
#          1
#        /  \
#       2    3
#      / \  / \
#     4  5  6  7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \  / \
#     4->5->6->7 -> NULL


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
from collections import deque
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None: return  
        q1 = deque([root]) #Mistake IF ROOT == nONE, q1 not None, q1.pop None.next wrong
        while q1:
            prev = None
            q2 = deque()
            while q1:
                node = q1.popleft() 
                node.next = prev
                prev = node
                if node.right:
                    q2.append(node.right)
                if node.left:
                    q2.append(node.left)
            q1 = q2


#             public void connect(TreeLinkNode root) {
#     if(root == null)
#         return;
        
#     if(root.left != null){
#         root.left.next = root.right;
#         if(root.next != null)
#             root.right.next = root.next.left;
#     }
    
#     connect(root.left);
#     connect(root.right);
# }

# Java solution with O(1) memory+ O(n) time
public class Solution {
    public void connect(TreeLinkNode root) {
        TreeLinkNode level_start=root;
        while(level_start!=null){
            TreeLinkNode cur=level_start;
            while(cur!=null){
                if(cur.left!=null) cur.left.next=cur.right;
                if(cur.right!=null && cur.next!=null) cur.right.next=cur.next.left;
                
                cur=cur.next;
            }
            level_start=level_start.left;
        }
    }
}