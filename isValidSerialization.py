#check final position for validity
#if seeing #, no stacking, means no continuing until finish current iteration
#Mistake not BST , just tree

class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        
        l = len(preorder)
        
        def _isValid(root_index):
            if root_index >= l:
                return l
            
            if preorder[root_index] == '#':
                return root_index
            
            left_end = _isValid(root_index + 1)
            right_end = _isValid(left_end + 1)
            
            return right_end
        
        return _isValid(0) == l - 1
        class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        # remember how many empty slots we have
        # non-null nodes occupy one slot but create two new slots
        # null nodes occupy one slot
        
        p = preorder.split(',')
        
        #initially we have one empty slot to put the root in it
        slot = 1
        for node in p:
            
            # no empty slot to put the current node
            if slot == 0:
                return False
                
            # a null node?
            if node == '#':
                # ocuppy slot
                slot -= 1
            else:
                # create new slot
                slot += 1
        
        #we don't allow empty slots at the end
        return slot==0

        ee detailed comments below. Time complexity is O(n), space is also O(n) for the stack.

# public class Solution {
#     public boolean isValidSerialization(String preorder) {
#         // using a stack, scan left to right
#         // case 1: we see a number, just push it to the stack
#         // case 2: we see #, check if the top of stack is also #
#         // if so, pop #, pop the number in a while loop, until top of stack is not #
#         // if not, push it to stack
#         // in the end, check if stack size is 1, and stack top is #
#         if (preorder == null) {
#             return false;
#         }
#         Stack<String> st = new Stack<>();
#         String[] strs = preorder.split(",");
#         for (int pos = 0; pos < strs.length; pos++) {
#             String curr = strs[pos];
#             while (curr.equals("#") && !st.isEmpty() && st.peek().equals(curr)) {
#                 st.pop();
#                 if (st.isEmpty()) {
#                     return false;
#                 }
#                 st.pop();
#             }
#             st.push(curr);
#         }
#         return st.size() == 1 && st.peek().equals("#");
#     }
# }
s = Solution() 
print s.isValidSerialization("3,2,1,#,#,#,#,5,#,#,#")