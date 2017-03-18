# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(head):
            prev = None
            count = 0
            while head:
                next= head.next 
                head.next = prev
                prev = head
                head = next
                count+=1
            
            return prev,count
        
        if not head or not head.next or not k:
            return head
            
        cur = head
        count = 0
        while cur: 
            count+=1
            cur = cur.next
        k = k % count
        if k == 0:
            return head
            
        head,count=reverse(head)
        p = head
     
        prev = None
        while k > 0 and p: #Mistake this not considerig k == 0, or single node case
            prev = p
            p = p.next
            k -= 1
        if  prev:
            prev.next = None
            
        newhead,_ = reverse(head)  #  k == 0, newhead is not the final head anymore
        newp,_ =reverse(p)
        head.next = newp
        
        return newhead
            
        