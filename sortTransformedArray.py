# https://leetcode.com/problems/sort-transformed-array/#/description
# Given a sorted array of integers nums and integer values a, b and c. Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

# The returned array must be in sorted order.

# Expected time complexity: O(n)

# Example:
# nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

# Result: [3, 9, 15, 33]

# nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

# Result: [-23, -5, 1, 7]

# d is the increment of i.

def sortTransformedArray(self, nums, a, b, c):
    nums = [x*x*a + x*b + c for x in nums]
    ret = [0] * len(nums)
    p1, p2 = 0, len(nums) - 1
    i, d = (p1, 1) if a < 0 else (p2, -1)
    while p1 <= p2:  #Mistake should take care of =
        if nums[p1] * -d > nums[p2] * -d:
            ret[i] = nums[p1]
            p1 += 1
        else:
            ret[i] = nums[p2]
            p2 -=1
        i += d
    return ret