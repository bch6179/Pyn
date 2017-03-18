to maintain the information about the two scenarios for each tree root,
rob(root) does not distinguish between these two cases, so "information is lost as the recursion goes deeper and deeper", which results in repeated subprobl

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def rob(self, root):
        def dfs(node):
            if node is None:
                return (0,0)
            l = dfs(node.left)
            r = dfs(node.right)
            return (l[1]+r[1], max(l[1]+r[1], l[0]+r[0]+node.val))  #not include root, include root
 
        return dfs(root)[1]

       public int rob(TreeNode root) {
    int[] res = robSub(root);
    return Math.max(res[0], res[1]);
}

private int[] robSub_MyBad(TreeNode root) {
    if (root == null) return new int[2];
    
    int[] left = robSub(root.left);
    int[] right = robSub(root.right);
    int[] res = new int[2];

    res[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
    res[1] = root.val + left[0] + right[0];
    
    return res; 


    # def rob(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     def helper(root):
    #         if root == None: return 0
    #         ll, l = 0,0
            
    #         while root:
    #             ll, l = l, max(l, root.val+ll)
    #             root = root.left if root.left else root.right #Mistake  one parent not mean only if left else root.right
    #         return l
    #     if root == None: return 0
    #     t1 = root.val + max(helper(root.left.left) if root.left else 0, helper(root.right.right) if root.right else 0)
    #     t2 = max(helper(root.left  if root.left else root.right), helper(root.right  if root.right else root.left))
    #     return max(t1,t2)