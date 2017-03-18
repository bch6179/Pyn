Similar to burstBloon: DP small dim , as last 

Lintcode: Minimum Adjustment Cost 解题报告

Minimum Adjustment Cost

Given an integer array, adjust each integers so that the difference of every adjcent integers are not greater than a given number target.

If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of |A[i]-B[i]|

注意
You can assume each number in the array is a positive integer and not greater than 100

样例
Given [1,4,2,3] and target=1, one of the solutions is [2,3,2,3], the adjustment cost is 2 and it's minimal. Return 2.



原题链接：http://lintcode.com/zh-cn/problem/minimum-adjustment-cost/#

class Solution:
    # @param A: An integer array.
    # @param target: An integer.
    def MinAdjustmentCost(self, A, target):
        # write your code here
        f = [[ sys.maxint for j in xrange(101)] for i in xrange(len(A)+1)]
        for i in xrange(101):
            f[0][i] = 0
        n = len(A)
        for i in xrange(1,n+1):
            for j in xrange(1, 101):
                f[i][j] = sys.maxint:
                for k in xrange(1,101):
                    if abs(j-k) <= target:
                        f[i][j] = min(f[i][j], f[i-1][k] + abs(A[i-1]-j))
        ans = f[n][100]
        for i in xrange(101):
            if f[n][i] < ans:
                ans = f[n][i]       

        return ans

Note
You can assume each number in the array is a positive integer and not greater than 100
注意是positive number 所以j的起始值是1不是0 因为这个犯了好几次错....
state: dp[i][v] 表示前i个数, 第i个数调整为v 满足条件, 所需要的最小代价
function:如果i个数时j 那么第i-1个数k是要满足 Math.abs(j - k) < target的
dp[i][v] = Math.min(dp[i-1][k] +  Math.abs(j -A.get(i-1))) //第i个数时j 第i-1个数为k时候使代价最小

如果第i个数是j, 那么第i-1个数k只能在[lowerRange, UpperRange]之间，lowerRange=Math.max(0, j-target), upperRange=Math.min(99, j+target), 这样的话，transfer function可以写成： for (int p=lowerRange; p<= upperRange; p++) { 　　res[i][j] = Math.min(res[i][j], res[i-1][k] + Math.abs(j-A.get(i-1))); }
initial:dp[0][j]= 0
return: 满足条件的最小代价 Math.min(dp[m][j]) // 改变j的值找到最小的代价

public class Solution {

    public int MinAdjustmentCost(ArrayList A, int target) {
        int m = A.size();
        int[][] dp = new int[m+1][101];
        for (int j = 0; j < 101; j++) {
            dp[0][j] = 0;
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= 100; j++) {
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = 1; k <= 100; k++) {
                    if (Math.abs(j - k) > target) {
                        continue;
                    }
                 
                    dp[i][j] = Math.min(dp[i][j], dp[i-1][k] +  Math.abs(j -A.get(i-1)));
//Math.abs(j -A.get(i-1)))表示第i个数改为j所需代价
                }
            }
        }
        int result = Integer.MAX_VALUE;
        for (int j = 1 ; j <= 100; j++) {
            result = Math.min(result, dp[m][j]);
        }
        return result;
    }
}


SOL 1:

主页君现在最喜欢这种题目了。好兴奋啊！

好啦，我们先上第一个版本，递归版本：

当前可取的值是1-100，并且与上一个值是在target的差值以内。

这个版本肯定是超时啦。因为我们有大量的重复的计算，每一次从头至尾计算时，从某个index开始的某个取值的计算会反复进行。


复制代码
 1 /**
 2      * @param A: An integer array.
 3      * @param target: An integer.
 4      */
 5     public static int MinAdjustmentCost1(ArrayList<Integer> A, int target) {
 6         // write your code here
 7         if (A == null) {
 8             return 0;
 9         }
10
11         return rec(A, new ArrayList<Integer>(A), target, 0);
12     }
13
14     /*
15      * SOL 1:
16      * 最普通的递归方法。
17      * */
18     public static int rec(ArrayList<Integer> A, ArrayList<Integer> B, int target, int index) {
19         int len = A.size();
20         if (index >= len) {
21             // The index is out of range.
22             return 0;
23         }
24
25         int dif = 0;
26
27         int min = Integer.MAX_VALUE;
28
29         // If this is the first element, it can be from 1 to 100;
30         for (int i = 0; i <= 100; i++) {
31             if (index != 0 && Math.abs(i - B.get(index - 1)) > target) {
32                 continue;
33             }
34
35             B.set(index, i);
36             dif = Math.abs(i - A.get(index));
37             dif += rec(A, B, target, index + 1);
38             min = Math.min(min, dif);
39
40             // 回溯
41             B.set(index, A.get(index));
42         }
43
44         return min;
45     }
复制代码


SOL 2:

我们还是跟以前一样，加一个memory，减少重复计算。

轻松AC. M[i][j]的定义是：从index = i处开始往后所有的differ，并且A[i]的取值取为j + 1;


