class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        res = 0
        heights.append(0)
        for i,h in enumerate(heights):
            while h < heights[stack[-1]]:
                j = heights[stack.pop()]
                res = max(res, j*(i-stack[-1]-1))
            stack.append(i)
        heights.pop()
        stack.pop()
        return res