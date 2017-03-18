
Longest Increasing Subsequence
state: 错误的方法: f[i]表示前i个数字中最长的LIS的长度 正确的方法: f[i]表示前i个数字中以第i个结尾的LIS的长 度 
function: f[i] = MAX{f[j]+1}, j < i && a[j] <= a [i]) intialize: f[0..n-1] = 1 answer: max(f[0..n-1])
LIS 贪心反例
1 1000 2 3 4 10 11 12 1 2 3 4 13