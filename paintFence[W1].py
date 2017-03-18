# Paint Fence
# There is a fence with n posts, each post can be painted with one of the k colors.

# You have to paint all the posts such that no more than two adjacent fence posts have the same color.

# Return the total number of ways you can paint the fence.

# Note: n and k are non-negative integers.
# 哈希表法
# 复杂度
# 时间 O(N) 空间 O(1)

class Solution(object):
    def paintFence(self, n, k):

        F = [0, k, k*k, 0]
        if n <=2: return F[n]
        for i in range(3, n+1):
            F[3] = (k-1)*(F[1] + F[2])
            F[1]= F[2]
            F[2] = F[3]
        return F[3]
s = Solution() 
print s.paintFence(3,3)