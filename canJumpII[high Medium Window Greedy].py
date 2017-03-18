
class Solution(object):
    def jump1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0: return -1
        maxInt = 1<<31 -1
        dp = [maxInt for i in range(len(nums))]
        dp[0] = 0
        for i in range(1,len(nums)):
            for j in range(i):
                if dp[j] != maxInt and j+nums[j] >= i: # Optimize
                    dp[i] = min(dp[i], dp[j]+1)
                    #  steps[i] = steps[j] + 1; front value is smaller
                    # break;  # Optimize
        return dp[-1]
    def jump2(self, nums):
        if nums == None or len(nums) == 0: return -1
        curEdge, nextEdge, minStep = 0,nums[0],0
   
        for i in range(0, len(nums)):
                if i > curEdge:
                    minStep += 1
                    curEdge = nextEdge           
                nextEdge = max(nextEdge, nums[i] + i)
                if nextEdge <= i or nextEdge >= len(nums): break
        return minStep
s = Solution() 
print s.jump2([0,2,3])
print s.jump2([2,0,1,1])


    #       public int jump(int[] A) {
    #     if (A == null || A.length == 0) {
    #         return -1;
    #     }
    #     int start = 0, end = 0, jumps = 0;
    #     while (end < A.length - 1) {
    #         jumps++;  #need one more jump, before out of border
    #         int farthest = end;
    #         for (int i = start; i <= end; i++) {
    #             if (A[i] + i > farthest) {
    #                 farthest = A[i] + i;
    #             }
    #         }
    #         start = end + 1;
    #         end = farthest;
    #     }
    #     return jumps;
    # }
                    