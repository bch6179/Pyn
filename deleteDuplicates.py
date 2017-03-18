from base import *
 
class Solution(object):
    def deleteDuplicatesI(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Note : Change cur next pointer to next unique one or Null, 
        #       change cur to that one as new iteration point and repeat
        
        if head ==  None or head.next == None:
            return head
        
        cur = head
        while cur:
            p = cur.next
            while p != None and cur.val == p.val:
                p = p.next
            cur.next = p
            cur = p  #Mistake 
        return head
    def deleteDuplicates3(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Note :  forward, connect cur.next to next.net, if next is duplicated
      
        cur = head
        while cur and cur.next: 
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
                    
        return head
    def deleteDuplicates2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Note : Change cur next pointer to next unique one or Null, 
        #       change cur to that one as new iteration point and repeat
        
        if head ==  None or head.next == None:
            return head
        cur = head
        p = head.next
        while p: 
            if cur.val != p.val:
                cur.next = p
                cur = p
            else:
                p = p.next
                if p == None:
                    cur.next = None
                    
        return head
 
    def deleteDuplicatesII(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        while head and head.next:
            p = head.next.next
            flag = False
            while p and head.next.val == p.val:
                p = p.next
                flag = True
            if flag:
                head.next = p
                #head = p  #Mistake head should not set to p, otherwise, next 2 2 not able to delete
                flag = False
            else:
                head = head.next
        return dummy.next
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        flag = False
        p = head.next.next

        while head.next and  p:
            #1
            if   head.next.val == p.val:
                p = p.next  # 2
                flag = True
                if p == None:
                    head.next = p
            else:
                if flag:
                    head.next = p
                    p = p.next
                    #head = p  
                    #Mistake 2)heaed should not set to p, not able to delete 22 among [1,1, 2,2 ], 
                    # #Mistake 1) should not set  p in the begining #1, otherwise,  #2  not change anything
                    #can't move the position of p=p.next to the share place
                    flag = False
                else:
                    head = head.next
                    p = p.next

        return dummy.next
s = Solution() 
print s.deleteDuplicates(ListNode(1,ListNode(1, ListNode(2,ListNode(3)))))