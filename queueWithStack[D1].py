
have one input stack, onto which I push the incoming elements, and one output stack, from which I peek/pop. I move elements from input stack to output stack when needed, i.e., when I need to peek/pop but the output stack is empty. When that happens, I move all elements from input to output stack, thereby reversing the order so it's the correct order for peek/pop.
class MyQueue {

    Stack<Integer> input = new Stack();
    Stack<Integer> output = new Stack();
    
    public void push(int x) {
        input.push(x);
    }

    public void pop() {
        peek();
        output.pop();
    }

    public int peek() {
        if (output.empty())
            while (!input.empty())
                output.push(input.pop());
        return output.peek();
    }

    public boolean empty() {
        return input.empty() && output.empty();
    }
}
The loop in peek does the moving from input to output stack. Each element only ever gets moved like that once, though, and only after we already spent time pushing it, so the overall amortized cost for each operation is O(1).
The idea is to simulate a queue using two stacks (same as previous posts). I use python list as the underlying data structure for stack and add a "move()" method to simplify code: it moves all elements of the "inStack" to the "outStack" when the "outStack" is empty. Here is the code

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.inStack) and (not self.outStack) 
        
    def move(self):
        """
        :rtype nothing
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())