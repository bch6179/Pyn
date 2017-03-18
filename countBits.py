# Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

# Example:
# For num = 5 you should return [0,1,1,2,1,2].

# Follow up:

# It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
# Show Hint 


class Solution(object):
    def countBits1(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        
        for i in range(num+1):
            count = 0
            while i > 0:
                if i & 1:
                    count += 1
                i = i >> 1
            res.append(count)
        return res
        
    def countBits(self, num):
        DP = [0] * (num+1)
        
        for i in range(1, num+1):
            if (i-1) & 1 == 0:
                DP[i] = DP[i-1] + 1
            else:
                DP[i] = DP[i>>1]
        
        return DP


#         An easy recurrence for this problem is f[i] = f[i / 2] + i % 2.

# public int[] countBits(int num) {
#     int[] f = new int[num + 1];
#     for (int i=1; i<=num; i++) f[i] = f[i >> 1] + (i & 1);
#     return f;
# }