# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from base import *
#Mistake loop prevention
#PRESET tHE END OF the ordered list to None, so that no loop
# if in order, tmp.next is None, tmp.next will point to cur as recovering
# but we gain the effect of saving tracking prev node to connect after it moved out 
class Solution(object):
    def insertionSortListAC(self, head):
            """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head
        cur = head.next
        head.next = None
        while cur:
            tmp = dummy
            while tmp.next != None and tmp.next.val <= cur.val:
                tmp = tmp.next
            next = cur.next
            cur.next = tmp.next
            tmp.next = cur
            cur = next
        return dummy.next
    def insertionSortListBad(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        prev = dummy
        dummy.next = head
        cur = head.next
        prev = dummy
        while cur:
            tmp = dummy
            while tmp.next != cur and tmp.next.val <= cur.val:
                tmp = tmp.next
            if tmp.next == cur: continue
            next = cur.next
            if tmp.next.val > cur.val:
                cur.next = tmp.next
                tmp.next = cur
                prev.next = next
            else:
                prev = cur
            cur = next
            
        return dummy.next
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #3->2->1->4
        
        def mergeSort(head):
            if head == None or head.next == None:
                return head
            
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            second = slow.next
            slow.next = None
            
            l = mergeSort(head)
            r = mergeSort(second)
            return merge(l,r)
        def merge(l,r):
            if l == None:
                return r
            if r == None:
                return l
            dummy = ListNode(0)
            cur = dummy
            while l and r:
                if l.val < r.val:
                    cur.next = l
                    l = l.next
                else:
                    cur.next = r
                    r = r.next
                cur = cur.next #Mistake how can you foget next to cur and not test out
            if l:
                    cur.next = l
            if r:
                cur.next =r
            return dummy.next
                    
        def mergeDfs(l, r):
            if l == None:
                return r
            if r == None:
                return l
            if l.val < r.val:
                l.next = merge(l.next, r)
                return l
            else:
                r.next = merge(l, r.next)
                return r
        return mergeSort(head)
#print s.sortList(ListNode(2, ListNode(1)))
s = Solution()
print s.insertionSortList(ListNode(2,ListNode(1)))


if (head == null || head.next == null) return head;
        ListNode dummy = new ListNode(Integer.MIN_VALUE);
        dummy.next = head;
        ListNode cur = head.next;
        head.next = null;  //important,  1-> 1->null , 3-2-4-null
        while (cur != null) {
            ListNode tmp = dummy;
            while (tmp.next != null && tmp.next.val <= cur.val) tmp = tmp.next;
            ListNode next = cur.next;
            cur.next = tmp.next;
            tmp.next = cur;
            cur = next;
        }
        return dummy.next;
    }
def insertionSortList(self, head):
    cur = dummy = ListNode(0)
    while head:
        if cur and cur.val > head.val: # reset pointer only when new number is smaller than pointer value
            cur = dummy
        while cur.next and cur.next.val < head.val: # classic insertion sort to find position
            cur = cur.next
        cur.next, cur.next.next, head = head, cur.next, head.next # insert
    return dummy.next



public ListNode insertionSortList(ListNode head) {
		if( head == null ){
			return head;
		}
		
		ListNode helper = new ListNode(0); //new starter of the sorted list
		ListNode cur = head; //the node will be inserted
		ListNode pre = helper; //insert node between pre and pre.next
		ListNode next = null; //the next node will be inserted
		//not the end of input list
		while( cur != null ){
			next = cur.next;
			//find the right place to insert
			while( pre.next != null && pre.next.val < cur.val ){
				pre = pre.next;
			}
			//insert between pre and pre.next
			cur.next = pre.next;
			pre.next = cur;
			pre = helper;
			cur = next;
		}
		
		return helper.next;
	}
































          