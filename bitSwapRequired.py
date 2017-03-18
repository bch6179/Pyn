果要将整数A转换为B，需要改变多少个bit位？
样例
如把31转换为14，需要改变2个bit位。
(31)10=(11111)2
(14)10=(01110)2
挑战
你能想出几种方法？

Determine the number of bits required to flip if you want to convert integer n to integer m.
Example
Given n = 31 (11111), m = 14 (01110), return 2.
Note
Both n and m are 32-bit integers.

class Solution {
    /**
     *@param a, b: Two integer
     *return: An integer
     */
    public static int bitSwapRequired(int a, int b) {
        int c = a ^ b;
        int count = 0;
        if (c < 0) {
            count++;
            c = Integer.MIN_VALUE ^ c;
        }
        while(c != 0) {
            count += c%2;
            c = c/2;
        }
        return count;
    }
}
 