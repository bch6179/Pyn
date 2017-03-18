Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        res = 0
        heights.append(0)
        for i, h in enumerate(heights): 
            while h < heights[stack[-1]]: # stack always non None,0 the minimum as the first top  , so skip the check
                curHeight = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, w * curHeight)
            stack.append(i) #Mistake should append i in stead of h, otherwise [2] input make it out of range
        heights.pop()    
        return res
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        n = len(matrix[0])
        heights = [0] * (n+1)
        res = 0
        for row in matrix:
            for i in range(n):
                if row[i] == '1':
                    heights[i]+=1
                else:
                    heights[i] =0
            stack = []
            i = 0
            while i < n+1: #Mistake should not use range, 2
                if not stack or heights[i] >= heights[stack[-1]]: #Mistake should >= instead of >, otherwise wrong calc
                    stack.append(i)
                    i+=1
                else:              
                    height = heights[stack.pop()]
                    res = max(res, height * ((i - stack[-1] - 1) if stack else i))
                    #Mistake in this branch no need to increase , so do not use range for auto increasing; the last 0 of height will make nothing
        
                
            #res = max(res, self.largestRectangleArea(heights))
        return res
s = Solution() 
print s.maximalRectangle(["10100","10111","11111","10010"])

# def maximalRectangle(self, matrix):
#     if not matrix or not matrix[0]:
#         return 0
#     n = len(matrix[0])
#     height = [0] * (n + 1)
#     ans = 0
#     for row in matrix:
#         for i in xrange(n):
#             height[i] = height[i] + 1 if row[i] == '1' else 0
#         stack = [-1]
#         for i in xrange(n + 1):
#             while height[i] < height[stack[-1]]: #if ori stack empty, height[-1] is 0; else height at stack.top, means go down
#                 h = height[stack.pop()]
#                 w = i - 1 - stack[-1]
#                 ans = max(ans, h * w)
#             stack.append(i)
#     return ans


# int maximalRectangle(vector<vector<char> > &matrix) {
#     if(matrix.empty()){
#         return 0;
#     }
#     int maxRec = 0;
#     vector<int> height(matrix[0].size(), 0);
#     for(int i = 0; i < matrix.size(); i++){
#         for(int j = 0; j < matrix[0].size(); j++){
#             if(matrix[i][j] == '0'){
#                 height[j] = 0;
#             }
#             else{
#                 height[j]++;
#             }
#         }
#         maxRec = max(maxRec, largestRectangleArea(height));
#     }
#     return maxRec;
# }

# int largestRectangleArea(vector<int> &height) {
#     stack<int> s;
#     height.push_back(0);
#     int maxSize = 0;
#     for(int i = 0; i < height.size(); i++){
#         if(s.empty() || height[i] >= height[s.top()]){
#             s.push(i);
#         }
#         else{
#             int temp = height[s.top()];
#             s.pop();
#             maxSize = max(maxSize, temp * (s.empty() ? i : i - 1 - s.top()));
#             i--;
#         }
#     }
#     return maxSize;
# }
# In order to solve this problem, I use the solution from "Largest Rectangle in Histogram".

# Now I assume you already know how to solve "Largest Rectangle in Histogram".

# We can regard a matrix as many histograms. For example, given a matrix below:

# 1 0 1 0

# 0 1 0 1

# 0 1 1 0

# 1 0 1 0

# 1 0 1 1

# From top to bottom, we can find these histograms:

# Number 1: 1 0 1 0

# Number 2: 0 1 0 1

# Number 3: 0 2 1 0

# Number 4: 1 0 2 0

# Number 5: 2 0 3 1

# Pass all of these histograms to the function which can solve "Largest Rectangle in Histogram". And then find the maximum one.

# Finally, we get the answer.