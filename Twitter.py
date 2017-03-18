https://leetcode.com/problems/design-twitter/#/description

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);


class Twitter(object):
    
    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)

 . You could've used a heap in which you store only the heads and then do 10 extractions (similar to what we do when we merge k sorted linked lists. Check out https://leetcode.com/discuss/108303/simple-and-clean-python-code-o-logk-for-getting-news-feed, but I am sure you already noticed that. Beautiful code, as always.

 heapq.merge(): "Merge multiple sorted inputs into a single sorted output (for example, merge timestamped entries from multiple log files). Returns an iterator over the sorted values."

Ok, it's an iterator, fair enough. But what is the complexity ofitertools.islice afterwards? Not sure about that.

9 months ago reply quote 
0
  StefanPochmann  
Reputation:  14,053
Same complexity as yours. You implemented it differently, but you're really doing the exact same thing.
@alexei5 No, that's actually much worse than mine. I'm not going through all of their tweets. Everything I use is lazy and doesn't look at more than it absolutely needs to

Simple and Clean Python code, O(logK) for getting news feed

9
  agave 
Reputation:  504
 import heapq

class Twitter(object):

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.followee = {}
        

    def postTweet(self, user, tweet):
        self.time += 1
        self.tweets[user] = self.tweets.get(user, []) + [(-self.time,  tweet)]
        
        

    def getNewsFeed(self, user):
        h, tweets = [], self.tweets
        people = self.followee.get(user, set()) | set([user])
        for person in people:
            if person in tweets and tweets[person]:
                time, tweet = tweets[person][-1]
                h.append((time, tweet, person, len(tweets[person]) - 1))
        heapq.heapify(h)
        news = []
        for _ in range(10):
            if h:
                time, tweet, person, idx = heapq.heappop(h)
                news.append(tweet)
                if idx:
                    new_time, new_tweet = tweets[person][idx-1]
                    heapq.heappush(h, (new_time, new_tweet, person, idx - 1))
        return news
        
        

    def follow(self, follower, other):
        self.followee[follower] = self.followee.get(follower, set()) | set([other])
        
        

    def unfollow(self, follower, other):
        if follower in self.followee:
            self.followee[follower].discard(other)
K is the number of followee of user. We have O(log(K)) runtime for getting news feed because we do maximum 10 extractions in a heap that holds maximum K elements (similar to what is done in merge K linked lists). The other ops are obviously O(1).

t think heapify is O(logn) operation.
Yes, insert and remove operation for heap only need O(logn). But what you did is to build a max-heap from an unsorted (but distinct) sequential container, the time complexity is O(n).

Anyway, thanks for your post. I posted an algorithm in C++ days ago, and I used the same method as you. The time complexity is O(n), and I'm shocked when seeing you can achieve O(logn) for getting news feed.

Please correct me if I'm wrong.

I do not think this will work well in a real system. You need to consider that data are actually stored on a database. The algorithm used in merge K lists will access DB many times. We can just pull 10 tweets from each followed user and find the top K tweets using any algorithm. The time spent on memory is much less than the time spent on DB reading which is reading the physical disk.

8 months ago reply quote 
0
  agave   @jedihy
Reputation:  504
@jedihy I don't get what you're saying. You can cache the database in main memory... Besides, what you just describe is not less than O(log(K)).

8 months ago reply quote 
0
  jedihy 
Reputation:  210
Yes but cache is expensive. The way I just describe is greater than O(log(K)) obviously but it does not matter. It will perform exactly 10 PULL operations to get tweets. Yours will do at most 20 PULL operations. The overhead on selecting the top K elements could be ignored compared to DB reading.

Anyway, as you said, we can cache these in memory. I probably overthink it.       
public class Twitter {
    private static int timeStamp=0;
    
    // easy to find if user exist
    private Map<Integer, User> userMap;
    
    // Tweet link to next Tweet so that we can save a lot of time
    // when we execute getNewsFeed(userId)
    private class Tweet{
        public int id;
        public int time;
        public Tweet next;
        
        public Tweet(int id){
            this.id = id;
            time = timeStamp++;
            next=null;
        }
    }
    
    
    // OO design so User can follow, unfollow and post itself
    public class User{
        public int id;
        public Set<Integer> followed;
        public Tweet tweet_head;
        
