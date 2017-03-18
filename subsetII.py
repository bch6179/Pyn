class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    #def subsetsWithDup2(self, nums):
    # """
    # :type nums: List[int]
    # :rtype: List[List[int]]
    # """
    # def dfs2(pos, path):
    #         res.append(list(path))
    #         for i in range(pos, len(nums)):
    #             # if i > 0 and nums[i] == nums[i-1] and nums[i] not in path:
    #             #     continue
    #             if i > pos and nums[i] == nums[i-1]:
    #                 continue
    #             path.append(nums[i])
    #             dfs2(i+1, path)
    #             path.pop(-1)
    #     res = []
    #     #self.helper(sorted(nums), 0, [], res)
    #     nums = sorted(nums)
    #     dfs2(0, [])
    #     return res

    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)): #argu1 decide where to start inserting, for duplicated ,only insert to the last one when it's not duplicated
                res.append(res[j] + [S[i]])
        return res
# if S[i] is same to S[i - 1], then it needn't to be added to all of the subset, just add it to the last l subsets which are created by adding S[i - 1]

s= Solution()
print s.subsetsWithDup([1,1,1,1])