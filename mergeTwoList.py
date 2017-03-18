from base import *
class Solution(object):
    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        head = dummy
    
        while l1 and l2:
            if l1.val < l2.val:
                head.next = l1  # head = dummy.next, none has no next
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return dummy.next
  def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode4PM-5PM Feb 7 Tue
        :rtype: ListNode
        """
        if not l1:
            return l2
            
        if not l2:
            return l1
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2  
l1 = ListNode(1, ListNode(3,ListNode(5)) )
l2 = ListNode(2, ListNode(4, ListNode(6)))
s = Solution() 
print s.mergeTwoLists(l1,l2)

 