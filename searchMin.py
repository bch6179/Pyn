# search min in rotated:   1, 1, 1, -1, 1, 1, 1, 1

class Solution(object):
    def findMin(self, nums):
    beg = 0
    end = len(nums)-1
    while beg <= end: #have to have beg = mid+1
        while beg < end and nums[beg] == nums[beg + 1]:
            beg += 1
        while end > beg and nums[end] == nums[end - 1]:
            +
            end -= 1
        if beg == end:
            return nums[beg]
        
        mid = (beg+end)/2
        if nums[mid] > nums[end]:
            beg = mid + 1
        else:
            end = mid
        
            
    return nums[beg]
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        b, e = 0, len(nums)-1
        
        while b  < e: # e-=1 since we have this, then we could b < e
        #but [3,1], b not change, so this go to infinite,unless we let b = m+1 , as you know lower is later for case 1
            m = b + (e-b)/2
            if nums[m] > nums[e]:
                b = m +1
            elif nums[m] < nums[e]:
                e = m
            else:
                e-=1  #remove duplicate
            
        return nums[b]  
 
    def findMini(self, nums):
 
        b, e = 0, len(nums)-1
        
        while b+1 < e:
            m = b + (e-b)/2
            flag = False
            while b < e and nums[m] == nums[e]:
                e -= 1
                flag = True #Mistake must
            if flag: 
                #e+=1  # 1 1 1 infinite
                continue
            if nums[m] > nums[e]:
                b = m 
            elif nums[m] < nums[e]:
                e = m
            
            # bad to set    e -= 1 in else , will miss the last
        return nums[b] if nums[b] < nums[e] else nums[e]
    def findMinI(self, nums): #bad
        """
        :type nums: List[int]
        :rtype: int
        """
        
        b, e = 0, len(nums)-1
        
        while b+1 < e:
            m = b + (e-b)/2
            flag = False
            while b < e and nums[m] == nums[e]: #this might not work, since we didn't verify nums[e] or m is the minimum, we miss that by skipping; not like search target, which is verified not then skip
                e -= 1
                flag = True #Mistake must
            if flag: 
                #e+=1  # 1 1 1 infinite
                continue
            if nums[m] > nums[e]:
                b = m 
            elif nums[m] < nums[e]:
                e = m
            
            # bad to set    e -= 1 in else , will miss the last
        return nums[b] if nums[b] < nums[e] else nums[e]
s = Solution() 
print s.findMin([3,1])
print s.findMin([2,2,0,0,0])
print s.findMin([0,1,2,2,2,2])
print s.findMin([3 ,1,3,3,3]) 
print s.findMin([3,3,1,3])  # Am == Ae, adjust sb , otherwise miss ---~- or -~-----, Am = As, adjust e, so undecision

/**  * Suppose a sorted array is rotated at some pivot unknown to you
beforehand.  *  * (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).  *
* You are given a target value to search. If found in the array return
its  * index, otherwise return -1.  *  * You may assume no duplicate
exists in the array.  * * Tags: Array, Binary Search  */ class
SearchRotatedSortedArr {     public static void main(String[] args) {

    }

    /**
     * Binary Search.
     * Check which half is sorted.
     * If target is within that half, search in that half.
     * If not, search in the other half.
     */

    //RM: quick switch, even you have solved similar; favor smaller variants like
    // A[m] A[l] and then target and A[l]; although you checked A[r] for findMin, b
    //ut here leave open;
    // solve the reachable, leave CPU handle the uncertainty; the key is to reduce unknown area by identifying determinate area;leave the undecision aresa in the unknown
    //leave the edge case to consider at last , nonrotated, and see if the target < Am, target > Al cover it
    //Am > Al not decide the scenario; 
    

#      public int findMin(int[] A) {
#         // write your code here
#         int l = 0;
#         int r = A.length - 1;
#         while(l + 1 < r) {
#             if (A[l] == A[l+1]) {
#                 l++;
#                 continue;
#             }
#             if (A[r] == A[r-1]) {
#                 r--;
#                 continue;
#             }

#             int m = l + (r-l)/2;
#             if (A[m] > A[r]) {
#                 l = m;
#             }
#             else r = m;
#         }

#         return (A[l] > A[r]?A[r]:A[l]);
#     }
# }