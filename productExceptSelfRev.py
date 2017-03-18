class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        res= []
        for i in range(0, len(nums)):
            res.append(p)
            p = p*nums[i]
        
        p = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= p
            p *= nums[i]
            
        return res

# 特别牛逼的递归解法，非常精妙，这里分享给大家。

#     public int[] productExceptSelfRev(int[] nums) {
#         multiply(nums, 1, 0, nums.length);

#         return c;
#     }

#     private int multiply(int[] a, int fwdProduct, int indx, int N) {
#         int revProduct = 1;
#         if (indx < N) {
#             revProduct = multiply(a, fwdProduct * a[indx], indx + 1, N);
#             int cur = a[indx];
#             a[indx] = fwdProduct * revProduct;
#             revProduct *= cur;
#         }
#         return revProduct;
#     }