# AC Python O(1) space solution 12 lines and easy to understand
# The algorithm is a BFS or level order traversal. We go through the tree level by level. node is the pointer in the parent level, tail is the tail pointer in the child level.
# The parent level can be view as a singly linked list or queue, which we can traversal easily with a pointer.
# Connect the tail with every one of the possible nodes in child level, update it only if the connected node is not nil.
# Do this one level by one level. The whole thing is quite straightforward.

# Python


def connect(self, node):
    tail = dummy = TreeLinkNode(0)
    while node:
        tail.next = node.left
        if tail.next:
            tail = tail.next
        tail.next = node.right
        if tail.next: #Mistake not adjust tail to the rightmost, so that for right subtree, it's not connected to the previous 
            tail = tail.next
        node = node.next
        if not node:
            tail = dummy
            node = dummy.next
