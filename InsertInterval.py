    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    # Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        h = 0
        for i, I in enumerate(intervals):           
            if I.end >= newInterval.start:
                if I.start <= newInterval.end:
                    newInterval.start = min(I.start, newInterval.start)
                    newInterval.end = max(I.end, newInterval.end)
                    h += 1 #Mistake return the wrong h, [1,5] [2,3]
                else:
                   
                    break
            else:
                res.append(I)
                h+=1
        res.append(newInterval)   # Has to be here, if [] then only here get chance to insert new
        res.extend(intervals[h:])
        return res
        #Mistake [] [5,7] become Null
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        result = []
        i = 0
        while i < len(intervals):
            if start <= intervals[i].end:
                if end < intervals[i].start:
                    break
                start = min(start, intervals[i].start)
                end = max(end, intervals[i].end)
            else:
                result.append(intervals[i])
            i += 1
        result.append(Interval(start, end))
        result += intervals[i:]
        return result

public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
    List<Interval> result = new LinkedList<>();
    int i = 0;
    // add all the intervals ending before newInterval starts
    while (i < intervals.size() && intervals.get(i).end < newInterval.start)
        result.add(intervals.get(i++));
    // merge all overlapping intervals to one considering newInterval
    while (i < intervals.size() && intervals.get(i).start <= newInterval.end) {
        newInterval = new Interval( // we could mutate newInterval here also
                Math.min(newInterval.start, intervals.get(i).start),
                Math.max(newInterval.end, intervals.get(i).end));
        i++;
    }
    result.add(newInterval); // add the union of intervals we got
    // add all the rest
    while (i < intervals.size()) result.add(intervals.get(i++)); 
    return result;
}