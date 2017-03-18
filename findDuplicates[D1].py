# Find All Duplicates in an Array

#Methond 1 :is circle , when you finished the swapping but found same elem in two different cells, then it's duplicated
# space not including the input and output variables

# The idea is we do a linear pass using the input array itself as a hash to store which numbers have been seen before. We do this by making elements at certain indexes negative. See the full explanation here

class Solution(object):
    def findDuplicates(self, nums):
        res = []
        for x in nums:
            if nums[abs(x)-1] > 0: #Mistake has to be abs(x), otherwise out of range [2,2], second 2 already -2
                nums[abs(x)-1] = -1*nums[abs(x)-1]  # use x for abs(nums[i]
            else:
                res.append(abs(x))#Mistake no need to abs recover
        return res
    def findDuplicates3(self, nums):
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = -1*abs(nums[abs(nums[i])-1])  # use x for abs(nums[i]
            else:
                res.append(abs(nums[i]))#Mistake no need to abs recover
        return res
    def findDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set()
        for i in range(len(nums)):
            while nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1] #Mistake nums[i] need to be the second change
                # bad one : nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
                # temp = nums[nums[i]-1]
                # nums[nums[i]-1] = nums[i]
                # nums[i] = temp
            if i != nums[i]-1:
                res.add(nums[i]) #Mistake returned i
        return list(res) ##Mistake NEED set , otherwise the first one in index 0 and second are duplicated

#         After nums[i] = nums[nums[i]-1], nums[i]-1 is no longer the same value. So you are setting nums[i] to the wrong index. You may want to back up nums[i]-1:

# c = nums[i] - 1
# nums[i], nums[c] = nums[c], nums[i]
# That's correct. Since A[p] has changed, A[p]+q is no longer the A[p]+q as before.
s = Solution() 
print s.findDuplicates([2,2])