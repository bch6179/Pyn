# I see the majority of those posts use hashset to record values. Actually, we can simply adapt the Floyd Cycle detection algorithm. I believe that many people have seen this in the Linked List Cycle detection problem. The following is my code:
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sum = 0
        v = set()
        while True:
            while n:
                m = n%10
                sum += m*m
                n/=10
            #if sum == orig: return False #Mistkae need a set
            if sum == 1:
                return True
            if sum not in v:
                v.add(sum)
            else: 
                return False
            n = sum
            sum = 0
            
        return sum == 1
int digitSquareSum(int n) {
    int sum = 0, tmp;
    while (n) {
        tmp = n % 10;
        sum += tmp * tmp;
        n /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    int slow, fast;
    slow = fast = n;
    do {
        slow = digitSquareSum(slow);
        fast = digitSquareSum(fast);
        fast = digitSquareSum(fast);
    } while(slow != fast);
    if (slow == 1) return 1;
    else return 0;
}

My bad got to run endlessly
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        orig = n
        sum = n
        while sum and sum != 1 :
            n = sum
            sum = 0
            while n:
                m = n%10
                sum += m*m
                n/=10
            if sum == orig: return False
        return sum == 1