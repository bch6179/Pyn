# {
#     "tags": [DFS, D&D],
#     "code": ['
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nonPrime = [False]*n
        count = 0
        for i in range(2, n):
            if not nonPrime[i]:
                count+=1
                j = 2
                while i*j < n:
                    nonPrime[i*j] = True
                    j+=1
        return count
        # def isPrime(n)_timeout:
        #     if n <= 1: return False  
        #     k = 2
        #     while k*k <= n:
        #         if n % k == 0:
        #             return False
        #         k+=1
        #     return True
            
          
        # count = 0
        # for i in range(2,n):
        #     if isPrime(i):
        #         count+=1
        # return count
class Solution:
    # @param {integer} n
# @return {integer}
def countPrimes(self, n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)        
e Sieve of Eratosthenes uses an extra O(n) memory and its runtime complexity is O(n log log n). For the more mathematically inclined readers, you can read more about its algorithm complexity on Wikipedia.

public int countPrimes(int n) {
   boolean[] isPrime = new boolean[n];
   for (int i = 2; i < n; i++) {
      isPrime[i] = true;
   }
   // Loop's ending condition is i * i < n instead of i < sqrt(n)
   // to avoid repeatedly calling an expensive function sqrt().
   for (int i = 2; i * i < n; i++) {
      if (!isPrime[i]) continue;
      for (int j = i * i; j < n; j += i) {
         isPrime[j] = false;
      }
   }
   int count = 0;
   for (int i = 2; i < n; i++) {
      if (isPrime[i]) count++;
   }
   return count;
}


# ']
# }