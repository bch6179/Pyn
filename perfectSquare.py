[LeetCode] Perfect Squares 完全平方数
 

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

 compute the next value to append to dp, i.e., how many squares I need for the number len(dp). Python supports indexing from the end with negative indexes, so the already computed dp[-1] tells me how many squares I need for the previous number (1 smaller than the number I'm handling now), dp[-4] tells me how many squares I need for the number that's 4 smaller than the number I'm handling now, etc.

public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n+1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for(int i = 1; i <= n; i++){
            for(int j = 1; j * j <= i; j++){
                dp[i] = Math.min(dp[i], dp[i - j*j] + 1);
            }
        }
        return dp[n];
    }
}

Of course you can just use O(1) space to solve this problem, you can refer to Lagrange's four-square theorem and try to find out a mathematical solution(in fact, there're some leetcoders using this), but in this case, if you insist on using DP to solve it, I don't think you can bring the space complexity down, here dp[n] doens't only depend on dp[n-1], you have to keep { dp[n - ii] + 1 , n - ii >=0 && i >= 1 } until you get the best dp[n].

about a year ago reply quote 
0
D derkhalifa 
Reputation:  -1
Can someone help us explain why the complexity is O(n)?
this is a sum of all square roots from 1 to n .. is this proven to be equivalent to O(n) ?

p[n] indicates that the perfect squares count of the given n, and we have:


dp[0] = 0 
dp[1] = dp[0]+1 = 1
dp[2] = dp[1]+1 = 2
dp[3] = dp[2]+1 = 3
dp[4] = Min{ dp[4-1*1]+1, dp[4-2*2]+1 } 
      = Min{ dp[3]+1, dp[0]+1 } 
      = 1				
dp[5] = Min{ dp[5-1*1]+1, dp[5-2*2]+1 } 
      = Min{ dp[4]+1, dp[1]+1 } 
      = 2
						.
						.
						.
dp[13] = Min{ dp[13-1*1]+1, dp[13-2*2]+1, dp[13-3*3]+1 } 
       = Min{ dp[12]+1, dp[9]+1, dp[4]+1 } 
       = 2
						.
						.
						.
dp[n] = Min{ dp[n - i*i] + 1 },  n - i*i >=0 && i >= 1
 

又是超哥一个人辛苦的更新题目，一个人托起LeetCode免费题的一片天空啊，赞一个~ 这道题说是给我们一个正整数，求它最少能由几个完全平方数组成。这道题是考察四平方和定理，to be honest, 这是我第一次听说这个定理，天啦撸，我的数学是语文老师教的么?! 闲话不多扯，回来做题。先来看第一种很高效的方法，根据四平方和定理，任意一个正整数均可表示为4个整数的平方和，其实是可以表示为4个以内的平方数之和，那么就是说返回结果只有1,2,3或4其中的一个，首先我们将数字化简一下，由于一个数如果含有因子4，那么我们可以把4都去掉，并不影响结果，比如2和8,3和12等等，返回的结果都相同，读者可自行举更多的栗子。还有一个可以化简的地方就是，如果一个数除以8余7的话，那么肯定是由4个完全平方数组成，这里就不证明了，因为我也不会证明，读者可自行举例验证。那么做完两步后，一个很大的数有可能就会变得很小了，大大减少了运算时间，下面我们就来尝试的将其拆为两个平方数之和，如果拆成功了那么就会返回1或2，因为其中一个平方数可能为0. (注：由于输入的n是正整数，所以不存在两个平方数均为0的情况)。注意下面的!!a + !!b这个表达式，可能很多人不太理解这个的意思，其实很简单，感叹号!表示逻辑取反，那么一个正整数逻辑取反为0，再取反为1，所以用两个感叹号!!的作用就是看a和b是否为正整数，都为正整数的话返回2，只有一个是正整数的话返回1，参见代码如下：

 

解法一：

