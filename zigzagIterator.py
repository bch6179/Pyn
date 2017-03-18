[LeetCode] Zigzag Iterator 之字形迭代器
 

Given two 1d vectors, implement an iterator to return their elements alternately.

For example, given two 1d vectors:

v1 = [1, 2]
v2 = [3, 4, 5, 6]
By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].

Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question - Update (2015-09-18):
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example, given the following input:

[1,2,3]
[4,5,6,7]
[8,9]
It should return [1,4,8,2,5,9,3,6,7].

 

这道题让我们写一个之字形迭代器，跟之前那道Flatten 2D Vector有些类似，那道题是横向打印，这道题是纵向打印，虽然方向不同，但是实现思路都是大同小异。我最先想到的方法是用两个变量i和j分别记录两个向量的当前元素位置，初始化为0，然后当i<=j时，则说明需要打印v1数组的元素，反之则打印v2数组中的元素。在hasNext函数中，当i或j打印等于对应数组的长度时，我们将其赋为一个特大值，这样不影响我们打印另一个数组的值，只有当i和j都超过格子数组的长度时，返回false，参见代码如下：

 

解法一：

复制代码
class ZigzagIterator {
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        v.push_back(v1);
        v.push_back(v2);
        i = j = 0;
    }
    int next() {
        return i <= j ? v[0][i++] : v[1][j++];
    }
    bool hasNext() {
        if (i >= v[0].size()) i = INT_MAX;
        if (j >= v[1].size()) j = INT_MAX;
        return i < v[0].size() || j < v[1].size();
    }
private:
    vector<vector<int>> v;
    int i, j;
};
复制代码
 

下面我们来看另一种解法，这种解法直接在初始化的时候就两个数组按照之字形的顺序存入另一个一位数组中了，那么我们就按顺序打印新数组中的值即可，参见代码如下：

 

解法二：

复制代码
class ZigzagIterator {
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        int n1 = v1.size(), n2 = v2.size(), n = max(n1, n2);
        for (int i = 0; i < n; ++i) {
            if (i < n1) v.push_back(v1[i]);
            if (i < n2) v.push_back(v2[i]);
        }
    }
    int next() {
        return v[i++];
    }
    bool hasNext() {
        return i < v.size();
    }
private:
    vector<int> v;
    int i = 0;
};
复制代码
 

由于题目中的Follow up让我们考虑将输入换成k个数组的情况，那么上面两种解法显然就不适用了，所以我们需要一种通解。我们可以采用queue加iterator的方法，用一个queue里面保存iterator的pair，在初始化的时候，有几个数组就生成几个pair放到queue中，每个pair保存该数组的首位置和尾位置的iterator，在next()函数中，我们取出queue队首的一个pair，如果当前的iterator不等于end()，我们将其下一个位置的iterator和end存入队尾，然后返回当前位置的值。在hasNext()函数中，我们只需要看queue是否为空即可，参见代码如下：

 

解法三：

复制代码
class ZigzagIterator {
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        if (!v1.empty()) q.push(make_pair(v1.begin(), v1.end()));
        if (!v2.empty()) q.push(make_pair(v2.begin(), v2.end()));
    }
    int next() {
        auto it = q.front().first, end = q.front().second;
        q.pop();
        if (it + 1 != end) q.push(make_pair(it + 1, end));
        return *it;
    }
    bool hasNext() {
        return !q.empty();
    }
private:
    queue<pair<vector<int>::iterator, vector<int>::iterator>> q;
};

class ZigzagIterator(object):
    
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.l = []
        i = 0
        while i < max(len(v1), len(v2)):
            if i < len(v1):
                self.l.append(v1[i])
            if i < len(v2):
                self.l.append(v2[i])
            i += 1
        self.index = 0

    def next(self):
        """
        :rtype: int
        """
        cur = self.l[self.index]
        self.index += 1
        return cur

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index < len(self.l):
            return True
        else:
            return False

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

class ZigzagIterator(object):
    
    def __init__(self, v1, v2):
        self.data = [(len(v), iter(v)) for v in (v1, v2) if v]

    def next(self):
        len, iter = self.data.pop(0)
        if len > 1:
            self.data.append((len-1, iter))
        return next(iter)

    def hasNext(self):
        return bool(self.data)

class ZigzagIterator(object):
    
    def __init__(self, v1, v2):
        self.vals = (v[i] for i in itertools.count() for v in (v1, v2) if i < len(v))
        self.n = len(v1) + len(v2)

    def next(self):
        self.n -= 1
        return next(self.vals)

    def hasNext(self):
        return self.n > 0
ere's a 8 lines solution for the original question. Since we only saved iterators, space is O(1):
instead of writing my own next function wrapping the list's pop, I can just directly use pop as next :-)

class ZigzagIterator(object):

    def __init__(self, v1, v2):
        self.vals = [x
                     for v in itertools.izip_longest(v1, v2)
                     for x in v
                     if x is not None][::-1]
        self.next = self.vals.pop

    def hasNext(self):
        return bool(self.vals)
class ZigzagIterator {
private:
    queue<pair<vector<int>::iterator, vector<int>::iterator>>q;         // use a queue to record iterators
    
public:
    ZigzagIterator(vector<int>& v1, vector<int>& v2) {
        if (v1.size()) { q.push(make_pair(v1.begin(), v1.end())); }
        if (v2.size()) { q.push(make_pair(v2.begin(), v2.end())); }
    }

    int next() {
        auto p = q.front(); q.pop();
        int val = *(p.first++);                                         // get the next value
        if (p.first != p.second) { q.push(p); }                         // only put next iterator back to queue if it's valid
        return val;
    }

    bool hasNext() {
        return q.size();
    }
};
For the follow up, idea is the same as above - just change v1/v2 to k vectors:

class ZigzagIterator {
private:
    queue<pair<vector<int>::iterator, vector<int>::iterator>>q;
    
public:
    ZigzagIterator(vector<vector<int>>& vecs) {                            // input is k vectors
        for (auto v : vecs) {
            if (v.size()) { q.push(make_pair(v.begin(), v.end())); }        // only record iterators
        }
    }

    int next() {
        auto p = q.front(); q.pop();
        int val = *(p.first++);
        if (p.first != p.second) { q.push(p); }
        return val;
    }

    bool hasNext() {
        return q.size();
    }
};
5 months ago reply quote 
2
POSTS 203
VIEWS Reply Back To Leetcode    Mark unread   Not Watching   Sort by 
0
  zzg_zzm   @soamaaazing
Reputation:  142
@soamaaazing Great strategy to use a queue to handle vector switching. Intuitively, one would employ an additional "indicator" to reference the current vector for next value retrieval (I used an iterator pointing to current vector for k vector case). However, the pop and push operations of queue itself can perform the job for free
lass ZigzagIterator(object):

def __init__(self, v1, v2):
    """
    Initialize your data structure here.
    :type v1: List[int]
    :type v2: List[int]
    """
    self.queue=[_ for _ in (v1,v2) if _]

def next(self):
    """
    :rtype: int
    """
    v=self.queue.pop(0)
    ret=v.pop(0)
    if v: self.queue.append(v)
    return ret

def hasNext(self):
    """
    :rtype: bool
    """
    if self.queue: return True
    return False





My:

  for follow up:
       
      for row in L:
          for j, v in enumerate(row): 
             orderedmap[j].append(v)
  return [w for v in map.values() for w in v]