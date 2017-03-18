 #[0,-1,2,-1]
# [1,2,1]
#[1,1,1,2,2]
# https://leetcode.com/problems/majority-element-ii/

#bad to follow up the same pattern as I, a, b will become the same 1 after ca get minus to 0
#understand I, you could merge the first two because of not branching out based on a or b
# 1, 2, 2,3,2, vs dirctionary not dropping to the same bucket
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        ca,cb, a, b = 0,0,0,1
        for num in nums:
            if a == num:  #mistake: should be before ca == 0, otherwise,a: 8,b: 8 
                ca += 1 
            elif b == num:
                cb += 1
            elif ca == 0:
                ca = 1;a= num
            elif cb == 0:
                cb = 1;b = num
            else:
                ca -= 1; cb -= 1
        return [v for v in set([a,b]) if nums.count(v) > len(nums)/3]
    
s = Solution() 
print s.majorityElement([8,8,7,7,7])
[-1,1,1,1,2,1]    [1,1] 
[2,2,1,3]
[1,2,1]


#bad
    #   if c1 == 0 or a == num:
    #             c1 += 1
    #             a = num
    #         elif c2 == 0 or b == num:
    #             c2 += 1
    #             b = num
    #         else:
    #             c1 -= 1
    #             c2 -= 1
    #     return [x for x,i in set([(a,c1),(b,c2)]) if i > 0 and nums.count(x) > (len(nums)/3)]

# https://leetcode.com/problems/majority-element-ii/

# [LeetCode]Majority Element II
# 作者是 在线疯狂 发布于 2015年6月29日 在 LeetCode.
# 题目描述：
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

# Hint:

# How many majority elements could it possibly have?

# 题目大意：
# 给定一个大小为n的整数数组，从中找出所有出现次数超过 ⌊ n/3 ⌋ 的元素。算法应该满足线性时间复杂度和O(1)空间复杂度。

# 提示：

# 一共可能有多少个“众数”？

# 解题思路：
# 可以从Moore投票算法中得到一些启发

# 参考LeetCode Discuss（https://leetcode.com/discuss/43248/boyer-moore-majority-vote-algorithm-and-my-elaboration）

# 观察可知，数组中至多可能会有2个出现次数超过 ⌊ n/3 ⌋ 的众数

# 记变量n1, n2为候选众数； c1, c2为它们对应的出现次数

# 遍历数组，记当前数字为num

# 若num与n1或n2相同，则将其对应的出现次数加1

# 否则，若c1或c2为0，则将其置为1，对应的候选众数置为num

# 否则，将c1与c2分别减1

# 最后，再统计一次候选众数在数组中出现的次数，若满足要求，则返回之