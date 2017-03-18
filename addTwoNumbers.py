# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return """ListNode(val=%r, next=%r""" % (self.val, self.next)


class LinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, val):     
        temp = ListNode(val)
        temp.next = self.head
        self.head = temp
       
    def print(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next

#http://www.geeksforgeeks.org/add-two-numbers-represented-by-linked-lists/
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        head = dummy 
        carry = 0
        
        result = LinkedList()
        while l1 is not None or l2 is not None:
            a,b = 0,0
            if l1 is not None:
                a = l1.val 
                l1 = l1.next
            if l2 is not None:
                b = l2.val
                l2 = l2.next
            sum = a+b+carry
            carry =  sum//10
            result.push(sum%10)
            

        if carry != 0:
            result.push(1)

         
        # prev = None
        
        # while head is not None:
        #     next =head.next
        #     head.next = prev
        #     prev = head
        #     head = next
            
        # return prev
        return result


l1 = LinkedList()
l1.push(3)
l1.push(4)
l1.push(2)
l2 = LinkedList()
l2.push(4)
l2.push(6)
l2.push(5)


s = Solution()
result = s.addTwoNumbers(l1.head, l2.head)
result.print()