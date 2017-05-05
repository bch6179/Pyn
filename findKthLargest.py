from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for num in nums:
            heappush(heap, num)
        t = len(nums) - k
        while t > 0:
            heappop(heap)
            t-=1
        return heap[0]
#O(k+(n-k)lgk)
# Python different solutions with comments (bubble sort, selection sort, heap sort and quick sort).
# # O(nlgn) time
# def findKthLargest1(self, nums, k):
#     return sorted(nums, reverse=True)[k-1]
    
# # O(nk) time, bubble sort idea, TLE
# def findKthLargest2(self, nums, k):
#     for i in xrange(k):
#         for j in xrange(len(nums)-i-1):
#             if nums[j] > nums[j+1]:
#                 # exchange elements, time consuming
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums[len(nums)-k]
    
# # O(nk) time, selection sort idea
# def findKthLargest3(self, nums, k):
#     for i in xrange(len(nums), len(nums)-k, -1):
#         tmp = 0
#         for j in xrange(i):
#             if nums[j] > nums[tmp]:
#                 tmp = j
#         nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
#     return nums[len(nums)-k]
    



# # O(k+(n-k)lgk) time, min-heap        
# def findKthLargest5(self, nums, k):
#     return heapq.nlargest(k, nums)[k-1]
    
# # O(n) time, quick selection
# def findKthLargest(self, nums, k):
#     # convert the kth largest to smallest
#     return self.findKthSmallest(nums, len(nums)+1-k)
    
# def findKthSmallest(self, nums, k):
#     if nums:
#         pos = self.partition(nums, 0, len(nums)-1)
#         if k > pos+1:
#             return self.findKthSmallest(nums[pos+1:], k-pos-1)
#         elif k < pos+1:
#             return self.findKthSmallest(nums[:pos], k)
#         else:
#             return nums[pos]
 
# # choose the right-most element as pivot   
# def partition(self, nums, l, r):
#     low = l
#     while l < r:
#         if nums[l] < nums[r]:
#             nums[l], nums[low] = nums[low], nums[l]
#             low += 1
#         l += 1
#     nums[low],      nums[r] = nums[r], nums[low]
#     return low

# def findKthLargest(self, nums, k):
#     # QuickSelect idea: AC in 52 ms
#     # ---------------------------
#     #
#     pivot = nums[0]
#     left  = [l for l in nums if l < pivot]
#     equal = [e for e in nums if e == pivot]
#     right = [r for r in nums if r > pivot]

#     if k <= len(right):
#         return self.findKthLargest(right, k)
#     elif (k - len(right)) <= len(equal):
#         return equal[0]
#     else:
#         return self.findKthLargest(left, k - len(right) - len(equal))
# pivot = nums[len(nums)//2]