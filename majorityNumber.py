from collections import *
#[Note]
#=====
#1
# more than half, index is 0,[n/2](i.e n/2+1,no matter e/o ); 
    #   if even 4, 4/2+1=3 > 2; if odd 5, 5/2+1 =3 > 2
#2 after sorting, no more than n/2 both side
class Solution(object):
    
    def findMajority(self, nums):
        #nums=sorted(nums)
        count = defaultdict(int)
        n = len(nums)
        for num in nums:
            count[num]+=1
            if count[num] >= n/2+1:
                return num
        return -1  
    def findMajority3(self, nums):
        count = 0
        x = None
        for num in nums:
            if count == 0 or x == num:
                x = num; count+=1
            else: count-=1
        return x  #mistake
    def findMajority2(self, nums):
        count = 0
        x = -1
        for num in nums:
            if count == 0 or num == x:
                x = num
                count += 1
            else:
                count -= 1
                if count == 0: x = -1  # @Mistake not run test
        if count >= 1: return x

    def partition(self, nums, l,r):
        # 2 3 2 6 2 5 4 # 542
        #p = 4
        #
         #l  unsorted h
        pivot = nums[r]
        n = r
        r-=1
        while l < r:
            while l < r and nums[l] <= pivot:
                l+=1
            while l < r and nums[r] >= pivot:
                r-=1
            temp = nums[r]
            nums[r] = nums[l]
            nums[l] = temp  
        nums[n] = nums[l] 
        nums[l] = pivot
        return l
    def quickSort(self, nums, l, r):
        if l < r:
            i = self.partition(nums, l,r)
            self.quickSort(nums, l, i-1)
            self.quickSort(nums, i+1, r)

    def findMajority2(self, nums):
        self.quickSort(nums, 0 , len(nums)-1)
        return nums[len(nums)/2]
 
s=Solution()
print( s.findMajority3([]))
print( s.findMajority3([2,2,3,2]))
print  s.findMajority3([3,3,3,2,4])