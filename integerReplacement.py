https://leetcode.com/problems/integer-replacement/?tab=Description


If n is even, halve it.
If n=3 or n-1 has less 1's than n+1, decrement n.
Otherwise, increment n.
Here is an example of such a solution in Java:

public int integerReplacement(int n) {
    int c = 0;
    while (n != 1) {
        if ((n & 1) == 0) {
            n >>>= 1;
        } else if (n == 3 || Integer.bitCount(n + 1) > Integer.bitCount(n - 1)) {
            --n;
        } else {
            ++n;
        }
        ++c;
    }
    return c;
}
Of course, doing bitCount on every iteration is not the best way. It is enough to examine the last two digits to figure out whether incrementing or decrementing will give more 1's. Indeed, if a number ends with 01, then certainly decrementing is the way to go. Otherwise, if it ends with 11, then certainly incrementing is at least as good as decrementing (*011 -> *010 / *100) or even better (if there are three or more 1's). This leads to the following solution:


lass Solution(object):
    def integerReplacement(self, n, counter=0):
    	if n == 1: return counter
    	if not n%2: return self.integerReplacement(n/2, counter+1)
    	else: return min(self.integerReplacement(n+1, counter+1), self.integerReplacement(n-1, counter+1))
EDIT:

ncise code! One slight improvement -- you actually do not need to add a variable counter. Moreover, memoization could save a lot of runtime: 300ms --> 30ms. Please see here: https://discuss.leetcode.com/topic/58402/python-top-down-approach-memoization-saves-hundreds-of-ms-345ms-36ms

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        if n % 2:
            return 1 + min(self.integerReplacement(n+1), self.integerReplacement(n-1))
        else:
            return 1 + self.integerReplacement(n/2)

 class Solution(object):
        def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {1:0}
        return self.recRep(n, memo)
        
    def recRep(self, n, memo):
        if n in memo:
            return memo[n]
        if n % 2:
            memo[n] = 1 + min(self.recRep(n+1, memo), self.recRep(n-1, memo))
            return memo[n]
        else:
            memo[n] = 1 + self.recRep(n/2, memo)
            return memo[n]
            
                       
Denote f(n) the minimum number of jumps from n to 1.
By definition, we have the recurrence
f(1) = 0, f(2n) = 1 + f(n), f(2n + 1) = min(f(2n) + 1, f(2n + 2) + 1).
First notice that this sequence is well defined because f(2n + 2) = f(n + 1) + 1, so f(2n + 1) = min(f(2n) + 1, f(n + 1) + 2). Every element is defined by some element before it.
We want to show (*):
If n % 4 = 3 and n != 3, then f(n) = f(n + 1) + 1.
If n % 4 = 1 or n = 3, then f(n) = f(n - 1) + 1.
This gives us an O(log n) time, O(1) space solution.

class Solution(object):
    def integerReplacement(self, n):
        rtn = 0
        while n > 1:
            rtn += 1
            if n % 2 == 0:
                n //= 2
            elif n % 4 == 1 or n == 3:
                n -= 1
            else:
                n += 1
        return rtn