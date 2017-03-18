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
from   base import *
 
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def getLength(head):
            i = 0
            while head:
                i+=1
                head = head.next
            return i
        def dfs(l, r, curObj):
            #if curObj[0] == None: return None
            if l == r: return None
            if l+1 == r: 
                t = TreeNode(curObj[0].val) #Mistake val not object
                curObj[0]= curObj[0].next #Mistake forgot this?
                return t
            t = TreeNode(0)
            m = l + (r-l)/2
            t.left = dfs(l, m, curObj)
            t.val = curObj[0].val #Mistake the order matters, since last val used in left already
            curObj[0] = curObj[0].next  # always go to the middel, and then back tracking to build up, if only 1,2
            

            t.right = dfs(m+1, r, curObj)  ##Mistake overwritten the 3 root node .next , left
            return t
            
        def dfs2(head):
            if head == None: return None
            if head.next == None: 
                t = TreeNode(head.val)
            dummy = TreeNode(0)
            dummy.next = head #Mistake missing head
            slow = dummy
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
        n = getLength(head)
        return dfs(0,n, [head])
s = Solution() 
print s.sortedListToBST(ListNode(1, ListNode(3)))