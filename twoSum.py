class Solution(object):
    def twoSum(self, nums, target):
        nums.sort()
        start, end = 0, len(nums)-1
        while start < end:
            sum = nums[start] + nums[end] 
            if sum == target:
                return [start, end]
            elif sum < target:
                start = start + 1
            else:
                end= end -1              
        return [-1,-1]


    def twoSum_hashmap(self, nums, target):

        #pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
        #pairs.sort(key=lambda pair: pair[1])  #sort based on the value of the pair
        hash = {}
        #循环nums数值，并添加映射
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
        #无解的情况
        return [-1, -1]
       
    
s = Solution()
print(s.twoSum([14,1,2,4],15))

#print(s.twoSum_hashmap([14,1,2,4],15))