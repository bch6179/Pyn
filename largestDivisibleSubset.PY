#[URL]https://leetcode.com/problems/largest-divisible-subset/?tab=Description
# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

# nums: [1,2,3]

# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:

# nums: [1,2,4,8]

# Result: [1,2,4,8]
# With this idea, we sort the list. Then, the question turns similar to no.300 longest increasing subsequence. For ith number, its largest divisible subset is the max of subset of any j from 0 - i-1 in which nums[i] % nums[j] == 0.
class Solution(object):
    from copy import copy
    def largestDivisibleSubset(self, nums):
    
        nums.sort()
        n = len(nums)
        if n == 0: return []
        # dp = [0] * n
        # dp[0] = [nums[0]]
        dp = [[c] for i,c in enumerate(nums)]
        #print(dp)
        for i in xrange(1, n):
            curNum = nums[i]
            maxSet = []
            for j in xrange(i):
                if curNum % nums[j] == 0:
                    localSet = dp[j][:]
                    if len(localSet) > len(maxSet):
                        maxSet = localSet
            
            maxSet.append(nums[i])
            dp[i] = maxSet
            #print(dp)
        
        #print(dp)
        res = []
        for localSet in dp:
            if len(localSet) > len(res):
                res = localSet
        return res
    def largestDivisibleSubsetMyss(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0: return []
        dp = [1] * len(nums)
        nums = sorted(nums)
        map = [{c} for i,c in enumerate(nums)]
        # dp[i] = max(dp[j])+1 for j in range(0,i)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    map[i].add(nums[j])
                    dp[i] = dp[j]+1  if dp[j]+1 >= dp[i] else dp[i]
            map[i].add(nums[j])
        maxLen = -(1<<31)
        res = set()
        for i,x in enumerate(dp):
            if x > maxLen:
                maxLen = x
                res = map[i]
        return list(res)
    def largestDivisibleSubset2(self, nums):
        S = {-1: set()}
        for x in sorted(nums):
            S[x] = max((S[d] for d in S if x % d == 0), key=len) | {x}
        return list(max(S.values(), key=len))
s=Solution()
print s.largestDivisibleSubset([4,8,10,240])
    # My S[x] is the largest subset with x as the largest element, i.e., the subset of all divisors of x in the input. With S[-1] = emptyset as useful base case. Since divisibility is transitive, a multiple x of some divisor d is also a multiple of all elements in S[d], so it's not necessary to explicitly test divisibility of x by all elements in S[d]. Testing x % d suffices.

    # While storing entire subsets isn't super efficient, it's also not that bad. To extend a subset, the new element must be divisible by all elements in it, meaning it must be at least twice as large as the largest element in it. So with the 31-bit integers we have here, the largest possible set has size 31 (containing all powers of 2).


#     Classic DP soution similar to LIS, O(n^2)
# Use DP to track max Set and pre index.

# public class Solution {
#     public List<Integer> largestDivisibleSubset(int[] nums) {
#         int n = nums.length;
#         int[] count = new int[n];
#         int[] pre = new int[n];
#         Arrays.sort(nums);
#         int max = 0, index = -1;
#         for (int i = 0; i < n; i++) {
#             count[i] = 1;
#             pre[i] = -1;
#             for (int j = i - 1; j >= 0; j--) {
#                 if (nums[i] % nums[j] == 0) {
#                     if (1 + count[j] > count[i]) {
#                         count[i] = count[j] + 1;
#                         pre[i] = j;
#                     }
#                 }
#             }
#             if (count[i] > max) {
#                 max = count[i];
#                 index = i;
#             }
#         }
#         List<Integer> res = new ArrayList<>();
#         while (index != -1) {
#             res.add(nums[index]);
#             index = pre[index];
#         }
#         return res;
#     }
# }
# My S[x] is the largest subset with x as the largest element, i.e., the subset of all divisors of x in the input. With S[-1] = emptyset as useful base case. Since divisibility is transitive, a multiple x of some divisor d is also a multiple of all elements in S[d], so it's not necessary to explicitly test divisibility of x by all elements in S[d]. Testing x % d suffices.

# While storing entire subsets isn't super efficient, it's also not that bad. To extend a subset, the new element must be divisible by all elements in it, meaning it must be at least twice as large as the largest element in it. So with the 31-bit integers we have here, the largest possible set has size 31 (containing all powers of 2).


# 368. Largest Divisible Subset

# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

# If there are multiple solutions, return any subset is fine.

# Example 1:

# nums: [1,2,3]

# Result: [1,2] (of course, [1,3] will also be ok)
# Example 2:

# nums: [1,2,4,8]

# Result: [1,2,4,8]
# Credits:
# Special thanks to @Stomach_ache for adding this problem and creating all test cases.

# Subscribe to see which companies asked this question


# C++ Solution with Explanations
# The key concept here is:
# Given a set of integers that satisfies the property that each pair of integers inside the set are mutually divisible, for a new integer S, S can be placed into the set as long as it can divide the smallest number of the set or is divisible by the largest number of the set.

# For example, let's say we have a set P = { 4, 8, 16 }, P satisfies the divisible condition. Now consider a new number 2, it can divide the smallest number 4, so it can be placed into the set; similarly, 32 can be divided by 16, the biggest number in P, it can also placed into P.

# Next, let's define:

# EDIT: For clarification, the following definitions try to enlarge candidate solutions by appending a larger element at the end of each potential set, while my implementation below is prefixing a smaller element at the front of a set. Conceptually they are equivalent but by adding smaller elements at the front saves the trouble for keeping the correct increasing order for the final answer. Please refer to comments in code for more details.

# For an increasingly sorted array of integers a[1 .. n]

# T[n] = the length of the largest divisible subset whose largest number is a[n]

# T[n+1] = max{ 1 + T[i] if a[n+1] mod a[i] == 0 else 1 }

# Now, deducting T[n] becomes straight forward with a DP trick. For the final result we will need to maintain a backtrace array for the answer.

# Implementation in C++:

# class Solution {
# public:
#     vector<int> largestDivisibleSubset(vector<int>& nums) {
#         sort(nums.begin(), nums.end());
        
#         vector<int> T(nums.size(), 0);
#         vector<int> parent(nums.size(), 0);
        
#         int m = 0;
#         int mi = 0;
        
#         // for(int i = 0; i < nums.size(); ++i) // if extending by larger elements
#         for(int i = nums.size() - 1; i >= 0; --i) // iterate from end to start since it's easier to track the answer index
#         {
#             // for(int j = i; j >=0; --j) // if extending by larger elements
#             for(int j = i; j < nums.size(); ++j)
#             {
#                 // if(nums[i] % nums[j] == 0 && T[i] < 1 + T[j]) // if extending by larger elements
#                 // check every a[j] that is larger than a[i]
#                 if(nums[j] % nums[i] == 0 && T[i] < 1 + T[j])
#                 {
#                     // if a[j] mod a[i] == 0, it means T[j] can form a larger subset by putting a[i] into T[j]
#                     T[i] = 1 + T[j];
#                     parent[i] = j;
                    
#                     if(T[i] > m)
#                     {
#                         m = T[i];
#                         mi = i;
#                     }
#                 }
#             }
#         }
        
#         vector<int> ret;
        
#         for(int i = 0; i < m; ++i)
#         {
#             ret.push_back(nums[mi]);
#             mi = parent[mi];
#         }

#         // sort(ret.begin(), ret.end()); // if we go by extending larger ends, the largest "answer" element will come first since the candidate element we observe will become larger and larger as i increases in the outermost "for" loop above.
#        // alternatively, we can sort nums in decreasing order obviously. 
        
#         return ret;
#     }
# };

# e TreeMap to memorize. Idea is to iterate previous done ones for the longest. O(n^2)

# public class Solution {
#     public int[] largestDivisibleSubset(int[] nums) {
#         Arrays.sort(nums);
#         Map<Integer, int[]> done = new TreeMap<>(); // num to (len, previous)
#         int max = 0;
#         int maxNum = -1;
#         for (int num: nums) {
#             int len = 1;
#             int prev = -1;
#             for (int d: done.keySet()) {
#                 if (num % d == 0) {
#                     if (len < done.get(d)[0] + 1) {
#                         len = done.get(d)[0] + 1;
#                         prev = d;
#                     }
#                 }
#             }
#             if (len > max) {
#                 max = len;
#                 maxNum = num;
#             }
#             done.put(num, new int[]{len, prev});
#         }
#         int[] ret = new int[max];
#         for (int i=max-1; i>=0; i--) {
#             ret[i] = maxNum;
#             maxNum = done.get(maxNum)[1];
#         }
#         return ret;
#     }
# }

# DFS/backtracking/pruning using DP, 32ms

# 0
# F freeprogrammer 
# Reputation:  1
#  class Solution {
# public:
#     vector<int> _maxSubset;
#     int _n;
#     // idx to start with    maxPrefix[idx] : maximum size of all subsets from [0:idx]
#     void dfs(const vector<int> &nums, int idx, vector<int> &maxPrefix, vector<int> &subset)
#     {
#         // i < idx have been processed
#         if(idx == _n) return;
#         if(_maxSubset.size() - subset.size() > (_n-idx)) return;
#         bool divisible = true;
#         for(const auto &v : subset) {
#             if(nums[idx] % v != 0) {
#                 divisible = false;
#                 break;
#             }
#         }
#         if(divisible && (int(subset.size()) >= (maxPrefix[idx]-1))) {
#             subset.push_back(nums[idx]);
#             maxPrefix[idx] = max(maxPrefix[idx], int(subset.size()));
#             if(subset.size() > _maxSubset.size()) {
#                 _maxSubset = subset;
#             }
#             dfs(nums, idx+1, maxPrefix, subset);
#             subset.pop_back();
#         }
#         if(int(subset.size()) >= (maxPrefix[idx]-1)) {
#             dfs(nums, idx+1, maxPrefix, subset);
#             maxPrefix[idx] = max(maxPrefix[idx], int(subset.size()));
#         }

#     }

#     vector<int> largestDivisibleSubset(vector<int>& nums) {
#         sort(nums.begin(), nums.end());
#         _n = nums.size();
#         vector<int> maxPrefix(nums.size(), 0);
#         vector<int> subset;
#         dfs(nums, 0, maxPrefix, subset);
#         return _maxSubset;
#     }
# };