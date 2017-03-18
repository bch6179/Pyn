def reverse(nums, start, end):
    while start < end:
        temp = nums[end]
        nums[end] = nums[start]
        nums[start] = temp
        start+=1
        end-=1

class Solution(object):
    def rotate(self, nums,k):
        n = len(nums)
        k = k % n ##Mistake  
        if n == 0: return
        reverse(nums, 0, n-k-1)  ##Mistake  
        reverse(nums, n-k, n-1)
        reverse(nums, 0, n-1)

    def rotate2(self, nums, k):
        nums= list(reversed(nums))
        n = len(nums)     
        if len(nums) <= 1 or len(nums) ==k or k==0: return nums
        res = list(reversed(nums[-k:]))
        temp = nums[:n-k]
        res1= list(reversed(temp))
        print(res)
        print(res1)
        return   res1+res
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        #if len(nums) <= 1 or len(nums) ==k or k==0: return nums
        for i in range(k):     
            temp = nums[-1]
            for j in range(len(nums)-2, -1, -1): #Mistake should not -i
                nums[j+1] = nums[j]
            nums[0] = temp
        return nums
s = Solution() 
#print s.rotate([1,2],2) #mistake
input = [1,2,3,4]
s.rotate(input,2)
print input