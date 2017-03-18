from base import *
def copynode(h):
    if not h: return None
    newhead = ListNode(h.val)
    newhead.next = copynode(h.next)

    return newhead
print copynode(ListNode(1, ListNode(2)))