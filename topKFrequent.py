Uses a dict to maintain counts, heapifys the list of counts, then selects K elements out of the max heap.

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        counter = collections.Counter(nums)
        # return [a for a, b in counter.most_common(k)]
        for n,c in counter.items():
            heapq.heappush(heap, (c,n))
        for _ in range(len(heap)-k):
            heapq.heappop(heap)
        return [n for c,n in heap]
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        freq_list=[]  
        for num in nums:
            if num in freq:
                freq[num] = freq[num] + 1
            else:
                freq[num] = 1
                
        for key in freq.keys():
           
            freq_list.append((-freq[key], key))
        heapq.heapify(freq_list)
        topk = []
        for i in range(0,k):
            topk.append(heapq.heappop(freq_list)[1])
        return topk

I used a dictionary to get the frequencies, and then used quick select to get the top k frequenct elements.

def topKFrequent(nums, k):
    
    def quick_select(left, right):
        pivot = left
        l, r = left, right
        while l < r:
            while l < r and counts[r][1] <= counts[pivot][1]:
                r -= 1
            while l < r and counts[l][1] >= counts[pivot][1]:
                l += 1
            counts[l], counts[r] = counts[r], counts[l]
        counts[left], counts[l] = counts[l], counts[left]
        
        if l + 1 == k:
            return counts[:l+1]
        elif l + 1 < k:
            return quick_select(l + 1, right)
        else:
            return quick_select(left, l - 1)
    
    if not nums:
        return []
        
    # Get the counts.
    counts = {}
    for x in nums:
        counts[x] = counts.setdefault(x, 0) + 1
        
    counts = counts.items()
    # Use quick select to get the top k counts.
    return [c[0] for c in quick_select(0, len(counts) - 1)]