from base import *
try:
    from Queue import *  # ver. < 3.0
except ImportError:
    from queue import *

def mergeTwoLists_recursion(l1, l2):
    if l1 == None: #Mistake not or then return None, otherwise miss one [1 3 ] [2 4], or even test [3] [4]
        return l2
    if l2 == None:
        return l1
    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2
def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1 #Mistake cur is None at the begining, cur = dummy, not cur = dummy.next
            cur = cur.next
            l1 = l1.next
        else:
            cur.next = l2
            cur = cur.next
            l2 = l2.next
    if not l1:
        cur.next = l2
    if not l2:
        cur.next = l1
    return dummy.next



def mergeKsortedList_countCmpNumber(list):
    k = len(list) - 1

    while k > 0:
        start = 0
        end = k
        while start < end:
            list[start] = mergeTwoLists(list[start], list[end])
            start += 1
            end -= 1
            if (start >= end):
                k = end
    return list[0]
def mergeKsortedList(list):
    if list == None or not list: return None #Mistake [] != None, only not [] is true
    n = len(list)
    if n == 1: return list[0]
   # if n == 2: return mergeTwoLists(list[0], list[1])
    n = n/2
    res= mergeTwoLists(mergeKsortedList(list[:n]), mergeKsortedList(list[n:])) # list[:] should make a copy already
     #Mistake right recursion mergeKsortedList infi loop for list [ [node]] when n = 1, mergeKsortedList( return mergeKsortedList()) if another is None)
   #if n == 2, n/2 = 1, n == 3
    return res


def mergeKsortedList_DivideAndConquer(list):
    return helper(list, 0, len(list)-1)

def helper(list, start, end):
    if (start == end):
        return list[start]

    m = start + (end-start)/2
    l1 = helper(list, start, m)
    l2 = helper(list, m+1, end)
    return mergeTwoLists(l1, l2) #[Note]
    #===== return linked node, so no worry about the start end; and also start <= end, since mid  <= end, not like i++ j--
from heapq import * #import * mistake
class Solution(object):
    def mergeKListsMy(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #if not lists or len(lists) == 0: return None
        #if len(lists) == 1: return lists[0]
        
        h = []
        
        for l in lists:
            if l: #mistake here 
                heappush(h, (l.val, l))
        dummy = ListNode(0)
        head = dummy
        while  h:
            _, t = heappop(h)
            head.next = t
            head = head.next
            if t.next:
                heappush(h, (t.next.val, t.next)) #Mistake here miss one ), so report wrong error for next line
        
        return dummy.next
        
from heapq import *

def mergeKsortedList1(list):
    heap = []
    for head in list:
        if head:
            heappush(heap, (head.val, head))
    dummy = ListNode(0)
    cur = dummy
    while heap != []:
        _, t = heappop(heap) 
        cur.next = t
        cur = cur.next
        if t.next:
            heappush(heap, (t.next.val, t.next))
    return dummy.next
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #if not lists or len(lists) == 0: return None
        #if len(lists) == 1: return lists[0]
        
        h = Q.PriorityQueue()
        
        for l in lists:
            if l: #mistake here 
                h.put((l.val, l))
        dummy = ListNode(0)
        head = dummy
        while  not h.empty(): #h.qsize() > 0:
            t = h.get()[1]
            head.next = t
            head = head.next
            if t.next:
                h.put((t.next.val, t.next)) #Mistake here miss one ), so report wrong error for next line
        
        return dummy.next
def mergeKsortedList2(list):
    heap = PriorityQueue()
    for head in list:
        heap.put((head.val, head))
    dummy = ListNode(0) #Mistake qsize() need ()
    cur = dummy
    while heap.qsize() > 0:  #Mistake  no len for queue
        t = heap.get()[1] 
        cur.next = t
        cur = cur.next
        if t.next:
            heap.put((t.next.val, t.next))
    return dummy.next
mylist = []
mylist.append(ListNode(1, tnext=ListNode(3)))
mylist.append(ListNode(4,tnext=ListNode(7)))
mylist.append(ListNode(2,tnext=ListNode(8)))

print mergeKsortedList(mylist)