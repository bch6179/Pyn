#  you have an array from a post-order traversal of a BST, you know that the root is the last element of the array. The left child of the root takes up the first part of the array, and consists of entries smaller than the root. Then follows the right child, consisting of elements larger than the root. (Both children may be empty).

# ________________________________
# |             |              |R|
# --------------------------------
#  left child     right child   root
# So the main problem is to find the point where the left child ends and the right begins.

# Both children are also obtained from their post-order traversal, so constructing them is done in the same way, recursively.

BST fromPostOrder(value[] nodes) {
    // No nodes, no tree
    if (nodes == null) return null;
    return recursiveFromPostOrder(nodes, 0,  nodes.length - 1);
}

// Construct a BST from a segment of the nodes array
// That segment is assumed to be the post-order traversal of some subtree
private BST recursiveFromPostOrder(value[] nodes, 
                                   int leftIndex, int rightIndex) {
    // Empty segment -> empty tree
    if (rightIndex < leftIndex) return null;
    // single node -> single element tree
    if (rightIndex == leftIndex) return new BST(nodes[leftIndex]);

    // It's a post-order traversal, so the root of the tree 
    // is in the last position
    value rootval = nodes[rightIndex];

    // Construct the root node, the left and right subtrees are then 
    // constructed in recursive calls, after finding their extent
    BST root = new BST(rootval);

    // It's supposed to be the post-order traversal of a BST, so
    // * left child comes first
    // * all values in the left child are smaller than the root value
    // * all values in the right child are larger than the root value
    // Hence we find the last index in the range [leftIndex .. rightIndex-1]
    // that holds a value smaller than rootval
    int leftLast = findLastSmaller(nodes, leftIndex, rightIndex-1, rootval);

    // The left child occupies the segment [leftIndex .. leftLast]
    // (may be empty) and that segment is the post-order traversal of it
    root.left = recursiveFromPostOrder(nodes, leftIndex, leftLast);

    // The right child occupies the segment [leftLast+1 .. rightIndex-1]
    // (may be empty) and that segment is the post-order traversal of it
    root.right = recursiveFromPostOrder(nodes, leftLast + 1, rightIndex-1);

    // Both children constructed and linked to the root, done.
    return root;
}

// find the last index of a value smaller than cut in a segment of the array
// using binary search
// supposes that the segment contains the concatenation of the post-order
// traversals of the left and right subtrees of a node with value cut,
// in particular, that the first (possibly empty) part of the segment contains
// only values < cut, and the second (possibly empty) part only values > cut
private int findLastSmaller(value[] nodes, int first, int last, value cut) {

    // If the segment is empty, or the first value is larger than cut,
    // by the assumptions, there is no value smaller than cut in the segment,
    // return the position one before the start of the segment
    if (last < first || nodes[first] > cut) return first - 1;

    int low = first, high = last, mid;

    // binary search for the last index of a value < cut
    // invariants: nodes[low] < cut 
    //             (since cut is the root value and a BST has no dupes)
    // and nodes[high] > cut, or (nodes[high] < cut < nodes[high+1]), or
    // nodes[high] < cut and high == last, the latter two cases mean that
    // high is the last index in the segment holding a value < cut
    while (low < high && nodes[high] > cut) {

        // check the middle of the segment
        // In the case high == low+1 and nodes[low] < cut < nodes[high]
        // we'd make no progress if we chose mid = (low+high)/2, since that
        // would then be mid = low, so we round the index up instead of down
        mid = low + (high-low+1)/2;

        // The choice of mid guarantees low < mid <= high, so whichever
        // case applies, we will either set low to a strictly greater index
        // or high to a strictly smaller one, hence we won't become stuck.
        if (nodes[mid] > cut) {
            // The last index of a value < cut is in the first half
            // of the range under consideration, so reduce the upper
            // limit of that. Since we excluded mid as a possible
            // last index, the upper limit becomes mid-1
            high = mid-1;
        } else {
            // nodes[mid] < cut, so the last index with a value < cut is
            // in the range [mid .. high]
            low = mid;
        }
    }
    // now either low == high or nodes[high] < cut and high is the result
    // in either case by the loop invariants
    return high;



def construct(nums, l ,r):

    if l > r: return None
    i = r-1
    while i >= l:
        if nums[i] < nums[r]:
            break
    
    root = TreeNode(nums[r])
    root.left = construct(nums, l, i)
    root.right = construct(nums, i+1, r-1)
    return root