Total Accepted: 115316
Total Submissions: 318927
Difficulty: Medium
Contributors: Admin
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Subscribe to see which companies asked this question.

#dp is not possible , location specified, can't find relation between subproblems
def maxArea(heights):
    start = 0
    end = len(heights)-1
    res = 0
    while start < end:
        mh =  min(heights[start], heights[end])
        res = max(res, mh*(end-start))

        while start < end and heights[start] <= mh:
            start+=1
        while start < end and heights[end] <= mh:
            end-=1
    return res

print maxArea([6,11,10,3])
# Simple and fast C++/C with explanation
# Start by evaluating the widest container, using the first and the last line. All other possible containers are less wide, so to hold more water, they need to be higher. Thus, after evaluating that widest container, skip lines at both ends that don't support a higher height. Then evaluate that new container we arrived at. Repeat until there are no more possible containers left.

# C++
# # two pointers greedy
# int maxArea(vector<int>& height) {
#     int water = 0;
#     int i = 0, j = height.size() - 1;
#     while (i < j) {
#         int h = min(height[i], height[j]);
#         water = max(water, (j - i) * h);
#         while (height[i] <= h && i < j) i++;  #6   7  2 3 only skip j for 2 , not 7, so that 6*6 get chance
#         while (height[j] <= h && i < j) j--;
#     }
#     return water;