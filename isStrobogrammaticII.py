[LeetCode] Strobogrammatic Number II 对称数之二
 

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

Hint:

Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.
 

这道题是之前那道Strobogrammatic Number的拓展，那道题让我们判断一个数是否是对称数，而这道题让我们找出长度为n的所有的对称数，我们肯定不能一个数一个数的来判断，那样太不高效了，而且OJ肯定也不会答应。题目中给了提示说可以用递归来做，而且提示了递归调用n-2，而不是n-1。我们先来列举一下n为0,1,2,3,4的情况：

n = 0:   none

n = 1:   0, 1, 8

n = 2:   11, 69, 88, 96

n = 3:   101, 609, 808, 906, 111, 619, 818, 916, 181, 689, 888, 986

n = 4:   1001, 6009, 8008, 9006, 1111, 6119, 8118, 9116, 1691, 6699, 8698, 9696, 1881, 6889, 8888, 9886, 1961, 6969, 8968, 9966

我们注意观察n=0和n=2，可以发现后者是在前者的基础上，每个数字的左右增加了[1 1], [6 9], [8 8], [9 6]，看n=1和n=3更加明显，在0的左右增加[1 1]，变成了101, 在0的左右增加[6 9]，变成了609, 在0的左右增加[8 8]，变成了808, 在0的左右增加[9 6]，变成了906, 然后在分别在1和8的左右两边加那四组数，我们实际上是从m=0层开始，一层一层往上加的，需要注意的是当加到了n层的时候，左右两边不能加[0 0]，因为0不能出现在两位数及多位数的开头，在中间递归的过程中，需要有在数字左右两边各加上0的那种情况，参见代码如下：  

 def findStrobogrammatic(self, n):
        nums = n%2 * list('018') or ['']
    while n > 1:
        n -= 2  # put this ealier to solve the dillma of 4 and 2
        nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n<2:] for num in nums]
    return nums

    class Solution(object):
        def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(m,n):
            if m == 0: return ['']
            if m == 1: return list('018')
            
            return [ a+g+b for a,b in '00 11 88 69 96'.split()[m==n:] for g in dfs(m-2, n) ]
            
        if n == 0: return []
        return dfs(n,n)

解法一：

复制代码
class Solution {
public:
    vector<string> findStrobogrammatic(int n) {
        return find(n, n);
    }
    vector<string> find(int m, int n) {
        if (m == 0) return {""};
        if (m == 1) return {"0", "1", "8"};
        vector<string> t = find(m - 2, n), res;
        for (auto a : t) {
            if (m != n) res.push_back("0" + a + "0");
            res.push_back("1" + a + "1");
            res.push_back("6" + a + "9");
            res.push_back("8" + a + "8");
            res.push_back("9" + a + "6");
        }
        return res;
    }
};
复制代码
 

这道题还有迭代的解法，感觉也相当的巧妙，需要从奇偶来考虑，奇数赋为0,1,8，偶数赋为空，如果是奇数，就从i=3开始搭建，因为计算i=3需要i=1，而我们已经初始化了i=1的情况，如果是偶数，我们从i=2开始搭建，我们也已经初始化了i=0的情况，所以我们可以用for循环来搭建到i=n的情况，思路和递归一样，写法不同而已，参见代码如下：

 

解法二：

复制代码
class Solution {
public:
    vector<string> findStrobogrammatic(int n) {
        vector<string> one{"0", "1", "8"}, two{""}, res = two;
        if (n % 2 == 1) res = one;
        for (int i = (n % 2) + 2; i <= n; ++i) {
            vector<string> t;
            for (auto a : res) {
                if (i != n) t.push_back("0" + a + "0");
                t.push_back("1" + a + "1");
                t.push_back("6" + a + "9");
                t.push_back("8" + a + "8");
                t.push_back("9" + a + "6");
            }
            res = t;
        }
        return res;
    }
};
复制代码


n == 1: [0, 1, 8]

n == 2: [11, 88, 69, 96]

How about n == 3?
=> it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 2

n == 4?
=> it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 2

n == 5?
=> it can be retrieved if you insert [0, 1, 8] to the middle of solution of n == 4

the same, for n == 6, it can be retrieved if you insert [11, 88, 69, 96, 00] to the middle of solution of n == 4

def findStrobogrammatic(self, n):
    evenMidCandidate = ["11","69","88","96", "00"]
    oddMidCandidate = ["0", "1", "8"]
    if n == 1:
        return oddMidCandidate
    if n == 2:
        return evenMidCandidate[:-1]
    if n % 2:
        pre, midCandidate = self.findStrobogrammatic(n-1), oddMidCandidate
    else: 
        pre, midCandidate = self.findStrobogrammatic(n-2), evenMidCandidate
    premid = (n-1)/2
    return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]

    def findStrobogrammatic(self, n):
        nums = n%2 * list('018') or ['']
    while n > 1:
        n -= 2
        nums = [a + num + b for a, b in '00 11 88 69 96'.split()[n<2:] for num in nums]
    return nums

    class Solution(object):
    def findStrobogrammatic(self, n, zero=False):
        if n==0:
            return [''] if zero else []
        if n==1:
            return ['1','8','0']

        validNums='0186969810' if zero else '18696981'
        return [validNums[i]+stg+validNums[-i-1] for i in xrange(len(validNums)/2) for stg in self.findStrobogrammatic(n-2, True)]