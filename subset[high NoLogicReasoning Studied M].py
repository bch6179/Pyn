class Solution(object):
    def helper(self, nums, start, tlist, res):
          #if start >= len(nums)+1: #Mistake append before return
          #return
        res.append(list(tlist))
      
        for i in range(start, len(nums)):
            tlist.append(nums[i]) #Mistake why set start 
            self.helper(nums, i+1, tlist, res)   #Mistake why start+1 
            tlist.pop(-1)
   
    def subsets(self, nums):
        def dfs2(pos, path):
            res.append(list(path))
            for i in range(pos, len(nums)):
                path.append(nums[i])
                dfs2(i+1, path)
                path.pop(-1)
        res = []
        #self.helper(sorted(nums), 0, [], res)
        nums = sorted(nums)
        dfs2(0, [])
        return res
    
s = Solution() 
res = s.subsets([1,2,3])
print res