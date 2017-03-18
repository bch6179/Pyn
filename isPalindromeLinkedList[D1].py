
[0216] CheckOneMore: dfs if return false, return; else if != return false, otherwise return true but remember to cur->next

slow->next=reverseList(slow->next);
slow=slow->next;
After running these two lines, slow will always point to the first node of the second half of the linked list.

For linked list 1->2->3->2-1, the code below first makes the list to be 1->2->3->2<-1 and the second 2->None, then make 3->None, for even number linked list: 1->2->2->1, make first 1->2->2<-1 and then the second 2->None, and lastly do not forget to make the first 2->None (If forget it still works while the idea behind is a little bit different).

def isPalindrome(self, head):
    if not head:
        return True
    # split the list to two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    slow.next = None # Don't forget here! But forget still works!
    # reverse the second part
    node = None
    while second:
        nxt = second.next
        second.next = node
        node = second
        second = nxt
    # compare two parts
    # second part has the same or one less node
    while node:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True


class Solution {

public:
    bool isPalindrome(ListNode* head) {
        ListNode *cur = head;//this is the normal cursor
        return judge(head, cur);
    }
    bool judge(ListNode *head, ListNode* &cur) {
        if (!head) return true;
        if (!judge(head->next, cur)) return false;
        if (cur->val != head->val) return false;
        else {cur = cur->next; return true;}
    }
    
def isPalindrome(self, head):
    if not head:
        return True

    def reverse(head):
        tmp = ans = None
        while node:
            tmp, node.next = node.next, ans
            ans, node = node, tmp
        return ans

    middle = fast = head
    while fast.next and fast.next.next:
        middle, fast = middle.next, fast.next.next

    rev = reverse(middle.next)
    fast = rev
    while fast and head.val == fast.val:
        fast, head = fast.next, head.next

    reverse(rev)
    return fast is None

    O(n) extra space solution by using deque:

# O(n) space
def isPalindrome(self, head):
    queue = collections.deque([])
    cur = head
    while cur:
        queue.append(cur)
        cur = cur.next
    while len(queue) >= 2:
        if queue.popleft().val != queue.pop().val:
            return False
    return True
about a year ago reply quote 
0
  JayWong   @caikehe
Reputation:  59
Say we know the mid point, using a stack requires O (N/2) extra space lol

7 months ago reply quote 
1
  JayWong 
Reputation:  59
Here is the stack algorithm with O(N) time complexity and O(N/2) space complexity:

The algorithm has two steps:

Find the midpoint of the linked list
Push the second half values into the stack
Pop values out from the stack, and compare them to the first half of the linked list
The advantages of this algorithm are we don't need to restore the linked list and the space complexity is acceptable (O(N/2))

def isPalindrome(self, head):

    if not head or not head.next:
        return True

    # 1. Get the midpoint (slow)
    slow = fast = cur = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    
    # 2. Push the second half into the stack
    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    # 3. Comparison
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next
    
    return True