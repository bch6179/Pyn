class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        s,e ,g = 0,0, len(nums)-1
        
        while e <= g:#Mistake should include = otherwise miss the last chance
            if nums[e] == 2:
                nums[e], nums[g] = nums[g], nums[e]
                g -= 1
            elif nums[e] == 0:
                nums[e], nums[s] = nums[s], nums[e]
                s += 1
                e += 1
            else:
                e+=1

s = Solution()
l = [1,0] 
s.sortColors(l)
print l