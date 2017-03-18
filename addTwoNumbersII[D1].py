
This Python solution does not alter the input lists and it adheres to the object oriented principles. The idea is very simple:

Convert input linked lists into numbers using a converter that is linear
After converting them into ints, sum them like you would normally
Convert the new integer into a linked list using another converter that converts a number into linked list by calling str() on it.
return the head
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.linkedListToNum(l1)
        num2 = self.linkedListToNum(l2)
        summed = num1+num2
        return self.numToLinkedList(summed)
    
    def numToLinkedList(self, num):
        dummy = ListNode(None)
        curr = dummy
        for d in str(num):
            node = ListNode(int(d))
            curr.next = node
            curr = node
        return dummy.next
     
    def linkedListToNum(self, l):
        string = ""
        cur = l
        while cur:
            string += str(cur.val)
            cur = cur.next
        return int(string)

 Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def listToStack(node):
            stack = []
            while node:
                stack.append(node.val)
                node = node.next
            return stack
            
        def stackToList(stack):
            head = ListNode(resultStack.pop())
            last = head
            while stack:
                last.next = ListNode(stack.pop())
                last = last.next
            return head
            
        def addDigitStacks(s1, s2):
            result = []
            carry = 0
            while s1 or s2 or carry:
                d1 = s1.pop() if s1 else 0
                d2 = s2.pop() if s2 else 0
                d = d1 + d2 + carry
                result.append(d % 10)
                carry = d // 10
            return result
            
        s1 = listToStack(l1)
        s2 = listToStack(l2)
        resultStack = addDigitStacks(s1, s2)
        return stackToList(resultStack)

ublic class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> s1 = new Stack<Integer>();
        Stack<Integer> s2 = new Stack<Integer>();
        
        while(l1 != null) {
            s1.push(l1.val);
            l1 = l1.next;
        };
        while(l2 != null) {
            s2.push(l2.val);
            l2 = l2.next;
        }
        
        int sum = 0;
        ListNode list = new ListNode(0);
        while (!s1.empty() || !s2.empty()) {
            if (!s1.empty()) sum += s1.pop();
            if (!s2.empty()) sum += s2.pop();
            list.val = sum % 10;
            ListNode head = new ListNode(sum / 10);
            head.next = list;
            list = head;
            sum /= 10;
        }
        
        return list.val == 0 ? list.next : list;
    }
}
