class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def adjust(self):
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
                
    def push(self, element):
        self.stack1.append(element)

    def top(self):
        self.adjust()
        return self.stack2[len(self.stack2) - 1]

    def pop(self):
        self.adjust()
        return self.stack2.pop()

        单栈法：
在执行push操作时，使用辅助栈swap，将栈中元素顺序按照push顺序的逆序存储。

此时，push操作的时间复杂度为O(n)，其余操作的时间复杂度为O(1)

Python代码：
class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        swap = []
        while self.stack:
            swap.append(self.stack.pop())
        swap.append(x)
        while swap:
            self.stack.append(swap.pop())

    # @return nothing
    def pop(self):
        self.stack.pop()

    # @return an integer
    def peek(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0