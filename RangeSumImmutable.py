[LeetCode] Range Sum Query - Mutable 区域和检索 - 可变
 

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
 

这道题是之前那道Range Sum Query - Immutable 区域和检索 - 不可变的延伸，之前那道题由于数组的内容不会改变，所以我们只需要建立一个累计数组就可以支持快速的计算区间值了，而这道题说数组的内容会改变，如果我们还是用之前的方法建立累计和数组，那么每改变一个数字，之后所有位置的数字都要改变，这样如果有很多更新操作的话，就会十分不高效。这道题我们要使用一种新的数据结构，叫做树状数组Binary Indexed Tree，这是一种查询和修改复杂度均为O(logn)的数据结构。这个树状数组比较有意思，所有的奇数位置的数字和原数组对应位置的相同，偶数位置是原数组若干位置之和，假如原数组A(a1, a2, a3, a4 ...)，和其对应的树状数组C(c1, c2, c3, c4 ...)有如下关系：



C1 = A1
C2 = A1 + A2
C3 = A3
C4 = A1 + A2 + A3 + A4
C5 = A5
C6 = A5 + A6
C7 = A7
C8 = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8
...
那么是如何确定某个位置到底是有几个数组成的呢，原来是根据坐标的最低位Low Bit来决定的，所谓的最低位，就是二进制数的最右边的一个1开始，加厚后面的0(如果有的话)组成的数字，例如1到8的最低位如下面所示：

坐标          二进制          最低位

1               0001          1

2               0010          2

3               0011          1

4               0100          4

5               0101          1

6               0110          2

7               0111          1

8               1000          8

...

最低位的计算方法有两种，一种是x&(x^(x–1))，另一种是利用补码特性x&-x。

这道题我们先根据给定输入数组建立一个树状数组bit，然后更新某一位数字时，根据最低位的值来更新后面含有这一位数字的地方，一般只需要更新部分偶数位置的值即可，在计算某一位置的前缀和时，利用树状数组的性质也能高效的很快算出来，参见代码如下：

 

复制代码
class NumArray {
public:
    NumArray(vector<int> &nums) {
        num.resize(nums.size() + 1);
        bit.resize(nums.size() + 1);
        for (int i = 0; i < nums.size(); ++i) {
            update(i, nums[i]);
        }
    }
    void update(int i, int val) {
        int diff = val - num[i + 1];
        for (int j = i + 1; j < num.size(); j += (j&-j)) {
            bit[j] += diff;
        }
        num[i + 1] = val;
    }
    int sumRange(int i, int j) {
        return getSum(j + 1) - getSum(i);
    }    
    int getSum(int i) {
        int res = 0;
        for (int j = i; j > 0; j -= (j&-j)) {
            res += bit[j];
        }
        return res;
    }

private:
    vector<int> num;
    vector<int> bit;
};
复制代码

class BinaryIndexTree(object):
    def __init__(self, nums):
        n = len(nums)
        self.nums = [0 for _ in xrange(n+1)]
        self.N = [0 for _ in xrange(n+1)]
        for i, v in enumerate(nums):
            self.set(i+1, v)

    def _lowbit(self, a):
        return a & -a

    def set(self, i, val):
        diff = val - self.nums[i]
        self.nums[i] = val
        while i < len(self.N):
            self.N[i] += diff
            i += self._lowbit(i)

    def get(self, i):
        ret = 0
        while i > 0:
            ret += self.N[i]
            i -= self._lowbit(i)

        return ret


class NumArray(object):
    def __init__(self, nums):
        self.bit = BinaryIndexTree(nums)

    def update(self, i, val):
        self.bit.set(i+1, val)

    def sumRange(self, i, j):
        return self.bit.get(j+1)-self.bit.get(i)

http://www.hrwhisper.me/leetcode-range-sum-query-mutable/

class NumArray(object):
def __init__(self, nums):
    """
    initialize your data structure here.
    :type nums: List[int]
    """
    self.sum_array = [0] * (len(nums) + 1)
    self.nums = nums
    self.n = len(nums)
    for i in xrange(len(nums)):
        self.add(i + 1,nums[i])


def add(self,x,val):
    while x <= self.n:
        self.sum_array[x] += val
        x += self.lowbit(x)


def lowbit(self,x):
    return x & -x

def sum(self,x):
    res = 0
    while x >0:
        res += self.sum_array[x]
        x -= self.lowbit(x)
    return res

def update(self, i, val):
    """
    :type i: int
    :type val: int
    :rtype: int
    """
    self.add(i + 1, val - self.nums[i])
    self.nums[i] = val

def sumRange(self, i, j):
    """
    sum of elements nums[i..j], inclusive.
    :type i: int
    :type j: int
    :rtype: int
    """
    if not self.nums: return  0
    return self.sum(j+1) - self.sum(i)