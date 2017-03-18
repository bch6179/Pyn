class Solution(object):
    def paintHouse(self, costs):
        if costs == None or len(costs) == 0: return -1
        n = len(costs)

        for i in range(1,n):
            costs[i][0] = costs[i][0] + min(costs[i-1][1], costs[i-1][2])
            costs[i][1] = costs[i][1] + min(costs[i-1][0], costs[i-1][2])
            costs[i][2] = costs[i][2] + min(costs[i-1][0], costs[i-1][1])
        return min(costs[n-1][0],costs[n-1][1],costs[n-1][2] )
    def paintHouseK(self, costs):
        if costs == None or len(costs) == 0: return -1
        n = len(costs)
        prevMin, prevSec = 0, 0
        prevId = -1
        for i in range(0,n):
            curMin, curSec = 1 << 31 -1, 1<<31-1
            curIdx = -1
            for j in range(0, k):
                costs[i][j] = costs[i][j] + prevMin if prevIdx != j else prevSec

                
                if  costs[i][j]< curMin:
                    curSec = curMin
                    curMin = costs[i][j]
                    curIdx = j
                elif  costs[i][j]< curSec:
                    curSec = costs[i][j]
                prevMin = curMin
                prevSec = curSec
                prevIdx = curIdx
        return prevMin                      

s = Solution() 
print s.paintHouse([[1,2,3],[1,2,3],[1,2,3]])