复制代码
class Solution {
public:
    int numSquares(int n) {
        while (n % 4 == 0) n /= 4;
        if (n % 8 == 7) return 4;
        for (int a = 0; a * a <= n; ++a) {
            int b = sqrt(n - a * a);
            if (a * a + b * b == n) {
                return !!a + !!b;
            }
        }
        return 3;
    }
};
复制代码
 

这道题远不止这一种解法，我们还可以用动态规划Dynamic Programming来做，我们建立一个长度为n+1的一维dp数组，将第一个值初始化为0，其余值都初始化为INT_MAX, i从0循环到n，j从1循环到i+j*j <= n的位置，然后每次更新dp[i+j*j]的值，动态更新dp数组，其中dp[i]表示正整数i能少能由多个完全平方数组成，那么我们求n，就是返回dp[n]即可，也就是dp数组的最后一个数字，参见代码如下：

 

解法二：

复制代码
// DP
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        for (int i = 0; i <= n; ++i) {
            for (int j = 1; i + j * j <= n; ++j) {
                dp[i + j * j] = min(dp[i + j * j], dp[i] + 1);
            }
        }
        return dp.back();
    }
};
复制代码
 

下面再来看一种DP解法，这种解法跟上面有些不同，上面那种解法是初始化了整个长度为n+1的dp数字，但是初始化的顺序不定的，而这个种方法只初始化了第一个值为0，那么在循环里计算，每次增加一个dp数组的长度，里面那个for循环一次循环结束就算好下一个数由几个完全平方数组成，直到增加到第n+1个，返回即可，想更直观的看这两种DP方法的区别，建议每次循环后都打印出dp数字的值来观察其更新的顺序，参见代码如下：

 

解法三：

复制代码
// DP
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(1, 0);
        while (dp.size() <= n) {
            int m = dp.size(), val = INT_MAX;
            for (int i = 1; i * i <= m; ++i) {
                val = min(val, dp[m - i * i] + 1);
            }
            dp.push_back(val);
        }
        return dp.back();
    }
};
复制代码
 

最后我们来介绍一种递归Recursion的解法，这种方法的好处是写法简洁，但是运算效率不敢恭维。我们的目的是遍历所有比n小的完全平方数，然后对n与完全平方数的差值递归调用函数，目的是不断更新最终结果，知道找到最小的那个，参见代码如下：

 

解法四：

复制代码
// Recrusion
class Solution {
public:
    int numSquares(int n) {
        int res = n, num = 2;
        while (num * num <= n) {
            int a = n / (num * num), b = n % (num * num);
            res = min(res, a + numSquares(b));
            ++num;
        }
        return res;
    }
};
复制代码
 

PS：解法二三四的运算效率真的不高，强推解法一，高效又易懂，如果想强行优化后三个算法，可以将解法一的前两个if判断加到后三个的算法的开头，能很大的提高运算效率。
Dynamic Programming: 440ms

class Solution 
{
public:
    int numSquares(int n) 
    {
        if (n <= 0)
        {
            return 0;
        }
        
        // cntPerfectSquares[i] = the least number of perfect square numbers 
        // which sum to i. Note that cntPerfectSquares[0] is 0.
        vector<int> cntPerfectSquares(n + 1, INT_MAX);
        cntPerfectSquares[0] = 0;
        for (int i = 1; i <= n; i++)
        {
            // For each i, it must be the sum of some number (i - j*j) and 
            // a perfect square number (j*j).
            for (int j = 1; j*j <= i; j++)
            {
                cntPerfectSquares[i] = 
                    min(cntPerfectSquares[i], cntPerfectSquares[i - j*j] + 1);
            }
        }
        
        return cntPerfectSquares.back();
    }
};
2.Static Dynamic Programming: 12ms

