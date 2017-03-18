#[Note]
#=====
#  *             *
#     *               *
#       -------------------
#                        * (increase count to 4)
#sort per start, actually just push new if start > min heap end value
#count only increased because of overlapping 

import heapq

class Solution:
    def minMeetingRooms(self, intervals):
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        
        starts.sort()
        ends.sort()
        s = e = 0
        numRooms = available = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                    
                s += 1
            else:
                available += 1
                e += 1
        
        return numRooms
# ice and indeed fast, like @insulator2016_rush said. Sorting the starts and ends separately helps noticeably. 
# #Here's a little variation with shorter preparation and using a for-loop for starts.
    def minMeetingRooms2(self, intervals):
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        e = 0
        numRooms = available = 0
        for start in starts:
            while ends[e] <= start:
                available += 1
                e += 1
            if available:
                available -= 1
            else:
                numRooms += 1

        return numRooms

    def minMeetingRooms3(self, intervals):  
        """ 
        :type intervals: List[Interval] 
        :rtype: int 
        """  
        heap, num = [], 0  
        heapq.heapify(heap)  
        #intervals.sort(lambda a, b : a.start - b.start)  
        intervals = sorted(intervals, key = lambda a:a.start)
        for i in range(len(intervals)):  
            if len(heap) == 0:  
                heapq.heappush(heap, intervals[i].end)  
                num += 1  
                continue  
            if heap[0] <= intervals[i].start:  
                heapq.heappop(heap)   
                heapq.heappush(heap, intervals[i].end)  
                num +=1  
                  
            else:  
                heapq.heappush(heap, intervals[i].end)  
        return num  
    def minMeetingRooms4(self, intervals): 
        heap = []
        heapq.heapify(heap)
        mc = 0
        for i in range(len(intervals)):
            if len(heap) == 0:
                heapq.heappush(heap,[intervals[i].start,intervals[i]] )
                mc = max(mc, len(heap))
                continue
            while len(heap) > 0 and  heap[0][1].end < intervals[i].start:
                heapq.heappop(heap)
            if (i >= len(intervals)): break
            heapq.heappush(heap, [intervals[i].start,intervals[i]] )
            mc = max(mc, len(heap))
        return mc
    def minMeetingRoomsPractice(self, intervals): 
        heap = []
        heapq.heapify(heap)
        mc,num =0, 0
        for i in range(len(intervals)):
            if len(heap) == 0:
                heapq.heappush(heap,intervals[i].end )
                num+=1 
                continue
            if heap[0] < intervals[i].start:
                heapq.heappop(heap)
            else: num+=1 
            heapq.heappush(heap,intervals[i].end )
        return num
class  Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

print 5
print 5/3
s = Solution()
intervals = [Interval(1,3),Interval(2,4),Interval(5,10), Interval(6, 12),Interval(7,13)]
print(intervals)
print(s.minMeetingRooms2(intervals))











 # Very similar with what we do in real life. Whenever you want to start a meeting, 
 # you go and check if any empty room available (available > 0) and
 # if so take one of them ( available -=1 ). Otherwise,
 # you need to find a new room someplace else ( numRooms += 1 ).  
 # After you finish the meeting, the room becomes available again ( available += 1 ).
 
 def minMeetingRooms(self, intervals):
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        
        starts.sort()
        ends.sort()
        s = e = 0
        numRooms = available = 0
        while s < len(starts):
            if starts[s] < ends[e]:
                if available == 0:
                    numRooms += 1
                else:
                    available -= 1
                    
                s += 1
            else:
                available += 1
                e += 1
        
        return numRooms


0 10    need 3  ava 0
0 20    
10 20
11 25

0 2
10 0
11 1
20 -2
25 -1







0-5
   7-9
      10--28
        11-21
    8--     23
           









  