# #Mistake
# don't make bad assumptions to make things so complicated  why the scenario that has random no next?


# An intuitive solution is to keep a hash table for each node in the list, via which we just need to iterate the list in 2 rounds respectively to create nodes and assign the values for their random pointers. As a result, the space complexity of this solution is O(N), although with a linear time complexity.

# As an optimised solution, we could reduce the space complexity into constant. The idea is to associate the original node with its copy node in a single linked list. In this way, we don't need extra space to keep track of the new nodes.

# The algorithm is composed of the follow three steps which are also 3 iteration rounds.

# Iterate the original list and duplicate each node. The duplicate
# of each node follows its original immediately.
# Iterate the new list and assign the random pointer for each
# duplicated node.
# Restore the original list and extract the duplicated nodes.
# The algorithm is implemented as follows:
# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
def __repr__(self):
	return """RandomListNode(label=%r, next=%r, random=%r""" % (self.label, self.next,self.random)

# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
            """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
         
        pairmaps = {}
        
        
        def dfs(head):   
            if not head:
                return None
            cur = None
            if head not in pairmaps:
                cur = RandomListNode(head.label)
                pairmaps[head] = cur
                if head.next:
                    cur.next = dfs(head.next)
                if head.random:
                    cur.random = dfs(head.random)#Mistake not Random, dfs param numbers
            else:
                cur = pairmaps[head] 
            return cur
            
        return dfs(head)
	def copyRandomList_my(self, head):
		pairmaps = {}
		def dfs(head):
			if not head:
				return None
			if head in pairmaps:
				return pairmaps[head]
			else:
				pairmaps[head] = RandomListNode(head.label)
				pairmaps[head].next = self.copyRandomList(head.next) . #Mistake should be dfs
				pairmaps[head].random   = self.copyRandomList(head.random)
				return pairmaps[head]
				
		return dfs(head)

	# def copyRandomListBF(self, head):    
	# 	if not head: return None
		
	# 	pairmaps = {}
	# 	newhead = None
	# 	cur = head
	# 	while cur:
	# 		pairmaps[cur] = RandomListNode(cur.label)
	# 		cur = cur.next
	# 	cur = head
	# 	newhead = pairmaps[head]
	# 	p = newhead
	# 	while cur:
	# 		if cur.next:
	# 			p.next = pairmaps[cur.next]
	# 		if cur.random:
	# 			p.random = pairmaps[cur.random]
	# 		p = p.next
	# 		cur = cur.next
	# 	return newhead

s = Solution() 
root= RandomListNode(1)

root.next = RandomListNode(2)
root.random = root.next
res = s.copyRandomList(root)
 
print(res)



# public RandomListNode copyRandomList(RandomListNode head) {
# 	RandomListNode iter = head, next;

# 	// First round: make copy of each node,
# 	// and link them together side-by-side in a single list.
# 	while (iter != null) {
# 		next = iter.next;

# 		RandomListNode copy = new RandomListNode(iter.label);
# 		iter.next = copy;
# 		copy.next = next;

# 		iter = next;
# 	}

# 	// Second round: assign random pointers for the copy nodes.
# 	iter = head;
# 	while (iter != null) {
# 		if (iter.random != null) {
# 			iter.next.random = iter.random.next;
# 		}
# 		iter = iter.next.next;
# 	}

# 	// Third round: restore the original list, and extract the copy list.
# 	iter = head;
# 	RandomListNode pseudoHead = new RandomListNode(0);
# 	RandomListNode copy, copyIter = pseudoHead;

# 	while (iter != null) {
# 		next = iter.next.next;

# 		// extract the copy
# 		copy = iter.next;
# 		copyIter.next = copy;
# 		copyIter = copy;

# 		// restore the original list
# 		iter.next = next;

# 		iter = next;
# 	}

# 	return pseudoHead.next;
    
# # Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None


# class Solution(object):
#     def __init__(self):
#         self.dummy = RandomListNode(0)
#     def copyRandomList-badassumption(self, head):
#         """
#         :type head: RandomListNode
#         :rtype: RandomListNode
#         """
         
#         pairmaps = {}
        
#         cur = self.dummy
#         def dfs(head):
#             if not head:
#                 return
        
#             cur.next = pairmaps[head] if head in pairmaps else RandomListNode(head.label)
#             if not self.newhead:
#                 self.newhead = cur
#             if head.next:
#                 dfs(head.next) #Mistake cur not sync up, not change to next too
#             if head.random:
#                 dfs(head.random)
#         dfs(head)
#         return self.newhead