        public User(int id){
            this.id=id;
            followed = new HashSet<>();
            follow(id); // first follow itself
            tweet_head = null;
        }
        
        public void follow(int id){
            followed.add(id);
        }
        
        public void unfollow(int id){
            followed.remove(id);
        }
        
        
        // everytime user post a new tweet, add it to the head of tweet list.
        public void post(int id){
            Tweet t = new Tweet(id);
            t.next=tweet_head;
            tweet_head=t;
        }
    }
    
    
    

    /** Initialize your data structure here. */
    public Twitter() {
        userMap = new HashMap<Integer, User>();
    }
    
    /** Compose a new tweet. */
    public void postTweet(int userId, int tweetId) {
        if(!userMap.containsKey(userId)){
            User u = new User(userId);
            userMap.put(userId, u);
        }
        userMap.get(userId).post(tweetId);
            
    }
    

    
    // Best part of this.
    // first get all tweets lists from one user including itself and all people it followed.
    // Second add all heads into a max heap. Every time we poll a tweet with 
    // largest time stamp from the heap, then we add its next tweet into the heap.
    // So after adding all heads we only need to add 9 tweets at most into this 
    // heap before we get the 10 most recent tweet.
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> res = new LinkedList<>();

        if(!userMap.containsKey(userId))   return res;
        
        Set<Integer> users = userMap.get(userId).followed;
        PriorityQueue<Tweet> q = new PriorityQueue<Tweet>(users.size(), (a,b)->(b.time-a.time));
        for(int user: users){
            Tweet t = userMap.get(user).tweet_head;
            // very imporant! If we add null to the head we are screwed.
            if(t!=null){
                q.add(t);
            }
        }
        int n=0;
        while(!q.isEmpty() && n<10){
          Tweet t = q.poll();
          res.add(t.id);
          n++;
          if(t.next!=null)
            q.add(t.next);
        }
        
        return res;
        
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    public void follow(int followerId, int followeeId) {
        if(!userMap.containsKey(followerId)){
            User u = new User(followerId);
            userMap.put(followerId, u);
        }
        if(!userMap.containsKey(followeeId)){
            User u = new User(followeeId);
            userMap.put(followeeId, u);
        }
        userMap.get(followerId).follow(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    public void unfollow(int followerId, int followeeId) {
        if(!userMap.containsKey(followerId) || followerId==followeeId)
            return;
        userMap.get(followerId).unfollow(followeeId);
    }
}

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter obj = new Twitter();
 * obj.postTweet(userId,tweetId);
 * List<Integer> param_2 = obj.getNewsFeed(userId);
 * obj.follow(followerId,followeeId);
 * obj.unfollow(followerId,followeeId);
 */

 The idea is upon tweet creation, broadcast it to all followers' newsFeed." This is not a good idea. For popular accounts, the followers can be millions. it's not reasonable to broadcast to all of them since most of them may not want to get the newsFeeds.

I think the current design in this post is reasonable, you should refresh the newsFeeds based on the current account request, not based on the followees' post.

Build the heap will take O(nlogn) time where n is the number of followed. I think just using an n-way merge will cost only 10*n which is faster theoretically.

Please correct me if I am wrong.

@lufangjianle I read this article http://highscalability.com/blog/2013/7/8/the-architecture-twitter-uses-to-deal-with-150m-active-users.html, then solved this problem in the way more or less as you said.

Since the traffic to read timeline is much larger than post a tweet, Twitter chose to precompute the timeline in Redis cluster. When the followee posts, the follower list will be pulled out of a service called Social Graph by Fanout service. Then it will inserts the new tweet id into each timeline of the follower.

Of course, this is an out-of-date article. It is supposed to be changed a lot. :) Here is key part of my solution. The timeline is precomputed beforehand.

    public void postTweet(int userId, int tweetId) {
        Tweet tw = new Tweet(tweetId);
        if (getTweets(userId).add(tw)) {
            getTimeline(userId).add(tw);
            for (int follower : getFollower(userId))
                getTimeline(follower).add(tw);
        }
    }

    public List<Integer> getNewsFeed(int userId) {
        List<Integer> ret = new ArrayList<>();
        int size = 0;
        for (Tweet tw : getTimeline(userId)) {
            if (++size > 10) break;
            ret.add(tw.id);
        }
        return ret;
    }