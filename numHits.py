# 362. Design Hit Counter Add to List
# DescriptionSubmissionsSolutions
# Total Accepted: 13278
# Total Submissions: 25032
# Difficulty: Medium
# Contributors: Admin
# Design a hit counter which counts the number of hits received in the past 5 minutes.

# Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

# It is possible that several hits arrive roughly at the same time.

# Example:
# HitCounter counter = new HitCounter();

# // hit at timestamp 1.
# counter.hit(1);

# // hit at timestamp 2.
# counter.hit(2);

# // hit at timestamp 3.
# counter.hit(3);

# // get hits at timestamp 4, should return 3.
# counter.getHits(4);

# // hit at timestamp 300.
# counter.hit(300);

# // get hits at timestamp 300, should return 4.
# counter.getHits(300);

# // get hits at timestamp 301, should return 3.
# counter.getHits(301); 
# Follow up:
# What if the number of hits per second could be very large? Does your design scale?

#1) Maintain the valid of a deque (timestamp, count) and countGlobalForWindow, seperate data , improved read , scale in both time and space
# 2) bucket , read and write both cost
# 3) map timestamp to count, and sum with a window loop 
class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(int)

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.dic[timestamp] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        start = timestamp-300+1 if timestamp > 300 else 0
        summation = 0
        for i in range(start, timestamp+1):
            summation += self.dic[i]
        return summation
def __init__(self):
    """
    Initialize your data structure here.
    """
    from collections import deque
    
    self.num_of_hits = 0
    self.time_hits = deque()
    

def hit(self, timestamp):
    """
    Record a hit.
    @param timestamp - The current timestamp (in seconds granularity).
    :type timestamp: int
    :rtype: void
    """
    #  while(!q.isEmpty() && timestamp - q.peek().sec > 299){ //at most 299 cycles, therefore O(1)
    #         hits -= q.peek().count;
    #         q.poll();
    #     }
    if not self.time_hits or self.time_hits[-1][0] != timestamp:
        self.time_hits.append([timestamp, 1])
    else:
        self.time_hits[-1][1] += 1
    
    self.num_of_hits += 1
            
#     Each time we get a new window, we delete old Seconds and subtract counts from total hits.
# this solution also scales on space because we at most have 300 items on the queue. we combine identical hits.

def getHits(self, timestamp):
    """
    Return the number of hits in the past 5 minutes.
    @param timestamp - The current timestamp (in seconds granularity).
    :type timestamp: int
    :rtype: int
    """
    while self.time_hits and self.time_hits[0][0] <= timestamp - 300:
        self.num_of_hits -= self.time_hits.popleft()[1]
    
    return self.num_of_hits


O(s) s is total seconds in given time interval, in this case 300.
basic ideal is using buckets. 1 bucket for every second because we only need to keep the recent hits info for 300 seconds. hit[] array is wrapped around by mod operation. Each hit bucket is associated with times[] bucket which record current time. If it is not current time, it means it is 300s or 600s... ago and need to reset to 1.

public class HitCounter {
    private int[] times;
    private int[] hits;
    /** Initialize your data structure here. */
    public HitCounter() {
        times = new int[300];
        hits = new int[300];
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        int index = timestamp % 300;
        if (times[index] != timestamp) {
            times[index] = timestamp;
            hits[index] = 1;
        } else {
            hits[index]++;
        }
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        int total = 0;
        for (int i = 0; i < 300; i++) {
            if (timestamp - times[i] < 300) {
                total += hits[i];
            }
        }
        return total;
    }
}

use an arraylist to store the time stamps, because I'm thinking all elements should be saved. And use a start pointer to point to the start index of last 300 timestamps.

public class HitCounter {
    ArrayList<Integer> list ;
    int start;

    /** Initialize your data structure here. */
    public HitCounter() {
        list = new ArrayList<Integer>();
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        list.add(timestamp);
        while(start< list.size() && list.get(start)<=timestamp-300){
            start++;
        }
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        while(start<list.size() && list.get(start)<=timestamp-300){
            start++;
        } 
        
        return list.size()-start;
    }
}
f huge amount of hits happened at the same timestamp, this solution will takes too much memory since each element in queue is a single hit. It's better to map timestamp to the number of hits at this timestamp.

6 months ago reply quote 
1
B blackbird   @touchdown
Reputation:  3
@touchdown what about we store timestamp and hit number pair instead of each element for one 
e size of hits getting larger and larger, this solution is inefficient;

list size will double once size hits a limit. A scalable problem will become more and more obvious.
worst case is that for everyHits happened after 5 mins, it will have to traverse the list from beginning to end; if LEN is n for every 5 mins, then the operation is linear. For read-heavy request, this is unacceptable.


ow it will scale if question asked for hit required in past 1000(or any higher value) minutes ?

Below is my solution Insertion O(1) and query time log(N). Idea is similar to binary search.

Code Link

public class HitCounter {
    List<Integer> data;
    /** Initialize your data structure here. */
    public HitCounter() {
        data = new ArrayList();
        data.add(Integer.MIN_VALUE);
        data.add(Integer.MAX_VALUE);
    }
    
    /** Record a hit.
        @param timestamp - The current timestamp (in seconds granularity). */
    public void hit(int timestamp) {
        data.set(data.size() - 1, timestamp);
        data.add(Integer.MAX_VALUE);
    }
    
    /** Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity). */
    public int getHits(int timestamp) {
        return getHitsBelow(timestamp + 1) - getHitsBelow(timestamp - 300 + 1);
    }
    
    private int getHitsBelow(int timestamp) {
        int lo = 0;
        int hi = data.size();
        while(lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if(data.get(mid) < timestamp && data.get(mid + 1) >= timestamp) {
                return mid;
            }
            if(data.get(mid) >= timestamp) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return hi;
    }
}
How it will scale if question asked for hit required in past 1000(or any higher value) minutes ?

Below is my solution Insertion O(1) and query time log(N). Idea is similar to binary se

Class Solution(): #Not WORKING:
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
