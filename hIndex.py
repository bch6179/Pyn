https://leetcode.com/problems/h-index/?tab=Description

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.


Really smart method!!! Here is my interpretation of the method and hope it helps those in need:

We first create a new vector counts of size L+1 where L is the length of the citations vector. The counts vector stores the number of papers having a citation equal to its index for i=0 to L-1. For i=L, it stores the number of papers having a citation equal to or greater than L. A simple fact is that the h-index can be at most L, this happens when all of his papers have citations no less than L. Therefore, for the purpose of computing h-index, if a person has L papers, it would end up with the same h-index no matter one of his paper has a citation of 10L or L.

After finalizing the counts vector, we can then easily locate his h-index by scanning from right (L) to left (0). By definition, index k is his h-index if the summation of all elements from counts[k] to counts[L] is no less than k.

The following is simply a copy of the original code with some new naming corresponding to the above interpretation:

public int hIndex(int[] citations) {
	int L = citations.length;
	if(L<1) return 0;
	int[] counts = new int[L+1];
	for(int i : citations) {
		if(i>L) counts[L]++;
		else counts[i]++;
	}
	int res = 0;
	for(int k=L; k>=0; k--) {
	    res += counts[k];
	    if(res>=k) return k;
	}
	return 0;
}

he idea behind it is some bucket sort mechanisms. First, you may ask why bucket sort. Well, the h-index is defined as the number of papers with reference greater than the number. So assume n is the total number of papers, if we have n+1 buckets, number from 0 to n, then for any paper with reference corresponding to the index of the bucket, we increment the count for that bucket. The only exception is that for any paper with larger number of reference than n, we put in the n-th bucket.

Then we iterate from the back to the front of the buckets, whenever the total count exceeds the index of the bucket, meaning that we have the index number of papers that have reference greater than or equal to the index. Which will be our h-index result. The reason to scan from the end of the array is that we are looking for the greatest h-index. For example, given array [3,0,6,5,1], we have 6 buckets to contain how many papers have the corresponding index. Hope to image and explanation help.

I give you 99 points, one less point means that you might get proud of 100 points.lass Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        buckets = [0 for _ in range(n + 1)]
        
        for num in citations:
            if num >= n:
                buckets[n] += 1
            else:
                buckets[num] += 1
                
        count = 0
        
        for i in reversed(range(len(buckets))):
            count += buckets[i]
            
            if count >= i:
                return i
                
        return 0
        
def hIndex(self, citations):
    citations.sort()
    n = len(citations)
    for i in xrange(n):
        if citations[i] >= (n-i):
            return n-i
    return 0
O(n) space, O(n) time

def hIndex(self, citations):
    n = len(citations)
    citeCount = [0] * (n+1)
    for c in citations:
        if c >= n:
            citeCount[n] += 1
        else:
            citeCount[c] += 1
    
    i = n-1
    while i >= 0:
        citeCount[i] += citeCount[i+1]
        if citeCount[i+1] >= i+1:
            return i+1
        i -= 1
    return 0