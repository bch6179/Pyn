class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        def dfs(nums,path):
            if len(nums) == 0:
                res.append(path)
                return 
            
            for i, num in enumerate(nums):
                dfs(nums[:i]+nums[i+1:] , path+[num])
        
        
        
        res = []
        dfs(nums, [])
        return res