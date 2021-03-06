# https://leetcode.com/problems/3sum-smaller/#/description
# ven an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# For example, given nums = [-2, 0, 1, 3], and target = 2.

# Return 2. Because there are two triplets which sums are less than 2:

# [-2, 0, 1]
# [-2, 0, 3]
# Follow up:
# Could you solve it in O(n2) runtime?

class Solution(object):
    def threeSumSmallerMyBad(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = 0
        n = len(nums)
        i = 0
        while i < n:
            start = i + 1
            end = n - 1
            
            while start < end:
                if nums[start]+nums[end] >= target - nums[i]:
                    end -= 1
                else: # don't know how to solve two dimisions
                    res += 1
                    end -= 1
After sorting, if i, 
-

def threeSumSmaller(self, nums, target):
    nums.sort()
    count = 0
    for k in range(len(nums)):
        i, j = 0, k - 1
        while i < j:
            if nums[i] + nums[j] + nums[k] < target:
                count += j - i
                i += 1
            else:
                j -= 1
    return count

public class Solution {
    int count;
    
    public int threeSumSmaller(int[] nums, int target) {
        count = 0;
        Arrays.sort(nums);
        int len = nums.length;
    
        for(int i=0; i<len-2; i++) {
            int left = i+1, right = len-1;
            while(left < right) {
                if(nums[i] + nums[left] + nums[right] < target) {
                    count += right-left;
                    left++;
                } else {
                    right--;
                }
            }
        }
        
        return count;
    }

12 months ago reply quote 
No. j (left) & k (right) meet and break the loop. So for each i, we have j's moves + k's moves == n moves. It is O(n2) because left always increments and right always decrements during each i.