复制代码
 1 /*
 2      * 递归2：
 3      * Rec + memory.
 4      * */
 5     /**
 6      * @param A: An integer array.
 7      * @param target: An integer.
 8      */
 9     public static int MinAdjustmentCost2(ArrayList<Integer> A, int target) {
10         // write your code here
11         if (A == null || A.size() == 0) {
12             return 0;
13         }
14
15         int[][] M = new int[A.size()][100];
16         for (int i = 0; i < A.size(); i++) {
17             for (int j = 0; j < 100; j++) {
18                 M[i][j] = Integer.MAX_VALUE;
19             }
20         }
21
22         return rec2(A, new ArrayList<Integer>(A), target, 0, M);
23     }
24
25     public static int rec2(ArrayList<Integer> A, ArrayList<Integer> B, int target, int index,
26            int[][] M) {
27         int len = A.size();
28         if (index >= len) {
29             // The index is out of range.
30             return 0;
31         }
32
33         int dif = 0;
34         int min = Integer.MAX_VALUE;
35
36         // If this is the first element, it can be from 1 to 100;
37         for (int i = 1; i <= 100; i++) {
38             if (index != 0 && Math.abs(i - B.get(index - 1)) > target) {
39                 continue;
40             }
41
42             if (M[index][i - 1] != Integer.MAX_VALUE) {
43                 dif = M[index][i - 1];
44                 min = Math.min(min, dif);
45                 continue;
46             }
47
48             B.set(index, i);
49             dif = Math.abs(i - A.get(index));
50             dif += rec2(A, B, target, index + 1, M);
51
52             min = Math.min(min, dif);
53
54             // Record the result.
55             M[index][i - 1] = dif;
56
57             // 回溯
58             B.set(index, A.get(index));
59         }
60
61         return min;
62     }
复制代码


SOL 3:修改了一下，递归增加一个参数 ： int x，表示在index 处A[i]取值为x，返回值的意义是，当此值取x时，从index往后，所有的diff之和。

这样的话，递归会看起来更加简洁一点儿。我们不需要记录上一个A[i]的取值。




复制代码
 1 /*
 2      * SOLUTION 3 递归2：
 3      * Rec + memory.
 4      * 改进的递归版本
 5      * */
 6     /**
 7      * @param A: An integer array.
 8      * @param target: An integer.
 9      */
10     public static int MinAdjustmentCost3(ArrayList<Integer> A, int target) {
11         // write your code here
12         if (A == null || A.size() == 0) {
13             return 0;
14         }
15
16         int[][] M = new int[A.size()][100];
17         for (int i = 0; i < A.size(); i++) {
18             for (int j = 0; j < 100; j++) {
19                 M[i][j] = Integer.MAX_VALUE;
20             }
21         }
22
23         // 首个数字可以取1-100
24         int min = Integer.MAX_VALUE;
25         for (int i = 1; i <= 100; i++) {
26             min = Math.min(min, rec3(A, target, 0, i, M));
27         }
28
29         return min;
30     }
31
32     /*
33      * 将当前值设置为x能求得的最小解
34      * */
35     public static int rec3(ArrayList<Integer> A, int target, int index, int x,
36            int[][] M) {
37         int len = A.size();
38         if (index >= len) {
39             // The index is out of range.
40             return 0;
41         }
42
43         if (M[index][x - 1] != Integer.MAX_VALUE) {
44             return M[index][x - 1];
45         }
46
47         int bas = Math.abs(x - A.get(index));
48         int min = Integer.MAX_VALUE;
49
50         // 对下一个值尝试取1-100
51         for (int i = 1; i <= 100; i++) {
52             // 下一个值的取值不可以超过abs
53             if (index != len - 1 && Math.abs(i - x) > target) {
54                 continue;
55             }
56
57             // 计算dif
58             int dif = bas + rec3(A, target, index + 1, i, M);
59             min = Math.min(min, dif);
60         }
61
62         // Record the result.
63         M[index][x - 1] = min;
64         return min;
65     }
复制代码


SOL 4:

LALA,主页君终于来打BOSS了。有了前面的递归的铺垫，把它转化为一个二维DP也就是水到渠成了。

D[i][v]: 把index = i的值修改为v，所需要的最小花费

我们引用一下九章算法黄老师课上的课件:

其实很简单，就是当前index为v时，我们把上一个index从1-100全部过一次，取其中的最小值
（判断一下前一个跟当前的是不是abs <= target）




 


GITHUB:

https://github.com/yuzhangcmu/LeetCode_algorithm/blob/master/algorithm/dp/MinAdjustmentCost_Class.java

分类: Lintcode
标签: 算法, 编程, Lintcode
好文要顶 关注我 收藏该文
Yu's Garden
关注 - 1
粉丝 - 61
+加关注
2 0
(请您对文章做出评价)
« 上一篇：LeetCode: Merge Two Sorted Lists 解题报告
» 下一篇：LeetCode: Insertion Sort List 解题报告
posted on 2014-12-09 18:47 Yu's Garden 阅读(2280) 评论(5) 编辑 收藏
评论

#1楼 2014-12-17 11:33 eryueniaobp
很清晰～
支持(2)反对(0)

#2楼[楼主] 2014-12-17 18:15 Yu's Garden
@eryueniaobp
谢谢夸奖！
支持(0)反对(0)

#3楼 2015-03-17 21:05 唐小喵
主页君，你喜欢这种题，我可讨厌死了！
支持(0)反对(0)

#4楼[楼主] 2015-03-17 21:07 Yu's Garden
@北京小王子
为什么呀。
支持(0)反对(0)

#5楼 2015-06-04 08:26 UmassJin
谢谢主页君的详细解答，对于recursion的解法不是很理解，对于每个A[i]，我们都要从1到100一次尝试？假设input是[5,8,2,3], target = 2, 思路是不是从A[0] 的1 到100 一次尝试过去，记录下每一个diff，然后再A[1] 1到100 一次尝试过去，记录下diff？
