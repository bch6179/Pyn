class Solution:
    def canJump(self, nums):
        farthest = 0
        for i, num in enumerate(nums):
            farthest = max(farthest, i + num)
            if farthest <= i: break #Mistake return False
        return farthest >= len(nums)-1
s = Solution() 

print s.canJump([1])
print s.canJump([0,1])
print s.canJump([0,0])
print s.canJump([2,0,0,1,3])