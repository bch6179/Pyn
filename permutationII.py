class Solution(object):
    def permuteUnique2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums,path,visited):
            if len(nums) == len(path):
                res.append(path)
                return 
            
            for i, num in enumerate(nums):
                if  visited[i]:
                    continue
    
                if i > 0 and nums[i-1] == nums[i] and not visited[i-1]:
                     continue  

                visited[i] = True
                dfs(nums, path+[num], visited)
                visited[i] = False
        res = []
        dfs(sorted(nums), [], [False]*len(nums))
        return list(res)

    #     To find the last index for inserting new number n into old permutation p, I search for previous instances of n in p. But because index throws an exception if unsuccessful, I add a sentinel n at the end (which is the appropriate last insertion index then).

    def permuteUnique(self, nums):
        perms = [[]]
        for n in nums:
            perms = [p[:i] + [n] + p[i:]
                    for p in perms
                    for i in xrange((p + [n]).index(n) + 1)]
        return perms
    # Or as "one-liner" using reduce:

    # def permuteUnique(self, nums):
    #     return reduce(lambda perms, n: [p[:i] + [n] + p[i:]
    #                                     for p in perms
    #                                     for i in xrange((p + [n]).index(n) + 1)],
    #                 nums, [[]])
s= Solution()
print s.permuteUnique([1,1,3])

