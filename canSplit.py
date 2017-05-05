[LeetCode] Split Array Largest Sum 分割数组的最大值
 

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
Given m satisfies the following constraint: 1 ≤ m ≤ length(nums) ≤ 14,000.

Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
 二分枚举答案（Binary Search）

将数组nums拆分成m个子数组，每个子数组的和不小于sum(nums) / m，不大于sum(nums)

又因为数组nums中只包含非负整数，因此可以通过二分法在上下界内枚举答案。

时间复杂度O(n * log m)，其中n是数组nums的长度，m为数组nums的和

Python代码：
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        size = len(nums)
        high = sum(nums)
        low = high / m
        while low <= high:
            mid = (low + high) / 2
            n = m
            cnt = 0
            valid = True
            for x in range(size):
                if nums[x] > mid:
                    valid = False
                    break
                if cnt + nums[x] > mid:
                    n -= 1
                    cnt = 0
                cnt += nums[x]
                if n == 0:
                    valid = False
                    break
            if valid:
                high = mid - 1
            else:
                low = mid + 1
        return low

这道题给了我们一个非负数的数组nums和一个整数m，让我们把数组分割成m个非空的连续子数组，让我们最小化m个子数组中的最大值。开始以为要用博弈论中的最小最大化算法，可是想了半天发现并不会做，于是后面决定采用无脑暴力破解，在nums中取出所有的m个子数组的情况都找一遍最大值，为了加快求子数组和的运算，还建立了累计和数组，可以还是TLE了，所以博主就没有办法了，只能上网参考大神们的解法，发现大家普遍使用了二分搜索法来做，感觉特别巧妙，原来二分搜索法还能这么用，厉害了我的哥。我们首先来分析，如果m和数组nums的个数相等，那么每个数组都是一个子数组，所以返回nums中最大的数字即可，如果m为1，那么整个nums数组就是一个子数组，返回nums所有数字之和，所以对于其他有效的m值，返回的值必定在上面两个值之间，所以我们可以用二分搜索法来做。我们用一个例子来分析，nums = [1, 2, 3, 4, 5], m = 3，我们将left设为数组中的最大值5，right设为数字之和15，然后我们算出中间数为10，我们接下来要做的是找出和最大且小于等于10的子数组的个数，[1, 2, 3, 4], [5]，可以看到我们无法分为3组，说明mid偏大，所以我们让right=mid，然后我们再次进行二分查找哦啊，算出mid=7，再次找出和最大且小于等于7的子数组的个数，[1,2,3], [4], [5]，我们成功的找出了三组，说明mid还可以进一步降低，我们让right=mid，然后我们再次进行二分查找哦啊，算出mid=6，再次找出和最大且小于等于6的子数组的个数，[1,2,3], [4], [5]，我们成功的找出了三组，我们尝试着继续降低mid，我们让right=mid，然后我们再次进行二分查找哦啊，算出mid=5，再次找出和最大且小于等于5的子数组的个数，[1,2], [3], [4], [5]，发现有4组，此时我们的mid太小了，应该增大mid，我们让left=mid+1，此时left=6，right=5，循环退出了，我们返回left即可，参见代码如下：

 

复制代码
class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        long long left = 0, right = 0;
        for (int i = 0; i < nums.size(); ++i) {
            left = max((int)left, nums[i]);
            right += nums[i];
        }
        while (left < right) {
            long long mid = left + (right - left) / 2;
            if (can_split(nums, m, mid)) right = mid;
            else left = mid + 1;
        }
        return left;
    }
    bool can_split(vector<int>& nums, int m, int sum) {
        int cnt = 1, curSum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            curSum += nums[i];
            if (curSum > sum) {
                curSum = nums[i];
                ++cnt;
                if (cnt > m) return false;
            }
        }
        return true;
    }
};
复制代码
这道题有DP和binary search两种做法。DP的话实现起来稍微麻烦一点，需要保存一个2d的array，大小为n*m，每个位置（i，j）保存从数列位置i开始到数列尾端，分割成j份的largest sum。同时空间和时间复杂度在m比较大的情况下比较高，并不是很建议勇这种方法implement，但是可以作为一种思路。类似的题目可以参考Burst Balloons。

另一种就是利用sum是整数的性质进项binary search。UB (upper bound) 是所有原array的所有数字的和，LB (lower bound) 是UB/m以数组中最大值两者之间的较大者。然后根据binary search的方式去验证给定的array能否依据这个largest sum进行分割。需要注意的是，这里sum需要使用long而不是int，不然会有overflow的问题。世间复杂度是O(n log sum) <= O(n log n*Integer.MAX_VALUE) <= O(n (logn + c)) = O(n logn)，额外的空间复杂度为O(1)。    p的subproblem是：
dp[i][j]: split nums[0:i] into j parts, 
dp的方程是：
dp[i][j] = min{ max{dp[k][j-1], sum(nums[k+1:i+1])} }, 
每个subproblem都遍历一遍可能的k，选择出最小的结果。注意由于array不含负数，dp[k-1] <= dp[k] 并且sum(nums[k:i+1]) >= sum(nums[k+1:i+1])，相当于一条递增，一条递减的线找交点，极端情况没有交点结果出现在两端，所以依然可以binary search找dp[k] == sum(nums[k+1:i+1])。

