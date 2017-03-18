 
 The basic idea is to iteratively update the array from the end to the beginning.
 It's O(k) space complexity, not time complexity. The space used is just the k+1 array elements, hence O(k)

  O(n) time solution: so C(n, m) = C(n, m-1) * (n-m+1) / m , Mirror the second half