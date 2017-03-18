#[Note]
#=====
#Instead of doing in a hard way, cur, next, which leave uncertainty ahead, we leave it behind by prev, cur

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key=lambda x:x.start)
        result = []
        for interval in intervals:
            if len(result) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
        return result
           
#Mistake solution
    #sort
        # toInsert = 0
        # i = 0
        # res = []
        # for i in range(len(intervals) - 1):
        #     cur = intervals[i]
        #     next = intervals[i+1]
        #     if cur.end < next.start:
        #         res.append(Interval(min(cur.start, next.start),
        #             max(cur.end, next.end)))
        #     else:
        #         res.append(cur)