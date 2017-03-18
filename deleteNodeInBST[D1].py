# Idea:

# Binary Search. If key < root.val, change left child to the returned new tree. Do the opposite if key > root.val.
# When found the node, put right child of the node to the end of the right most leaf node of left child. That way the values are still in order.
# Return the left child of the node(skip root, a.k.a delete it). If the node doesn't have left child, return right child.
# This solution always runs in O(log(n)) time since when it finds the node to delete, it goes to the right most leaf to put right subtree there.

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        
        if root.val == key:
            if root.left:
                left_right_most = root.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                left_right_most.right = root.right
                
                return root.left
            else:
                return root.right
                
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root



# I have a slightly different version, while handling in the event of node being found, instead of calling recursion again I handle it right away, this makes my running time faster


# Steps:

# Recursively find the node that has the same value as the key, while setting the left/right nodes equal to the returned subtree
# Once the node is found, have to handle the below 4 cases
# node doesn't have left or right - return null
# node only has left subtree- return the left subtree
# node only has right subtree- return the right subtree
# node has both left and right - find the minimum value in the right subtree, set that value to the currently found node, then recursively delete the minimum value in the right subtree
# public TreeNode deleteNode(TreeNode root, int key) {
#     if(root == null){
#         return null;
#     }
#     if(key < root.val){
#         root.left = deleteNode(root.left, key);
#     }else if(key > root.val){
#         root.right = deleteNode(root.right, key);
#     }else{
#         if(root.left == null){
#             return root.right;
#         }else if(root.right == null){
#             return root.left;
#         }
        
#         TreeNode minNode = findMin(root.right);
#         root.val = minNode.val;
#         root.right = deleteNode(root.right, root.val);
#     }
#     return root;
# }

# private TreeNode findMin(TreeNode node){
#     while(node.left != null){
#         node = node.left;
#     }
#     return node;
# }
#  public TreeNode deleteNode(TreeNode root, int key) {
#         if (root == null) return null;
        
#         if (root.val > key) {
#             root.left = deleteNode(root.left, key);
#         } else if (root.val < key) {
#             root.right = deleteNode(root.right, key);
#         } else {
#             if (root.left == null) return root.right;
#             if (root.right == null) return root.left;
            
#             TreeNode rightSmallest = root.right;
#             while (rightSmallest.left != null) rightSmallest = rightSmallest.left;
#             rightSmallest.left = root.left;
#             return root.right;
#         }
#         return root;
#     }