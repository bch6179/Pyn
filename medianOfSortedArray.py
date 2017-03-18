class Solution(object):
    def median(A, B):
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, int((m + n + 1) / 2)
        while imin <= imax:
            i = int((imin + imax) / 2)
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0


    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findKth(A, B, n // 2 + 1)
        else:
            smaller = self.findKth(A, B, n // 2)
            bigger = self.findKth(A, B, n // 2 + 1)   # instead of n//2
            return (smaller + bigger) / 2.0

    def findKth(self, A, B, k):
        if len(A) == 0:
            return B[k - 1]    # instead of B[0]
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        
        a = A[k // 2 - 1] if len(A) >= k // 2 else None
        b = B[k // 2 - 1] if len(B) >= k // 2 else None
        
        if b is None or (a is not None and a < b):
            return self.findKth(A[k // 2:], B, k - k // 2)
        return self.findKth(A, B[k // 2:], k - k // 2) 

  

s = Solution()
print (s.findMedianSortedArrays2([1,3], [2]))
print (s.findMedianSortedArrays2((1,2,3,4), (5,6,7)))