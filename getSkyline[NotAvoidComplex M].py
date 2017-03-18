{URL: https://leetcode.com/problems/the-skyline-problem/}

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

#https://briangordon.github.io/2014/08/the-skyline-problem.html


# class EDGE:
#     def __init__(self, x, h, isLeft):
#         self.x = x
#         self.height = h
#         self.isLeft = isLeft
class Solution:
  
    def cmpfunc(self, e1, e2):
        if e1[0] != e2[0]:
            return e1[0] - e2[0]
        if (e1[2] == 's' and e2[2] == 's'):
            return e2[1] - e1[1]
        if (e1[2] == 'e' and e2[2] == 'e'):
            return e1[1] - e2[1]
        return -1 if e1[2] == 's' else 1
        
    def getSkyline2(self, LRH):# converted to edges , prefererd, when end edge occurs, remove the start edge from queue immediately
        skyline = []
        H = []

        size = len(LRH)

        edges = sorted([(LRH[x][0], LRH[x][2], 's') for x in range(size)] + 
                        [(LRH[x][1], LRH[x][2], 'e') for x in range(size)],
                        cmp=self.cmpfunc)
        print edges
        for edge in edges:
            if edge[2] == 's':
                if  not H or edge[1] > -H[0]: #NOT SORT CORRECTLY, 2 3 will both in the skyline, duplicated
                    skyline.append([edge[0], edge[1]])
                heappush(H, -edge[1])
            else:
                H.remove(-edge[1])
                if not H or -H[0] < edge[1]: # if don't sort correctly, then the lower hight will be in the skyline
                    skyline.append([edge[0], 0 if not H else -H[0]])
        return skyline
    def getSkyline(self, LRH):  #based on box- not easy to understand
        skyline = []
        i, n = 0, len(LRH)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:   #Prevernt from same x buildings, wait until hightest at x
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:  # pop others to get next lower hight not left behind yet
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline

        # In each loop, we first check what has the smaller x-coordinate: adding the next building from the input, or removing the next building from the queue. In case of a tie, adding buildings wins, as that guarantees correctness (think about it :-). We then either add all input buildings starting at that x-coordinate or we remove all queued buildings ending at that x-coordinate or earlier (remember we keep buildings in the queue as long as they're "under the roof" of a larger actually alive building). And then, if the current maximum height in the queue differs from the last in the skyline, we add it to the skyline.

        Use an infinite vertical line x to scan from left to right. If max height changes, record [x, height] in res. Online judge is using Python 2.7.9 and there's no max heap's push and pop method, so we can use a min heap hp storing -H as "max heap". Thanks to this discussion, set comprehension is faster and shorter than list(set((R, 0, None) for L, R, H in buildings)).

    def getSkyline(self, buildings): # SHORTER VERSION of active set 
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))  #sort first and second...
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: #if it's the last building or none-shaded one come
                heapq.heappop(hp)
            if negH: 
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]
s = Solution()
print(s.getSkyline([[2,9,10],[2,10,11], [3,8,16], [4,12,15],[5,12,13],[13,16,5]]))


# class MaxHeap:
#     def __init__(self, buildings):
#         self.buildings = buildings
#         self.size = 0
#         self.heap = [None] * (2 * len(buildings) + 1)
#         self.lineMap = dict()
#     def maxLine(self):
#         return self.heap[1]
#     def insert(self, lineId):
#         self.size += 1
#         self.heap[self.size] = lineId
#         self.lineMap[lineId] = self.size
#         self.siftUp(self.size)
#     def delete(self, lineId):
#         heapIdx = self.lineMap[lineId]
#         self.heap[heapIdx] = self.heap[self.size]
#         self.lineMap[self.heap[self.size]] = heapIdx
#         self.heap[self.size] = None
#         del self.lineMap[lineId]
#         self.size -= 1
#         self.siftDown(heapIdx)
#     def siftUp(self, idx):
#         while idx > 1 and self.cmp(idx / 2, idx) < 0:
#             self.swap(idx / 2, idx)
#             idx /= 2
#     def siftDown(self, idx):
#         while idx * 2 <= self.size:
#             nidx = idx * 2
#             if idx * 2 + 1 <= self.size and self.cmp(idx * 2 + 1, idx * 2) > 0:
#                 nidx = idx * 2 + 1
#             if self.cmp(nidx, idx) > 0:
#                 self.swap(nidx, idx)
#                 idx = nidx
#             else:
#                 break
#     def swap(self, a, b):
#         la, lb = self.heap[a], self.heap[b]
#         self.lineMap[la], self.lineMap[lb] = self.lineMap[lb], self.lineMap[la]
#         self.heap[a], self.heap[b] = lb, la
#     def cmp(self, a, b):
#         return self.buildings[self.heap[a]][2] - self.buildings[self.heap[b]][2]

# class Solution2:
#     def getSkyline(self, buildings):
#         size = len(buildings)
#         points = sorted([(buildings[x][0], x, 's') for x in range(size)] + 
#                         [(buildings[x][1], x, 'e') for x in range(size)])
#         maxHeap = MaxHeap(buildings)
#         ans = []
#         for p in points:
#             if p[2] == 's':
#                 maxHeap.insert(p[1])
#             else:
#                 maxHeap.delete(p[1])
#             maxLine = maxHeap.maxLine()
#             height = buildings[maxLine][2] if maxLine is not None else 0
#             if len(ans) == 0 or ans[-1][0] != p[0]:
#                 ans.append([p[0], height])
#             elif p[2] == 's':
#                 ans[-1][1] = max(ans[-1][1], height)
#             else:
#                 ans[-1][1] = min(ans[-1][1], height)
#             if len(ans) > 1 and ans[-1][1] == ans[-2][1]:
#                 ans.pop()
#         return ans

# dong.wang.1694 
# Reputation:  1,346
# The idea is to do line sweep and just process the buildings only at the start and end points. The key is to use a priority queue to save all the buildings that are still "alive". The queue is sorted by its height and end time (the larger height first and if equal height, the one with a bigger end time first). For each iteration, we first find the current process time, which is either the next new building start time or the end time of the top entry of the live queue. If the new building start time is larger than the top one end time, then process the one in the queue first (pop them until it is empty or find the first one that ends after the new building); otherswise, if the new building starts before the top one ends, then process the new building (just put them in the queue). After processing, output it to the resulting vector if the height changes. Complexity is the worst case O(NlogN)

# It sweeps from left to right. But it doesn't only keep heights of "alive buildings" in the priority queue and it doesn't remove them as soon as their building is left behind. Instead, (height, right) pairs are kept in the priority queue and they stay in there as long as there's a larger height in there, not just until their building is left behind.

# In each loop, we first check what has the smaller x-coordinate: adding the next building from the input, or removing the next building from the queue. In case of a tie, adding buildings wins, as that guarantees correctness (think about it :-). We then either add all input buildings starting at that x-coordinate or we remove all queued buildings ending at that x-coordinate or earlier (remember we keep buildings in the queue as long as they're "under the roof" of a larger actually alive building). And then, if the current maximum height in the queue differs from the last in the skyline, we add it to the skyline.
