  Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.


https://leetcode.com/problems/reorder-list/?tab=Description

 def reorderList(self, head):
        if not head:
        return
        
    # find the mid point
    slow = fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half in-place
    pre, node = None, slow
    while node:
        pre, node.next, node = node, pre, node.next  #slow.next is set to None here
    
    # Merge in-place; Note : the last node of "first" and "second" are the same
    first, second = head, pre
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
    return 


    # Splits in place a list in two halves, the first half is >= in size than the second.
# @return A tuple containing the heads of the two halves
def _splitList(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
        fast = fast.next

    middle = slow.next
    slow.next = None

    return head, middle

# Reverses in place a list.
# @return Returns the head of the new reversed list
def _reverseList(head):

  last = None
  currentNode = head

  while currentNode:
    nextNode = currentNode.next
    currentNode.next = last
    last = currentNode
    currentNode = nextNode

  return last

# Merges in place two lists
# @return The newly merged list.
def _mergeLists(a, b):

    tail = a
    head = a

    a = a.next
    while b:
        tail.next = b
        tail = tail.next
        b = b.next
        if a:
            a, b = b, a
            
    return head

ame up with a very similar code, but in the second while loop I wrote pre, node, node.next = node, node.next, pre instead of pre, node.next, node = node, pre, node.next. Why does switching the order of assignment matter here? I thought Python evaluated the entire right side before doing any assignment at all?

8 months ago reply quote 
0
C cmc   @cmc
Reputation:  147
You are right that the right hand side would be evaluated first. But then it will assign these value/objects to those on the left hand side one by one. In your code, the original node.next will be assign to the new node first, and then the original pre will be assigned to the NEW node.next since node has already been assigned to a new object.
   The recursive idea have been posted by yucheng.wang. Given a example, 1->2->3->4->5, the solution will reorder node(3), then reorder 2 and 4 to have (2->4->3), then 1 and 5 get have 1->5->2->4->3. Each call of reorderList(ListNode* head, int len) will return the last element after this reorderList() call.

int getLength(ListNode *head){
int len = 0;
while( head != NULL ){
++len; head = head->next;
}
return len;
}

ListNode * reorderList(ListNode *head, int len){
    if(len == 0)
        return NULL;
    if( len == 1 )
        return head;
    if( len == 2 )
        return head->next;
    ListNode * tail = reorderList(head->next, len-2);
    ListNode * tmp = tail->next;
    tail->next = tail->next->next;
    tmp->next = head->next;
    head->next = tmp;
    return tail;
}

void reorderList(ListNode *head) {  //recursive
    ListNode  * tail = NULL;
    tail = reorderList(head, getLength(head));
}

class Solution {
public:
    void reorderList(ListNode* head) {
        if (!head || !head->next) return;
        ListNode *cur = NULL;
        finished = false;
        old_head = head;
        reorderList(head, cur);
    }
private:
    void reorderList(ListNode *head, ListNode *&cur)
    {
        if (!head)
        {
            cur = old_head;
            return;
        }
        reorderList(head->next, cur);
        if (!finished)
        {
            if (cur && (cur == head || cur->next == head))
            {
                finished = true;
                head->next = NULL;
                return;
            }
            head->next = cur->next;
            cur->next = head;
            cur = cur->next->next;                
        }
    }
    
    bool finished;
    ListNode *old_head;
};
    // merge two lists: O(n)
    for (p1 = head, p2 = head2; p1; ) {
        auto t = p1->next;
        p1 = p1->next = p2;
        p2 = t;
    }