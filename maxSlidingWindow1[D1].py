#practise, look at explanation at another
#mistake    [1,-1] 1  if not h: break

from heapq import *

from collections import deque


class Solution(object):

 # a = [5,3,6, 7,6,5,4,3]
#   #  6:4 6:2 5:0 3:1 
 

    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        h = []
        res = []
        for i in range(k):
            heapq.heappush(h, [-nums[i], i])
        
        for i in range(k, len(nums)):
            t = h[0]
            res.append(-t[0])
             
            while  t[1] <= i-k:
                heapq.heappop(h)
                if not h: break
                t = h[0]
            heapq.heappush(h, [-nums[i],i])
         
        res.append(-h[0][0])
        return res
        # a = [5,3,6, 7,6,5,4,3]  0 2
        #     6:4 6:2 5:0 3:1 
    def maxSlidingWindow(self, a, k):  
        window = deque()
        res = []
        for i in range(k):
            while window and a[window[-1]] < a[i]:
                window.pop()
            window.append(i)
            
        for i in range(k, len(a)): 
            res.append( a[window[0]])  # before filling new, left head is the max
            while window and window[0] < i-k+1:   #remove outdated ones
                window.popleft()
            while window and a[window[-1]] < a[i]: #when a bigger new coming, out stack   the top ones which are smaller than the most left ones
                window.pop()       
            window.append(i)
        if window:
            res.append(a[window[0]])
        return res
s = Solution() 
print s.maxSlidingWindow([5,3,6, 7,6,5,4,3] ,3)
                                 

# def sliding_window_minimum(k, li):
#     '''
#     A iterator which takes the size of the window, `k`, and an iterable,
#     `li`. Then returns an iterator such that the ith element yielded is equal
#     to min(list(li)[max(i - k + 1, 0):i+1]).
#     Each yield takes amortized O(1) time, and overall the generator takes O(k)
#     space.
#     '''

#     window = deque()
#     for i, x in enumerate(li):
#         while window and window[-1][0] >= x:
#             window.pop()
#         window.append((x, i))
#         while window[0][1] <= i - k:
#             window.popleft()
#         yield window[0][0]























