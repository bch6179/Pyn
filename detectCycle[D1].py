# main idea is the same with problem Linked List Cycle II,https://leetcode.com/problems/linked-list-cycle-ii/. Use two pointers the fast and the slow. The fast one goes forward two steps each time, while the slow one goes only step each time. They must meet the same item when slow==fast. In fact, they meet in a circle, the duplicate number must be the entry point of the circle when visiting the array from nums[0]. Next we just need to find the entry point. We use a point(we can use the fast one before) to visit form begining with one step each time, do the same job to slow. When fast==slow, they meet at the entry point of the circle. The easy understood code is as follows.

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return -1
        try:
            slow = nums[0]
            fast = nums[slow]
            
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]] #Mistake not slow, otherwise inifi
            
            fast = 0      #back one step since we have init fast =slow.next
            while slow != fast:
                fast = nums[fast]
                slow = nums[slow]
            return slow
        except:           #no duplicate; if duplicate , then we won't have index number is n
            return -1

 this problem, nums[a] = b can be seen as a.next = b, the the problem is exactly the same as Linked List Cycle II which finds the node that cycle begins.

def findDuplicate(self, nums):
    slow = fast = finder = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            while finder != slow:
                finder = nums[finder]
                slow = nums[slow]
            return finder
        
              H: distance from head to cycle entry E
        D: distance from E to X
        L: cycle length
                          _____
                         /     \
        head_____H______E       \
                        \       /
                         X_____/   
        
    
        If fast and slow both start at head, when fast catches slow, slow has traveled H+D and fast 2(H+D). 
        Assume fast has traveled n loops in the cycle, we have:
        2H + 2D = H + D + L  -->  H + D = nL  --> H = nL - D
        Thus if two pointers start from head and X, respectively, one first reaches E, the other also reaches E. 
        In my solution, since fast starts at head.next, we need to move slow one step forward in the beginning of part 2

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        try:
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            # if there is an exception, we reach the end and there is no cycle
            return None

        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next

        return head