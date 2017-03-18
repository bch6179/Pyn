#[Note]
#=====
#int mid = (i + j) /2 + 1;	// Make mid biased to the right, so that search right boundary won't get stuck
#if (A[i]!=target) return ret; early return 
 #   else ret[0] = i;  template answer


# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

# Subscribe to see which companies asked this question


# >>> bisect.bisect_left(l, 8)
# 3
# >>> bisect.bisect_right(l, 8) - 1
# 4
#> bisect.bisect(l, 8)
#5

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 0: return [-1,-1]
        start, end = 0, len(nums)-1
        
        while start < end:
            m = start + (end-start)/2
            if nums[m] < target:
                start = m+1 #Mistake if start = m , and start < end, it will get stuck, for [2,2]3
            else:
                end = m#left trending doesn't have right dillemma 
        low = end if nums[end] == target else -1 #Mistake not end-1, [2,2] 3 will return 0
        start, end = 0, len(nums)-1
        #  while start < end:
        #     m = start + (end-start)/2
        #     if nums[m] <= target:
        #         start = m+1
        #     else:
        #         end = m
        # high = end  if nums[end] == target else end-1
        while start +1 < end:
            m = start + (end-start)/2
            if nums[m] <= target:
                start = m  #Right dillemma between stuck, or start= m+1 if start < end, and get high from end-1 or none -1
            else:
                end = m
        if nums[end] == target: #Mistake check end first
            high = end 
        elif nums[start] == target:
            high = start
        else:
            high = -1
        
        return [low, high]


        #    while start +1 < end:
        #     m = start + (end-start)/2
        #     if nums[m] < target:
        #         start = m  
        #     else:
        #         end = m #left trending doesn't have right dillemma 
        # if nums[start] == target: #Mistake check end first
        #     low = start 
        # elif nums[end] == target:
        #     low = end
        # else:
        #     low = -1

        vector<int> searchRange(int A[], int n, int target) {
    int i = 0, j = n - 1;
    vector<int> ret(2, -1);
    // Search for the left one
    while (i < j)
    {
        int mid = (i + j) /2;
        if (A[mid] < target) i = mid + 1;
        else j = mid;
    }
    if (A[i]!=target) return ret;
    else ret[0] = i;
    
    // Search for the right one
    j = n-1;  // We don't have to set i to 0 the second time.
    while (i < j)
    {
        int mid = (i + j) /2 + 1;	// Make mid biased to the right
        if (A[mid] > target) j = mid - 1;  
        else i = mid;				// So that this won't make the search range stuck.
    }
    ret[1] = j;
    return ret; 
}