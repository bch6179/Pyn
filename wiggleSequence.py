https://leetcode.com/problems/wiggle-subsequence/?tab=Description

376. Wiggle Subsequence Add to List
Description  Submission  Solutions
Total Accepted: 18669
Total Submissions: 53732
Difficulty: Medium
Contributors: Admin
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Examples:
Input: [1,7,4,9,2,5]
Output: 6
The entire sequence is a wiggle sequence.

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
  def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # trivial case
        if (len(nums) < 2):
            return len(nums)
        # create array of diffs
        diffs = []
        for i in range(1, len(nums)):
            x = nums[i] - nums[i - 1]
            # ignore diffs of 0 as they don't count as turning points
            if (x != 0):
                diffs.append(x)
        # if there were diffs of only 0, then seq length is 1
        if (not diffs):
            return 1
            
        cnt = 1 # min seq length at this stage
        # now count the number of times the sign of diff between consecutive numbers changes
        # that will be equal to the max wiggle subseq length
        for i in range(1, len(diffs)):
            prod = diffs[i] * diffs[i - 1]
            if (prod < 0):
                cnt += 1
                
        return cnt + 1
Two solutions. One is DP, the other is greedy (8 lines).
DP:

public int wiggleMaxLength(int[] nums) {
		if (nums.length == 0 || nums.length == 1) {
			return nums.length;
		}
		int k = 0;
		while (k < nums.length - 1 && nums[k] == nums[k + 1]) {  //Skips all the same numbers from series beginning eg 5, 5, 5, 1
			k++;
		}
		if (k == nums.length - 1) {
			return 1;
		}
		int result = 2;     // This will track the result of result array
		boolean smallReq = nums[k] < nums[k + 1];       //To check series starting pattern
		for (int i = k + 1; i < nums.length - 1; i++) {
			if (smallReq && nums[i + 1] < nums[i]) {
				nums[result] = nums[i + 1];
				result++;
				smallReq = !smallReq;    //Toggle the requirement from small to big number
			} else {
				if (!smallReq && nums[i + 1] > nums[i]) {
					nums[result] = nums[i + 1];
					result++;
					smallReq = !smallReq;    //Toggle the requirement from big to small number
				}
			}
		}
		return result;
	}

    or every position in the array, there are only three possible statuses for it.

up position, it means nums[i] > nums[i-1]
down position, it means nums[i] < nums[i-1]
equals to position, nums[i] == nums[i-1]
So we can use two arrays up[] and down[] to record the max wiggle sequence length so far at index i.
If nums[i] > nums[i-1], that means it wiggles up. the element before it must be a down position. so up[i] = down[i-1] + 1; down[i] keeps the same with before.
If nums[i] < nums[i-1], that means it wiggles down. the element before it must be a up position. so down[i] = up[i-1] + 1; up[i] keeps the same with before.
If nums[i] == nums[i-1], that means it will not change anything becasue it didn't wiggle at all. so both down[i] and up[i] keep the same.

In fact, we can reduce the space complexity to O(1), but current way is more easy to understanding.

public class Solution {
    public int wiggleMaxLength(int[] nums) {
        
        if( nums.length == 0 ) return 0;
        
        int[] up = new int[nums.length];
        int[] down = new int[nums.length];
        
        up[0] = 1;
        down[0] = 1;
        
        for(int i = 1 ; i < nums.length; i++){
            if( nums[i] > nums[i-1] ){
                up[i] = down[i-1]+1;
                down[i] = down[i-1];
            }else if( nums[i] < nums[i-1]){
                down[i] = up[i-1]+1;
                up[i] = up[i-1];
            }else{
                down[i] = down[i-1];
                up[i] = up[i-1];
            }
        }
        
        return Math.max(down[nums.length-1],up[nums.length-1]);
    }
}



class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int size=nums.size();
        if(size==0) return 0;
        vector<int> f(size, 1);
        vector<int> d(size, 1);
        for(int i=1; i<size; ++i){
            for(int j=0; j<i; ++j){
                if(nums[j]<nums[i]){
                    f[i]=max(f[i], d[j]+1);
                }
                else if(nums[j]>nums[i]){
                    d[i]=max(d[i], f[j]+1);
                }
            }
        }
        return max(d.back(), f.back());
    }
};
Greedy:

class Solution {
public:
    int wiggleMaxLength(vector<int>& nums) {
        int size=nums.size(), f=1, d=1;
        for(int i=1; i<size; ++i){
                 if(nums[i]>nums[i-1]) f=d+1;
            else if(nums[i]<nums[i-1]) d=f+1;
        }
        return min(size, max(f, d));
    }
};


def wiggleMaxLength(self, nums):
    nan = float('nan')
    diffs = [a-b for a, b in zip([nan] + nums, nums + [nan]) if a-b]
    return sum(not d*e >= 0 for d, e in zip(diffs, diffs[1:]))
Explanation / Proof:

Imagine the given array contains [..., 10, 10, 10, 10, ...]. Obviously we can't use more than one of those tens, as that wouldn't be wiggly. So right away we can ignore all consecutive duplicates.

Imagine the given array contains [..., 10, 7, 11, 13, 17, 19, 23, 20, ...]. So increasing from 7 to 23. What can we do with that? Well we can't use more than two of those increasing numbers, as that wouldn't be wiggly. And if we do use two, we'd better use the 7 and the 23, as that offers the best extensibility (for example, the 19 wouldn't allow to next pick the 20 for the wiggly subsequence). And if we do use only one, it still should be either the 7 or the 23, as the 7 is the best wiggle-low and the 23 is the best wiggle-high of them. So whether we actually use the 7 and the 23 or not, we definitely can and should remove the 11, 13, 17, and 19. So then we have [..., 10, 7, 23, 20, ...]. Now, notice that the 7 is a local minimum (both the 10 and the 23 are larger) and the 23 is a local maximum. And if we do this with all increasing or decreasing streaks, i.e., keep only their first and last number, then all the numbers we have left are local extrema, either smaller than both neighbors or larger than both neighbors. Which means that at that point, we're already fully wiggly. And we only removed as many numbers as we have to. So it's a longest possible wiggly subsequence.

My solution first computes differences of neighbors and throws out zeros (which does get rid of those useless consecutive duplicates). And then it just counts the local extrema (by checking two consecutive differences).

I use nan for some convenience, I'll let you figure that part out :-)