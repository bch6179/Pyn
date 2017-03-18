class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0: break
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1
                else:
                    res.append([nums[i],nums[j], nums[k]])
                    j+=1  #Mistake j wrongly write to i
                    k-=1                                     # j  k this will skip
                while ( j < k and i != j-1 and nums[j] == nums[j-1]): j+=1 # 1 1  , so not j+1, but j-1
               #                                      i   j      k this will skip one solution  
                #[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]  -2 -2 . 3 6
                while ( j < k and k < len(nums)-1 and nums[k] == nums[k+1]): k-=1
        return res
s = Solution() 
#print s.threeSum([0,-4,-1,-4,-2,-3,2])
#print s.threeSum([-2,0,1,1,2])
s.threeSum([-1,0,1,2,-1,-4])