class Solution 
{
public:
    int numSquares(int n) 
    {
        if (n <= 0)
        {
            return 0;
        }
        
        // cntPerfectSquares[i] = the least number of perfect square numbers 
        // which sum to i. Since cntPerfectSquares is a static vector, if 
        // cntPerfectSquares.size() > n, we have already calculated the result 
        // during previous function calls and we can just return the result now.
        static vector<int> cntPerfectSquares({0});
        
        // While cntPerfectSquares.size() <= n, we need to incrementally 
        // calculate the next result until we get the result for n.
        while (cntPerfectSquares.size() <= n)
        {
            int m = cntPerfectSquares.size();
            int cntSquares = INT_MAX;
            for (int i = 1; i*i <= m; i++)
            {
                cntSquares = min(cntSquares, cntPerfectSquares[m - i*i] + 1);
            }
            
            cntPerfectSquares.push_back(cntSquares);
        }
        
        return cntPerfectSquares[n];
    }
};
3.Mathematical Solution: 4ms

class Solution 
{  
private:  
    int is_square(int n)
    {  
        int sqrt_n = (int)(sqrt(n));  
        return (sqrt_n*sqrt_n == n);  
    }
    
public:
    // Based on Lagrange's Four Square theorem, there 
    // are only 4 possible results: 1, 2, 3, 4.
    int numSquares(int n) 
    {  
        // If n is a perfect square, return 1.
        if(is_square(n)) 
        {
            return 1;  
        }
        
        // The result is 4 if and only if n can be written in the 
        // form of 4^k*(8*m + 7). Please refer to 
        // Legendre's three-square theorem.
        while ((n & 3) == 0) // n%4 == 0  
        {
            n >>= 2;  
        }
        if ((n & 7) == 7) // n%8 == 7
        {
            return 4;
        }
        
        // Check whether 2 is the result.
        int sqrt_n = (int)(sqrt(n)); 
        for(int i = 1; i <= sqrt_n; i++)
        {  
            if (is_square(n - i*i)) 
            {
                return 2;  
            }
        }  
        
        return 3;  
    }  
}; 
4.Breadth-First Search: 80ms

class Solution 
{
public:
    int numSquares(int n) 
    {
        if (n <= 0)
        {
            return 0;
        }
        
        // perfectSquares contain all perfect square numbers which 
        // are smaller than or equal to n.
        vector<int> perfectSquares;
        // cntPerfectSquares[i - 1] = the least number of perfect 
        // square numbers which sum to i.
        vector<int> cntPerfectSquares(n);
        
        // Get all the perfect square numbers which are smaller than 
        // or equal to n.
        for (int i = 1; i*i <= n; i++)
        {
            perfectSquares.push_back(i*i);
            cntPerfectSquares[i*i - 1] = 1;
        }
        
        // If n is a perfect square number, return 1 immediately.
        if (perfectSquares.back() == n)
        {
            return 1;
        }
        
        // Consider a graph which consists of number 0, 1,...,n as
        // its nodes. Node j is connected to node i via an edge if  
        // and only if either j = i + (a perfect square number) or 
        // i = j + (a perfect square number). Starting from node 0, 
        // do the breadth-first search. If we reach node n at step 
        // m, then the least number of perfect square numbers which 
        // sum to n is m. Here since we have already obtained the 
        // perfect square numbers, we have actually finished the 
        // search at step 1.
        queue<int> searchQ;
        for (auto& i : perfectSquares)
        {
            searchQ.push(i);
        }
        
        int currCntPerfectSquares = 1;
        while (!searchQ.empty())
        {
            currCntPerfectSquares++;
            
            int searchQSize = searchQ.size();
            for (int i = 0; i < searchQSize; i++)
            {
                int tmp = searchQ.front();
                // Check the neighbors of node tmp which are the sum 
                // of tmp and a perfect square number.
                for (auto& j : perfectSquares)
                {
                    if (tmp + j == n)
                    {
                        // We have reached node n.
                        return currCntPerfectSquares;
                    }
                    else if ((tmp + j < n) && (cntPerfectSquares[tmp + j - 1] == 0))
                    {
                        // If cntPerfectSquares[tmp + j - 1] > 0, this is not 
                        // the first time that we visit this node and we should 
                        // skip the node (tmp + j).
                        cntPerfectSquares[tmp + j - 1] = currCntPerfectSquares;
                        searchQ.push(tmp + j);
                    }
                    else if (tmp + j > n)
                    {
                        // We don't need to consider the nodes which are greater ]
                        // than n.
                        break;
                    }
                }
                
                searchQ.pop();
            }
        }
        
        return 0;
    }
};
2 years ago reply quote 
SOLUTION-SHARING 15.9k CPP 4.3k 47
POSTS 30.5k
VIEWS Reply Back To Leetcode    Mark unread   Not Watching   Sort by 
41
A AaronHui 
Reputation:  41
why Static Dynamic Programming is faster than Dynamic Programming

