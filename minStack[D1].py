class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            minv = x
        else: 
            _, minv = self.stack[-1]
        self.stack.append((x,min(x,minv)))
        

    def pop(self):
        """
        :rtype: void
        """
        v,_ = self.stack.pop()
        return v

    def top(self):
        """
        :rtype: int
        """
        v, _ = self.stack[-1]
        return v
        
    def getMin(self):
        """
        :rtype: int
        """
        _, minv = self.stack[-1]
        return minv


s = MinStack() 
s.push(-2)
s.push(0)
s.push(-3)
print s
print s.getMin()
s.pop()
print s.getMin()


# class MinStack(object):

#     def __init__(self):
#         self.stack = []
        
#     def push(self, x):
#         self.stack.append((x, min(self.getMin(), x))) 
           
#     def pop(self):
#         self.stack.pop()

#     def top(self):
#         if self.stack:
#             return self.stack[-1][0]
        
#     def getMin(self):
#         if self.stack:
#             return self.stack[-1][1]
#         return sys.maxint    