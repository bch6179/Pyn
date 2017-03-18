class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        pre = lower-1
        nums.append(upper+1)
        res = [] 
        for n in nums:
            if n-pre == 2:
                res.append(str(n-1)) #Mistake not missing pre
            elif n-pre > 2:
                res.append(str(pre+1)+'->'+str(n-1))
            pre = n
        return res
        