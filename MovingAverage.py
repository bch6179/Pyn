class MovingAverage



    def __init__(self, size):
        self.vect, self.sums, self.idx, self.size = [0] * size, 0, 0, size
        

    def next(self, val):
        self.idx += 1
        self.sums -= self.vect[self.idx % self.size]
        self.vect[self.idx % self.size] = val
        self.sums += val
        return self.sums / float(min(self.idx, self.size))
My solution requires real O(1) time for next() operation as it is not needed to compute the sum every time. We just subtract the element that is exiting from the sliding window, and we're done. We need also to substitute that element with the new one.

 Circular Array - real O(1) time next()

 def __init__(self, size):
        """
    Initialize your data structure here.
    :type size: int
    """
    self.maxsize = size
    self.sum = 0
    self.window = collections.deque()

def next(self, val):
    """
    :type val: int
    :rtype: float
    """
    self.window.append(val)
    if len(self.window) < self.maxsize:
        self.sum += val
    else:
        self.sum += val - self.window.popleft()
        
    return self.sum/self.maxsize