，试图计算平均值，再每次尽量均分。

。  但这样， 会有一种情况
average = 100,   m = 
1,2,4,5,6 99,99, 10, 9 ,8 , 7, .....    这样的情况，还是需要把两个99 分开。 那样左

这样结束后， 需要 左右挪动 每个位置，  这样就会互相影响。
因此，这个应该是行不通的。

-------》  考虑分而治之的思想 , 再考虑， m的情况，可以分为 a+b = m的两种情况，因此我们试着考虑DP 算法
首先我考虑的是2维的DP，就是对于index (a,b) inclusive, 可以分成的最小的情况。

但是由于 m == 14,000，因此可能空间太大了。

因此考虑1维的， 由此变成，每次取下最前面的一个（或者几个），然后再分后面的till the end of nums array。
由此，数组就变成了 n * m的了。

?
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
public class Solution {
    public int splitArray(int[] nums, int m) {
        int[][] DP = new int[nums.length][m];
        int n = nums.length;
        for(int i =0;i<n ;i++)
            Arrays.fill(DP[i],-1);
        int[] sumToEnd = new int[n];
        for(int i = n-1; i>=0; i--)
            sumToEnd[i] = nums[i]+ ( i==n-1 ? 0: sumToEnd[i+1] );
        return helper(nums, 0, DP, m, sumToEnd);
    }
    private int helper(int[] nums, int start, int[][] DP, int m, int[] sumToEnd){
        if(DP[start][m-1] == -1){// if have not been initialized
            if(m == 1){
                DP[start][m-1] = sumToEnd[start];
            }else{//detach the head, and recursively calculate the part
                int res = Integer.MAX_VALUE, frontSum = 0;
                for(int i =start;i<= nums.length-m;i++){
                    frontSum += nums[i];
                    int restLargestSum = helper(nums,i+1, DP, m-1, sumToEnd);
                    res = Math.min(res, Math.max(frontSum, restLargestSum));
                    if(frontSum >= restLargestSum)
                        break;
                }
                DP[start][m-1] = res;
            }
        }
        return DP[start][m-1];
    }
}

DP solution. This is obviously not as good as the binary search solutions; but it did pass OJ.

dp[s,j] is the solution for splitting subarray n[j]...n[L-1] into s parts.

dp[s+1,i] = min{ max(dp[s,j], n[i]+...+n[j-1]) }, i+1 <= j <= L-s

This solution does not take advantage of the fact that the numbers are non-negative (except to break the inner loop early). That is a loss. (On the other hand, it can be used for the problem containing arbitrary numbers)

public int splitArray(int[] nums, int m)
{
    int L = nums.length;
    int[] S = new int[L+1];
    S[0]=0;
    for(int i=0; i<L; i++)
        S[i+1] = S[i]+nums[i];

    int[] dp = new int[L];
    for(int i=0; i<L; i++)
        dp[i] = S[L]-S[i];

    for(int s=1; s<m; s++)
    {
        for(int i=0; i<L-s; i++)
        {
            dp[i]=Integer.MAX_VALUE;
            for(int j=i+1; j<=L-s; j++)
            {
                int t = Math.max(dp[j], S[j]-S[i]);
                if(t<=dp[i])
                    dp[i]=t;
                else
                    break;
            }
        }
    }

    return dp[0];   

    import sys
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        dp = [[sys.maxint]*(m) for _ in range(len(nums)+1)]
        acc = 0
        dp[0][0] = 0
        for i in range(1, len(nums)+1):
            acc += nums[i - 1]
            dp[i][0] = acc

        for j in range(m):
            dp[0][j] = 0

        for i in range(1, len(nums)+1):
            for i_ in range(i):
                for j in range(1, m):
                    dp[i][j] = min(dp[i][j], max(dp[i_][j-1], dp[i][0]-dp[i_][0]))
        #print dp
        return dp[len(nums)][m-1]
Then by binary search, got AC:

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def valid(mid):
            cnt = 0
            current = 0
            for n in nums:
                current += n
                if current>mid:
                    cnt += 1
                    if cnt>=m:
                        return False
                    current = n
            return True

        l = max(nums)
        h = sum(nums)

        while l<h:
            mid = l+(h-l)/2
            if valid(mid):
                h = mid
            else:
                l = mid+1
        return l