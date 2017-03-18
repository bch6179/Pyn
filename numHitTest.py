import collections

class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = collections.defaultdict(int)
        self.timeHits = collections.defaultdict(int)
        self.countInWindow = 0
        self.lasthit = 0
        self.data[self.lasthit] = 0
        self.timeHits[0] = 0 
    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not timestamp or timestamp <= 0: return

        self.timeHits[timestamp] += 1
        last = timestamp - 300  if timestamp > 300 else 0
        self.data[timestamp] =  self.timeHits[timestamp] - self.timeHits[last]
        self.data[timestamp] += self.data[self.lasthit]
        self.lasthit = timestamp
    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        last = timestamp - 300  if timestamp > 300 else 0
        return self.data[timestamp]  - self.timeHits[last]
         


# Your HitCounter object will be instantiated and called as such:
obj = HitCounter()
obj.hit(1)
obj.hit(2)
obj.hit(3)
print  obj.getHits(4)
obj.hit(300)
 
print  obj.getHits(300)

print  obj.getHits(301)
print  obj.getHits(302)