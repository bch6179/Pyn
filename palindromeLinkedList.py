from base import *

class Solution(object):
    def isPalindrome(self, head):
           
        fast = slow = head
        rev = None
        
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while slow and slow.val == rev.val:
            slow = slow.next
            rev = rev.next
        
        return not rev
            
O(n) time, O(1) space. The second solution restores the list after changing it.

Solution 1: Reversed first half == Second half?

Phase 1: Reverse the first half while finding the middle.
Phase 2: Compare the reversed first half with the second half.
 
Solution 2: Play Nice

Same as the above, but while comparing the two halves, restore the list to its original state by reversing the first half back. Not that the OJ or anyone else cares.

def isPalindrome(self, head):
    rev = None
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, head = head, rev, head.next
    tail = head.next if fast else head
    isPali = True
    while rev:
        isPali = isPali and rev.val == tail.val
        head, head.next, rev = rev, head, rev.next
        tail = tail.next
    return isPali
    
    def isPalindrome(self, head): # recursive timeout
        def helper(other, head):
            if not other:
                return True,head

            res = helper(other.next, head)
            
            return res[0] and other.val == res[1].val, res[1].next
            

        return helper(head,head)[0]
        
    def isPalindromeBad(self, head): #after reverse, head becomes a single node, although you copy to cur
        """
        :type head: ListNode
        :rtype: bool
        """
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        while head and prev and head != prev:
            if head.val != prev.val:
                return False
            if head.next == prev:
                break
            head = head.next
            prev = prev.next
        return True
s= Solution()
print s.isPalindrome(ListNode(1,ListNode(3,ListNode(3,ListNode(1)))))