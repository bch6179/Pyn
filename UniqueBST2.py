Similar to merge sort, after dividing to smaller subproblems, combine them with the chosen root based on BST left right subtree structure recursively
/**
 * Given n, <strong>generate</strong> all structurally unique BST's (binary
 * search trees) that store values 1...n.
 * 
 * For example,
 * Given n = 3, your program should return all 5 unique BST's shown below
 * 
 *    1         3     3      2      1
 *     \       /     /      / \      \
 *      3     2     1      1   3      2
 *     /     /       \                 \
 *    2     1         2                 3
 * 
 * Tags: Tree, DP, Backtracking
 */
def generateTrees(self, n):
    def node(val, left, right):
        node = TreeNode(val)
        node.left = left
        node.right = right
        return 
        #map comprehension
    def trees(first, last):
        return [node(root, left, right)
                for root in range(first, last+1)
                for left in trees(first, root-1)
                for right in trees(root+1, last)] or [None]
    return trees(1, n)

        def dfs(self, start, end):
            if start == end+1:
            return 
        result = []
        for i in xrange(start, end+1):
            for l in self.dfs(start, i-1):
                for r in self.dfs(i+1, end):
                    node = TreeNode(i)
                    node.left, node.right  = l, r
                    result.append(node)
        return result 

         def dfsMy(l , r):
            res = []
            if start == end+1: #Mistake here should end+1 , pass the last check point
                return None
                
            for i in range(1, n+1):
                l1 = dfs(l, i-1)
                l2  = dfs( i+1, r)
                for x in l1:
                    for y in l2:
                        root = ListNode(i) #Mistake why put root here

                        root.left = x
                        root.right = y
                        res.append(root)
                        
            return res or [None]
        
        #return dfs(1, n)
                


class UniqueBST2 {
    public static void main(String[] args) {
        
    }
    
    /**
     * 1..n is the in-order traversal for any BST with nodes 1 to n. 
     * if pick i-th node as root
     * the left subtree will contain elements 1 to (i-1)
     * and the right subtree will contain elements (i+1) to n. 
     * use recursive calls to get back all possible trees for left and right 
     * subtrees and combine them in all possible ways with the root.
     */
    public List<TreeNode> generateTrees(int n) {
        return genTrees(1, n);
    }
    
    public List<TreeNode> genTrees (int start, int end) {
        List<TreeNode> list = new ArrayList<TreeNode>();
        if (start > end) { // base case
            list.add(null);
            return list;
        }
        
        List<TreeNode> left, right;
        for (int i = start; i <= end; i++) { // pick ith node from start to end
            left = genTrees(start, i - 1); // list of left subtree
            right = genTrees(i + 1, end); // list of right subtree
            for (TreeNode lnode : left) {
                for (TreeNode rnode: right) {
                    /*there exists a combination for each tree*/
                    TreeNode root = new TreeNode(i);
                    root.left = lnode; // attach root of left subtree
                    root.right = rnode; // attach root of right subtree
                    list.add(root); // add tree to result
                }
            }
        }
        return list;
    }
}
