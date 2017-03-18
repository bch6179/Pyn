from base import *
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def getLen(head):
            count = 0
            while head:
                count+=1
                head = head.next
            return count
        # def helper(head, num):
        #     if n % 2 == 1 and num == n/2 + 1:
        #         return (True, None)
        #     if n % 2 == 0 and num = n/2:
        #         return (True, head) 
        #     res, num, last = helper(head.next, num+1)
        #     if res == False: return False, 0, None
            
        #     if  n % 2 == 1 and num == n/2+1:
        #             return True, num+1, last
        #     elif n % 2 == 0 and num == n/2:
                
        #     if root.val == last.val:
        #         return True, num+1, last.next
        #     else:
        #         return False, 0, None
        def helper(head, length):
            if head == None or length == 0:
                return True, None
            elif length == 1:
                return True, head.next
            elif length == 2:
                return head.val == head.next.val, head.next.next
            res, last = helper(head.next, length - 2)
            if res == False: return False, None
            return last.val == head.val, last.next


        def helper2(head, cur):
            if head == None:
                return True, cur
            
            res, cur = helper(head.next,cur)
            if res == False: return False, None
            res = (head.val == cur.val)
            if res:
                cur = cur.next
            return res, cur 
            
            
        
        cur =head
        #res,_ = helper(head, cur)
        res, _ = helper(head, getLen(head))
        return res
s = Solution() 
print s.isPalindrome(ListNode(1,ListNode(3, ListNode(3,ListNode(1)))))