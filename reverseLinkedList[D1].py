from base import *
def reverse(root): #? bad

    if  root.next == None:
        return root
    res = reverse(root.next)
    res.next = root
    root.next = None
    return res
def reverse2(root, tail = None):
    if root == None:
        return None
    next = root.next #Mistake should save to next, otherwise it become tail for next recursion
    root.next = tail
    if next is None:
        return root
    else:
        return reverse(next, root)
 
print reverse(ListNode(3, ListNode(5, ListNode(6))))