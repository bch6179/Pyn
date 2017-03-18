class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2: return 0
        begin = 0 #Mistake should not 1,n-2, otherwise 3,2,1, return 1
        end = n-1
        
        while begin+1 < end:
            m = begin + (end-begin)/2
            if nums[m] > nums[m+1]:
                if nums[m] > nums[m-1]:
                    return m
                else: 
                    end = m
            else:
                begin = m
        if nums[begin] > nums[end]:
            return begin
        else:
            return end

#             onsider that each local maximum is one valid peak.
# My solution is to find one local maximum with binary search.
# Binary search satisfies the O(logn) computational complexity.

# Binary Search: recursion

# class Solution {
# public:

# int findPeakElement(const vector<int> &num) {
#     return Helper(num, 0, num.size()-1);
# }
# int Helper(const vector<int> &num, int low, int high)
# {
#     if(low == high)
#         return low;
#     else
#     {
#         int mid1 = (low+high)/2;
#         int mid2 = mid1+1;
#         if(num[mid1] > num[mid2])
#             return Helper(num, low, mid1);
#         else
#             return Helper(num, mid2, high);
#     }
# }
# };
# Binary Search: iteration

# class Solution {
# public:
#     int findPeakElement(const vector<int> &num) 
#     {
#         int low = 0;
#         int high = num.size()-1;
        
#         while(low < high)
#         {
#             int mid1 = (low+high)/2;
#             int mid2 = mid1+1;
#             if(num[mid1] < num[mid2])
#                 low = mid2;
#             else
#                 high = mid1;
#         }
#         return low;
#     }
# };
# Sequential Search:

# class Solution {
# public:
#     int findPeakElement(const vector<int> &num) {
#         for(int i = 1; i < num.size(); i ++)
#         {
#             if(num[i] < num[i-1])
#             {// <
#                 return i-1;
#             }
#         }
#         return num.size()-1;
#     }
# };