2 years ago reply quote 
1
C ckclark   @AaronHui
Reputation:  1
The table can be reused.

2 years ago reply quote 
2
Z zhukov   @AaronHui
Reputation:  471
Yes, for example, if you first call numSquares(100), a table with size 101 will be built. Then if you call numSquares(10), the function doesn't need to rebuild the table and it will immediately return the entry with index 10.

2 years ago reply quote 
0
B Boris.laifu 
Reputation:  0
thanks for the explanation.

2 years ago reply quote 
7
T TonyLic   @AaronHui
Reputation:  116
static DP is equivalent to DP if you only call function once. However, if you call it several times, static vector would be reused and make whole test cases much faster.

about a year ago reply quote 
1
B bipedalbit 
Reputation:  4
Static vector is taking advantage of the online judge procedure. Kind of weird isn't it? By the way, so curious about the magic 4^k*(8*m + 7)!

about a year ago reply quote 
1
X xuewuxiao 
Reputation:  123
My solution is 200ms on leetcode.
I think this can be regarded as dfs.
start from n, minus square one by one, finally, reach zero. in all these solution, we keep the minimum.
I use a variable level to avoid going to unnecessary deep level. thus save a lot of time.

class Solution {
public:
    int numSquares(int n) {
        vector<int> nums(n+1);
        return helper(n, nums, n);
    }
    
    int helper(int n, vector<int>& nums, int level) {
        if (!n)
            return 0;
        if (nums[n])
            return nums[n];
        if (!level)
            return -1;
            
        --level;
        const int up = sqrt(n);
        int ans = n;
        int res = n;
        for (int i=up; i>=1 && res; i--) {
            res = helper(n-i*i, nums, min(ans, level));
            if (res >= 0)
                ans = min(ans, res);
        }
        nums[n] = ans + 1;
        return nums[n];
    }
};

My DP solution with memoization. It is not fast as the static DP solution though (my run time is 186ms); not sure why yet.

public int numSquares(int n) {
    
    int[] res = new int[n+1];
    for(int i=1; i<=n; i++)
        res[i] = Integer.MAX_VALUE; // memoize the result in a vector, i.e., res[i] stores the length of target i

    return getResult(res, n)[n];
}

public int[] getResult(int[] res, int k) {
    if(k==1) {
        res[k] = 1;
        return res;
    }
    
    // if already stored, just return the value
    if(res[k]<Integer.MAX_VALUE)
        return res;
    // if not stored yet, compute it recursively.
    else {
        for(int i=1; i<=k; i++) {
            int is = i*i;
            if(is>k) break; // only need to run the for loop up to sqrt(i)
            res[k] = Math.min(res[k], 1+getResult(res, k-is)[k-is]);
        }
    }
    return res;
}

class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

        re so many "large" test cases that it's worthwhile to keep data between test cases rather than recomputing from scratch all the time. At least in the slower languages. My dp tells the numbers of squares needed for the first integers, and when asked about a new n, I extend dp just as much as necessary.
 