class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            if n & 1:
                count+=1
            n = n >> 1
        return count
public int hammingDistance(int x, int y) {
    int xor = x ^ y, count = 0;
    for (int i=0;i<32;i++) count += (xor >> i) & 1;
    return count;
}

def hammingWeight(self, n): 
       return   (bin(n)).count('1')

 class Solution:
# @param n, an integer
# @return an integer
def hammingWeight(self, n):
    return len([i for i in range(32) if (1<<i)&n])  