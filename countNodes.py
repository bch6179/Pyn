Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getHeight(root):
            res = 0
            while root:
                res+=1
                root = root.left # Mistake right is not correct, 1->left is 1 
            return res
            
        if not root: return 0
        hl = getHeight(root.left)
        hr = getHeight(root.right)
         
        if hl == hr:
            return pow(2, hl) + self.countNodes(root.right) #Mistkake use pow not ^
        else:
            return pow(2,hr) + self.countNodes(root.left)


class Solution {

public:

    int countNodes(TreeNode* root) {

        if(!root) return 0;

        int hl=0, hr=0;

        TreeNode *l=root, *r=root;

        while(l) {hl++;l=l->left;}

        while(r) {hr++;r=r->right;}

        if(hl==hr) return pow(2,hl)-1;



        return 1+countNodes(root->left)+countNodes(root->right);

    }

};

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.lastcount = 0
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getHeight(root):
            h = 0
            while root:
                h+=1
                root = root.left
            return h
        def dfs(root, h, level):
            if level == h:
                self.lastcount += 1
                return
            dfs(root.left, h, level+1)
            dfs(root.right, h, level+1)
            
        if root == None: return 0
        h = getHeight(root)
        if h == 1: return 1
        
        dfs(root, h, 1)
        return pow(2, h-1)-1+self.lastcount
compare the depth between left sub tree and right sub tree.
A, If it is equal, it means the left sub tree is a full binary tree
B, It it is not , it means the right sub tree is a full binary tree

 class Solution:
        # @param {TreeNode} root
        # @return {integer}
        def countNodes(self, root):
            if not root:
                return 0
            leftDepth = self.getDepth(root.left)
            rightDepth = self.getDepth(root.right)
            if leftDepth == rightDepth:
                return pow(2, leftDepth) + self.countNodes(root.right)
            else:
                return pow(2, rightDepth) + self.countNodes(root.left)
    
        def getDepth(self, root):
            if not root:
                return 0
            return 1 + self.getDepth(root.left)
Concise Java iterative solution O((logn) ^ 2)

12
B BeaverNation 
Reputation:  10
Using the intrinsic property of binary tree to do a binary search. The image shows the meaning of variables in my code. In each loop, if the the total tree is complete, we add all the nodes and stop. If the left subtree is incomplete, add all nodes in the right subtree (plus the parent node) and let the left subtree be the new tree. If the left subtree is complete, add all nodes in the left subtree (plus the parent node) and let the right subtree be the new tree. The out loop run at most O(logn) and the inner loops for finding depths are also O(logn). So the total running time is O((logn)^2).



  public int countNodes(TreeNode root) {
        int sum = 0;

        while (root != null) {
            int llh = leftDepth(root.left);
            int lrh = rightDepth(root.left);
            int rrh = rightDepth(root.right);
            if (llh == rrh) {
                sum += (1 << llh + 1) - 1;
                break;
            } else if (llh > lrh) {
                sum += 1 << rrh;
                root = root.left;
            } else {
                sum += 1 << llh;
                root = root.right;
            }
        }
        return sum;
    }

    public int leftDepth(TreeNode root) {
        int h = 0;
        while (root != null) {
            root = root.left;
            h++;
        }
        return h;
    }

    public int rightDepth(TreeNode root) {
        int h = 0;
        while (root != null) {
            root = root.right;
            h++;
        }
        return h;
    }
    