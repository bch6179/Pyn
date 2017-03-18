#1 binary search the min x which is close to solve quadratic equation  x(1+x) = 2s  (here say n is s, then binary search running sum problem 
`(x * ( x + 1)) / 2 <= n`, stair number k is just like x the last add on to make the sum close to s but not overflow; not ask you to imagine adding the actual value of steps, then the n is not the sum)
#2 simulate the steps adding process identify the bucket that n is located, return the K 
#  sum=< n < sum+k+1



#Problem description:
# You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

# Given n, find the total number of full staircase rows that can be formed.
#1
# 1 1
# 1 1 1
# 1
class Solution(object):
    def arrangeCoins1(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((1+8*n)**0.5 - 1) / 2
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """   
        #n=0:0 edge
        # 1  sum = 1  1    , 1:1, 2:1,  n/1 >=1, n < 3   k =1
        # 2        3 < n 2    3:2 , 4:2:, 5:2    n /3 > =1 , n < 6 , k=2 
        # 3        6 < n  3   n = 6: 3,  7, 8 , 9:3    n / sum >= 1, n < sum+k+1, k=3
        #          6+4 > n 4
        if n == 0:  #Mistake
            return 0
        k = 0
        sum = 0
        while sum <= n:
            k+=1
            sum+= k
        res = k-1
        return res
    def arrangeCoins2(self, n):
        """
        :type n: int
        :rtype: int
        """   
        if n == 0:  #Mistake
            return 0
        k = 1
        sum = 0
        while True:
            sum+= k
            if n >= sum and n < sum+k+1:
                return k
            k+=1
        #Mistake 
        #sum,count = 0,0
        # while True:
        #     sum += k
        #     count += 1
        #     if (sum >= n):
        #         return count
        #     k+=1
s = Solution() 
print s.arrangeCoins(6)

# public int arrangeCoins(int n) {   
#         //convert int to long to prevent integer overflow
#         long nLong = (long)n;
        
#         long st = 0;
#         long ed = nLong;
        
#         long mid = 0;
        
#         while (st <= ed){
#             mid = st + (ed - st) / 2;
            
#             if (mid * (mid + 1) <= 2 * nLong)
# 
# 
# {
#                 st = mid + 1;
#             }else{
#                 ed = mid - 1;
#             }
#         }
        
#         return (int)(st - 1);
#     }
# You can further reduce the search to half. i.e., Assign ed = (n/2) + 1
    # int arrangeCoins(int n) {
    #     long low = 1, high = n;
    #     while (low < high) {
    #         long mid = low + (high - low + 1) / 2;
    #         if ((mid + 1) * mid / 2.0 <= n) low = mid;
    #         else high = mid - 1;
    #     }
    #     return high;
    # }

    #     int way1(int n) {
    #     int level = 1;
    #     for (long sum = 0; sum <= n; level++) 
    #         sum += level;
    #     return max(level - 2, 0);    
    # }
    he problem is basically asking the maximum length of consecutive number that has the running sum lesser or equal to `n`. In other word, find `x` that satisfy the following condition:

`1 + 2 + 3 + 4 + 5 + 6 + 7 + ... + x <= n`
`sum_{i=1}^x i <= n`
Running sum can be simplified,

`(x * ( x + 1)) / 2 <= n`