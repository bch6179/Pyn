# Given a binary tree, find all leaves and then remove those leaves. Then repeat the previous steps until the tree is empty.

# Example:
# Given binary tree 
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Returns [4, 5, 3], [2], [1].

def findLeaves(self, root):
    def dfs(node):
        if not node:
            return -1
        i = 1 + max(dfs(node.left), dfs(node.right))  #leaf, hight is 0, stored here
        if i == len(out):
            out.append([])
        out[i].append(node.val)
        return i
    out = []
    dfs(root)
    return out

# 下面这种DFS方法没有用计算深度的方法，而是使用了一层层剥离的方法，思路是遍历二叉树，找到叶节点，将其赋值为NULL，然后加入leaves数组中，这样一层层剥洋葱般的就可以得到最终结果了：

 

# 解法二：

# 复制代码
# class Solution {
# public:
#     vector<vector<int>> findLeaves(TreeNode* root) {
#         vector<vector<int>> res;
#         while (root) {
#             vector<int> leaves;
#             root = remove(root, leaves);
#             res.push_back(leaves);
#         }
#         return res;
#     }
#     TreeNode* remove(TreeNode *node, vector<int> &leaves) {
#         if (!node) return NULL;
#         if (!node->left && !node->right) {
#             leaves.push_back(node->val);
#             return NULL;
#         }
#         node->left = remove(node->left, leaves);
#         node->right = remove(node->right, leaves);
#         return node;
#     }
# };