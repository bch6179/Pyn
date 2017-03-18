class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        
        res = []
        msum = 0
        i = 0
        mingp = (1 << 31) - 1
        while i < len(nums) - 2:
            start = i + 1
            end = len(nums) - 1
            cont = True
            while start < end and cont:
                sum = nums[i] + nums[start] + nums[end]
                if sum <  target:
                    start += 1
                elif sum > target:
                    end -= 1
                else:
                    cont = False  #Mistake if == target, need also check with mingp and set msum; should not break  [-3  0  -1 4]  4
                if abs(sum-target) < mingp:
                    mingp = abs(sum-target)
                    msum = sum
            i += 1
        return msum

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        if n < 3: return 0
        res = 0
        mingap = (1<<31) -1
        for i in range(n-2):
            start = i+1
            end = n-1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                gap = abs(target-sum)
                if gap < mingap:
                    mingap = gap
                    res = sum
                if target-sum  == 0:
                    return sum
                elif target-sum < 0:
                    end-=1
                else:
                    start+=1
        return res