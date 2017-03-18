#  #1 priority queue  O(nlogw)
#  #2 deque  O(n)   dq.popleft(), nums[dq[0]] maintain the max number
#  #3 list []

#  import heapq
# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         if not nums: return []
#         h = []
#         res = []
#         for i in range(k):
#             heapq.heappush(h, [-nums[i], i])
        
#         for i in range(k, len(nums)):
#             t = h[0]
#             res.append(-t[0])
             
#             while  t[1] <= i-k:
#                 heapq.heappop(h)
#                 if not h: 
#                     break #Mistake 
#                 t = h[0]
#             heapq.heappush(h, [-nums[i],i])
         
#         res.append(-h[0][0])
#         return res
# class Solution:
#     # @param {integer[]} nums
#     # @param {integer} k
#     # @return {integer[]}
#     def maxSlidingWindow(self, nums, k):
#         if nums == []:
#             return []
#         ans,tmp = [], []
#         for i in range(0, k):
#             while tmp != [] and nums[i] > nums[tmp[-1]]:
#                 tmp.pop()
#             tmp.append(i)
#         for i in range(k, len(nums)):
#             ans.append(nums[tmp[0]])
#             while tmp != [] and nums[i] > nums[tmp[-1]]:
#                 tmp.pop()
#             tmp.append(i)
#             while tmp != [] and tmp[0] <= i-k:
#                 tmp.pop(0)
#         ans.append(nums[tmp[0]])
#         return ans

#          The dequeue maintain the elements in the current window and possible maximum value.

import collections
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        dq = collections.deque()
        result = [0 for x in range(n-k+1)]
        for i in range(k):
            while dq and nums[i]>nums[dq[-1]]:
                dq.pop()
            dq.append(i)
    
        for i in range(n-k):
            result[i] = nums[dq[0]] #The max value if at the front
            while dq and dq[0]<=i-k+1: #Pop out the elements that are not in window
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i+k]:
                dq.pop()
            dq.append(i+k)
        result[-1] = nums[dq[0]] #Last iteration
        return result
s = Solution() 
print s.maxSlidingWindow([7,6,5,4,3,2,1],4)
#     e scan the array from 0 to n-1, keep "promising" elements in the deque. The algorithm is amortized O(n) as each element is put and polled once.

# At each i, we keep "promising" elements, which are potentially max number in window [i-(k-1),i] or any subsequent window. This means

# If an element in the deque and it is out of i-(k-1), we discard them. We just need to poll from the head, as we are using a deque and elements are ordered as the sequence in the array

# Now only those elements within [i-(k-1),i] are in the deque. We then discard elements smaller than a[i] from the tail. This is because if a[x] <a[i] and x<i, then a[x] has no chance to be the "max" in [i-(k-1),i], or any other subsequent window: a[i] would always be a better candidate.

# As a result elements in the deque are ordered in both sequence in array and their value. At each step the head of the deque is the max element in [i-(k-1),i]

# public int[] maxSlidingWindow(int[] a, int k) {		
# 		if (a == null || k <= 0) {
# 			return new int[0];
# 		}
# 		int n = a.length;
# 		int[] r = new int[n-k+1];
# 		int ri = 0;
# 		// store index
# 		Deque<Integer> q = new ArrayDeque<>();
# 		for (int i = 0; i < a.length; i++) {
# 			// remove numbers out of range k
# 			while (!q.isEmpty() && q.peek() < i - k + 1) {
# 				q.poll();
# 			}
# 			// remove smaller numbers in k range as they are useless
# 			while (!q.isEmpty() && a[q.peekLast()] < a[i]) {
# 				q.pollLast();
# 			}
# 			// q contains index... r contains content
# 			q.offer(i);
# 			if (i >= k - 1) {
# 				r[ri++] = a[q.peek()];
# 			}
# 		}
# 		return r;
# 	}
 
# A long array A[] is given to you.There is a sliding window of size w which is moving from the very left of the array to the very right.You can only see the w numbers in the window. Each time the sliding window moves rightwards by one position. Following is an example:
# The array is [1 3 -1 -3 5 3 6 7], and w is 3.
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Input: A long array A[], and a window width w
# Output: An array B[], B[i] is the maximum value of from A[i] to A[i+w-1]
# Requirement: Find a good optimal way to get B[i]

# The obvious brute force solution with run time complexity of O(nw) is definitely not efficient enough.Every time the window is moved, you have to search for a total of w elements in the window.

# A heap data structure quickly comes to mind. We could boost the run time to approximately O(n lg w) (Note that I said approximately because the size of the heap changes constantly and averages about w). Insert operation takes O(lg w) time, where w is the size of the heap.However, getting the maximum value is cheap, it merely takes constant time as the maximum value is always kept in the root(head) of the heap.As the window slides to the right, some elements in the heap might not be valid anymore(range is outside of the current window). How should you remove them? You would need to be somewhat careful here.Since you only remove elements that are out of the window’s range, you would need to keep track of the elements’ indices too.
# Note that as n grows larger, the term lg w is pretty insignificant compared to n, and thus the overall complexity approximates to O(n). (Edit: In fact, the correct run time complexity should be O(n log n). If A is sorted, then the inner while loop will never run.This is due to the next element (which is larger) being pushed to the queue’s top as the new maximum. (Thanks to my readers anonymous and faircoin who pointed out this.)


# typedef pair<int, int> Pair;
# void maxSlidingWindow(int A [], int n, int w, int B []) {
#     priority_queue<Pair> Q;
#     for (int i = 0; i < w; i++)
#         Q.push(Pair(A[i], i));
#     for (int i = w; i < n; i++)
#     {
#         Pair p = Q.top();
#         B[i - w] = p.first;
#         while (p.second <= i - w)
#         {
#             Q.pop();
#             p = Q.top();
#         }
#         Q.push(Pair(A[i], i));
#     }
#     B[n - w] = Q.top().first;
# }

# You might be wondering: Is there a better way of doing this without using a heap? How about using a double-ended queue? (A linked list should be fine too)

# The double-ended queue is the perfect data structure for this problem.It supports insertion/deletion from the front and back. The trick is to find a way such that the largest element in the window would always appear in the front of the queue.How would you maintain this requirement as you push and pop elements in and out of the queue?

# Besides, you might notice that there are some redundant elements in the queue that we shouldn’t even consider about. For example, if the current queue has the elements: [10 5 3], and a new element in the window has the element 11. Now, we could have emptied the queue without considering elements 10, 5, and 3, and insert only element 11 into the queue.

# A natural way most people would think is to try to maintain the queue size the same as the window’s size.Try to break away from this thought and try to think outside of the box. Removing redundant elements and storing only elements that need to be considered in the queue is the key to achieve the efficient O(n) solution below.



# void maxSlidingWindow(int A[], int n, int w, int B[])
# {
#     deque<int> Q;
#     for (int i = 0; i < w; i++)
#     {
#         while (!Q.empty() && A[i] >= A[Q.back()])
#             Q.pop_back();
#         Q.push_back(i);
#     }
#     for (int i = w; i < n; i++)
#     {
#         B[i - w] = A[Q.front()];
#         while (!Q.empty() && A[i] >= A[Q.back()])
#             Q.pop_back();
#         while (!Q.empty() && Q.front() <= i - w)
#             Q.pop_front();
#         Q.push_back(i);
#     }
#     B[n - w] = A[Q.front()];
# }
 
 
# The above algorithm could be proven to have run time complexity of O(n). This is because each element in the list is being inserted and then removed at most once.Therefore, the total number of insert + delete operations is 2n.
 