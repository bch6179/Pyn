import heapq 
class Solution(object):
    def thirdMaxBad(self, nums):
        l = []
        for num in set(nums):
            
            heapq.heappush(l, -num) # heap only ensure top 3 but the last one is not necessarily the 3rd one
            if len(l) > 3:
                l.pop()       
        return -l[-1] if len(l) == 3 else -l[0]
    def thirdMax2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if not nums: return None
        # myset = set()
        
        # for n in nums:
        #     myset.add(n)
        # res = [-sys.maxint-1]*3
        # # myheap = collections.deque(maxlen=3)
        
        # # for n in myset:
        # #     if len(myheap) == 3:
        # #         myheap.popleft()
        # #     heapq.heappush(myheap, n)    
        # for n in myset:
        #     if n > res[2]:
        #         res[2] = n
        #     elif n > res[1]:
        l = []
        for num in set(nums):
            
            l = sorted(l+[-num])[:3]
            if len(l) > 3:
                l.pop()
            
        
        return -l[-1] if len(l) == 3 else -l[0]
s= Solution()
print s.thirdMax([3,2,1])