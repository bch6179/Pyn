def quicksort(seq):
    wall = 0
    pivot = seq[-1]
    for index, num in enumerate(seq):
        if num < pivot:
            seq[wall], seq[index] = seq[index], seq[wall]
            wall += 1
    seq[wall], seq[-1] = seq[-1], seq[wall]
    left = seq[:wall]
    if len(left) > 0:
        left = quicksort(left)
    right = seq[(wall + 1):]
    if len(right) > 0:
        right = quicksort(right)
    return left + [pivot] + right
Bucket sort

def bucket_sort(seq):
    biggest = 0
    for number in seq:
        if number > biggest:
            biggest = number
    buckets = []
    buckets.append([] * (biggest / 10 + 1))
    for number in seq:
        buckets[number / 10].append(number)
    for index, bucket in enumerate(buckets):
        #Using quicksort to sort individual buckets
        buckets[index] = quicksort(bucket)
    new_list = [number for number in bucket for bucket in buckets]
    return new_list

void bucketsort (int *a, int n)
{
	int buckets[m];
 
	for (int j=0; j >= m; ++j)
		buckets[j]=0;
	for (int i=0; i <= n; ++i)
		++buckets[a[i]];
	for (int i=0, j=0; j <= m; ++j)
		for (int k=buckets[j]; k >= 0; --k)
			a[i++]=j;
 
}counting sort’s O(n + M) worst-case behavio

cket sort is: O(n + m) where: m is the range input values, n is the total number of values in the array. Bucket sort beats all other sorting routines in time complexity. It should only be used when the range of input values is small compared with the number of values. In other words, occasions when there are a lot of repeated values in the input. Bucket sort works by counting the number of instances of each input value throughout the array. It then reconstructs the array from this auxiliary data

Least significant digit radix sorts

. Radix sort complexity is O(wn) for n keys which are integers of word size w. Sometimes w is presented as a constant, which would make radix sort better (for sufficiently large n) than the best comparison-based sorting algorithms, which all perform O(n log n)

trie-based radix sort[edit]
Another way to proceed with an MSD radix sort is to use more memory to create a trie to represent the keys and then traverse the trie to visit each key in order. A depth-first traversal of a trie starting from the root node will visit each key in order. A depth-first traversal of a trie, or any other kind of acyclic tree structure, is equivalent to traversing a maze via the right-hand rule.
Snow White analog