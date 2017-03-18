from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        :rtype: nothing
        
        """
        return self.queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue) == 0
        
# nalysis:
# This is a classic question related to queue and stack. Let's review the stack and queue data structure, it is very easy to remember the properties of those two data structures that:

# Queue:  FIFO (First In First Out)
# Stack: LIFO (Last In First Out)

# This question asks to use queue to simulate stack. There are several ways to do so, here I just provide one of the solutions that utilizing two queues. The basic idea is to swap the two queues every time when popping the element from stack. Queue 1 stores the stack top element, Queue 2 stores the previous elements. Every time when pushing one element into stack, push queue 1's top in queue 2, and push the new element in queue 1. Every time when popping the top element in stack, push the queue 1's top (only one element in this queue). Then push n-1 elements from queue 2 to queue 1, where n is the total number of elements in queue 2. In other words, we left one element in queue 2 (this is the top element in the current stack), and push all the other elements into the empty queue (queue 1). Finally we swap queue 1 and queue 2. The stack is empty iff queue 1 and queue 2 are all empty. The top element is always the only element in queue 1.

# class Stack(object):
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.q1 = []
#         self.q2 = []
         
 
#     def push(self, x):
#         """
#         :type x: int
#         :rtype: nothing
#         """
#         self.q1.append(x)
#         if len(self.q1) == 1:
#             return
#         else:
#             self.q2.append(self.q1.pop(0))
         
 
#     def pop(self):
#         """
#         :rtype: nothing
#         """
#         self.q1.pop(0)
#         for i in range(len(self.q2)-1):
#             self.q1.append(self.q2.pop(0))
#         self.q1, self.q2 =  self.q2, self.q1
         
 
#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.q1[0]
 
#     def empty(self):
#         """
#         :rtype: bool
#         """
#         if len(self.q1)==0 and len(self.q2)==0:
#             return True
#         else:
#             return False


# class Stack:
#     # initialize your data structure here.
#     def __init__(self):
#         self.queue = []

#     # @param x, an integer
#     # @return nothing
#     def push(self, x):
#         self.queue.append(x)

#     # @return nothing
#     def pop(self):
#         for x in range(len(self.queue) - 1):
#             self.queue.append(self.queue.pop(0))
#         self.queue.pop(0)

#     # @return an integer
#     def top(self):
#         top = None
#         for x in range(len(self.queue)):
#             top = self.queue.pop(0)
#             self.queue.append(top)
#         return top


#     # @return an boolean
#     def empty(self):
#         return self.queue == []
# from collections import deque
# >>> l = deque([0, 1, 2, 3, 4])
# >>> l.popleft()
# 0		

# class Stack {
# public:
# 	queue<int> que;
# 	// Push element x onto stack.
# 	void push(int x) {
# 		que.push(x);
# 		for(int i=0;i<que.size()-1;++i){
# 			que.push(que.front());
# 			que.pop();
# 		}
# 	}

# 	// Removes the element on top of the stack.
# 	void pop() {
# 		que.pop();
# 	}

# 	// Get the top element.
# 	int top() {
# 		return que.front();
# 	}

# 	// Return whether the stack is empty.
# 	bool empty() {
# 		return que.empty();
# 	}
# };