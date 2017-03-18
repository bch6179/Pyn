
class Solution(object):
    def __init_(self):
        self.index = 0
    def dfs1(nums, left, right): # like preorder traversal, use implicit stack the root is set in the right of the second dfs branch
        #after cur not stasfy the calls through first branch, it will trace back to second branch
        #if invalid occur, the process will get stuck, otherwise until min, max level
        if self.index < len(nums) and nums[self.index] > left and nums[self.index] < right:
            t = nums[self.index]
            self.index += 1
            self.dfs1(nums, left, t )
            self.dfs1(nums, t, right )

    def verifyPreorder2Stacks(self, nums):
        stack = []
        inorder = [] #reverse of the roots of the visited left subtree
        for p in nums:
            if inorder and p < inorder[-1]:  #case 1, p must greater than the root of the left tree if inorder not empty
            # equal: min otherwise the root of current tree ; after visiting left tree, nums[l] becomes the low , i.e, stack last pop
                return False
            while stack and stack[-1] < p: #see an ascending one could be in the left tree or up the right
                inorder.append(stack.pop()) #when stack is empty after popping, start the right tree; otherwise, start the right tree of the left tree
            stack.append(p)   #stack all the roots of the left subtree, where the right of the each root not visited yet;keep stacking until seeing a upper one and pop then start upper one as next iteration 
    def verifyPreorder(self, nums):
        if len(nums) <= 0: return True
        i = 0
        self.dfs1(nums, float('-inf'),float('inf'))
        return self.index == len(nums)

    def verifyPreorder2(self, nums): 
        def dfs(nums, l, r): #verify that the left tree elems < root < right tree elems, and then recursively verify left and right subtree
            if l >= r: # use nums l as leftmost then scan to the rightmost, so no need to pass cur
                return True

            root = nums[l]
            rightRootIndex = -1
            for i in range(l+1, r+1): #Mistake  should not be len(nums), but r
                if nums[i] > root:  #verify left trees valid and find right most
                    rightRootIndex = i #Mistake for index should be i instead of rightRootIndex, otherwise the init -1 doesn't work
                    break 
            if rightRootIndex != -1: #verify right trees valid
                for i in range(rightRootIndex+1, r+1):
                     if nums[i] <= root: # Mistake comparing to root, not nums[rightRootIndex]:
                         return False
                if dfs(nums, l+1, rightRootIndex-1): #Mistake why use not
                    return dfs(nums, rightRootIndex, r) #Mistake should be rightRoot instead of rightRootIndex+1
                return False
            else:
                return  dfs(nums, l+1, r ) 
          
               
          
        return dfs(nums, 0, len(nums)-1)
        # def dfs(nums,  low, hi):
        #     res = False
        #     if i < len(nums) and low < nums[i] < hi:
        #         root = nums[i]
        #         j = i+1  #rightRoot index
        #         while j < len(nums) and nums[j] < root:
        #             j += 1
        #         if j > i+1:
        #             res=dfs(nums, i+1, low, root)
        #         if res and j < len(nums):
        #             return dfs(nums, j, root, high)
        #         return False
            
        #return dfs(nums,  loat('-inf'),float('inf'))
s = Solution() 
nums = [3,2,1,5,4,6]
print s.verifyPreorder(nums)

#   public boolean verifyHelper(int[] preorder, int l, int r){
#         if(l >= r)  return true;
         
#         int rightRoot = -1;
#         int root = preorder[l];
#         for(int i = l+1; i <= r; i++){
#             if(preorder[i] > root){
#                 rightRoot = i;
#                 break;
#             }
#         }
         
#         if(rightRoot != -1){
#             for(int i = rightRoot; i <=r; i++){
#                 if(preorder[i] <= root){
#                     return false;
#                 }
#             }
#         }
         
#         if(rightRoot == -1) return verifyHelper(preorder, l+1, r);
#         if(!verifyHelper(preorder, l+1, rightRoot-1)) return false;
#         return verifyHelper(preorder, rightRoot, r);
#     }
# }

# olution 2 ... O(1) extra space

# Same as above, but abusing the given array for the stack.

# public boolean verifyPreorder(int[] preorder) {
#     int low = Integer.MIN_VALUE, i = -1;
#     for (int p : preorder) {
#         if (p < low)
#             return false;
#         while (i >= 0 && p > preorder[i])
#             low = preorder[i--];
#         preorder[++i] = p;
#     }
#     return true;
# }
# Solution 3 ... Python

# Same as solution 1, just in Python.

# def verifyPreorder(self, preorder):
#     stack = []
#     low = float('-inf')
#     for p in preorder:
#         if p < low:
#             return False
#         while stack and p > stack[-1]:
#             low = stack.pop() # low is the root value of current right subtree, must less than that in above check
#         stack.append(p)
#     return True

# same logic, use one more stack to be easier to understand
# Basically this is how to recover inorder sequence from preorder sequence of a BST.

# public boolean verifyPreorder(int[] preorder) {
#     Stack<Integer> stack = new Stack<>();
#     Stack<Integer> inorder = new Stack<>();
    
#     for(int v : preorder){
#         if(!inorder.isEmpty() && v < inorder.peek())
#             return false;
#         while(!stack.isEmpty() && v > stack.peek()){
#             inorder.push(stack.pop());
#         }
#         stack.push(v);
#     }
#     return true;
# # } 