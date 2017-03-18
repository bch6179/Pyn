# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from base import *
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def dfs(head):
            if head == None: return None
            if head.next == None: return TreeNode(head.val)
            dummy = TreeNode(0)
            dummy.next = head #Mistake missing head, # if only two then slow.next will be none
            slow = dummy # we want to let the middle to be the root, so back slow one step, otherwise, slow is the middle
            fast = head
            while fast != None and fast.next != None:
                fast =fast.next.next
                slow = slow.next
            temp = slow.next
            slow.next = None
            node = TreeNode(temp.val)
            node.left = dfs(head)
            node.right = dfs(temp.next) #Mistake here duplicate temp
            return node
        return dfs(head)
 
s = Solution() 
print s.sortedListToBST(ListNode(1, ListNode(2, ListNode(3,ListNode(4)))))