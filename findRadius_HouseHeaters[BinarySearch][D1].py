#  序（Sort） + 二分查找（Binary Search）

# 升序排列加热器的坐标heaters

# 遍历房屋houses，记当前房屋坐标为house：

#     利用二分查找，分别找到不大于house的最大加热器坐标left，以及不小于house的最小加热器坐标right
    
#     则当前房屋所需的最小加热器半径radius = min(house - left, right - house)
    
#     利用radius更新最终答案ans
# Python代码：
import bisect
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        ans = 0
        heaters.sort()
        for house in houses:
            radius = 0x7FFFFFFF
            le = bisect.bisect_right(heaters, house)
            if le > 0:
                radius = min(radius, house - heaters[le - 1])  #locate in the right of the first heater, find the rightest one : house >= heater
            ge = bisect.bisect_left(heaters, house)
            if ge < len(heaters):
                radius = min(radius, heaters[ge] - house)  #locate at least in the left of the last heater, find the leftmost one: house <= heater
            ans = max(ans, radius)
        return ans

#     nput: [1,2,3,4],[1,4]
# Output: 1
# Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
 

# 这道题是一道蛮有意思的题目，首先我们看题目中的例子，不管是houses还是heaters数组都是有序的，所以我们也需要给输入的这两个数组先排序，以免其为乱序。我们就拿第二个例子来分析，我们的目标是houses中的每一个数字都要被cover到，那么我们就遍历houses数组，对每一个数组的数字，我们在heaters中找能包含这个数字的左右范围，然后看离左右两边谁近取谁的值，如果某个house位置比heaters中最小的数字还小，那么肯定要用最小的heater去cover，反之如果比最大的数字还大，就用最大的数字去cover。对于每个数字算出的半径，我们要取其中最大的值。通过上面的分析，我们就不难写出代码了，我们在heater中两个数一组进行检查，如果后面一个数和当前house位置差的绝对值小于等于前面一个数和当前house位置差的绝对值，那么我们继续遍历下一个位置的数。跳出循环的条件是遍历到heater中最后一个数，或者上面的小于等于不成立，此时heater中的值和当前house位置的差的绝对值就是能cover当前house的最小半径，我们更新结果res即可，参见代码如下：

 

# 解法一：

# 复制代码
# class Solution {
# public:
#     int findRadius(vector<int>& houses, vector<int>& heaters) {
#         int n = heaters.size(), j = 0, res = 0;
#         sort(houses.begin(), houses.end());
#         sort(heaters.begin(), heaters.end());
#         for (int i = 0; i < houses.size(); ++i) {
#             int cur = houses[i];
#             while (j < n - 1 && abs(heaters[j + 1] - cur) <= abs(heaters[j] - cur)) {
#                 ++j;
#             }
#             res = max(res, abs(heaters[j] - cur));
#         }
#         return res;
#     }
# };
# 复制代码
 

# 还是上面的思路，我们可以用二分查找法来快速找到第一个大于等于当前house位置的数，如果这个数存在，那么我们可以算出其和house的差值，并且如果这个数不是heater的首数字，我们可以算出house和前面一个数的差值，这两个数中取较小的为cover当前house的最小半径，然后我们每次更新结果res即可，参见代码如下：

 

# 解法二：

# 复制代码
# class Solution {
# public:
#     int findRadius(vector<int>& houses, vector<int>& heaters) {
#         int res = 0, n = heaters.size();
#         sort(heaters.begin(), heaters.end());
#         for (int house : houses) {int left = 0, right = n;
#             while (left < right) {
#                 int mid = left + (right - left) / 2;
#                 if (heaters[mid] < house) left = mid + 1;
#                 else right = mid;
#             }
#             int dist1 = (right == n) ? INT_MAX : heaters[right] - house; # first >=
#             int dist2 = (right == 0) ? INT_MAX : house - heaters[right - 1]; #first smaller than house
#             res = max(res, min(dist1, dist2));
#         }
#         return res;
#     }
# };
# 复制代码
 

# 我们可以用STL中的lower_bound来代替二分查找的代码来快速找到第一个大于等于目标值的位置，其余部分均和上面方法相同，参见代码如下：

 

# 解法三：

# 复制代码
# class Solution {
# public:
#     int findRadius(vector<int>& houses, vector<int>& heaters) {
#         int res = 0;
#         sort(heaters.begin(), heaters.end());
#         for (int house : houses) {
#             auto pos = lower_bound(heaters.begin(), heaters.end(), house);
#             int dist1 = (pos == heaters.end()) ? INT_MAX : *pos - house;
#             int dist2 = (pos == heaters.begin()) ? INT_MAX : house - *(--pos);
#             res = max(res, min(dist1, dist2));
#         }
#         return res;
#     }
# };
# 复制代码
    # def findRadius(self, houses, heaters):  My Bad one
    #     """
    #     :type houses: List[int]
    #     :type heaters: List[int]
    #     :rtype: int
    #     """
    #     n = len(houses)
    #     m = len(heaters)
    #     maxgap = 0
        
    #     for i in range(1, m):
    #         gap = heaters[i] - heaters[i-1] - 1
    #         maxgap = gap/2 + (1 if gap % 2 == 1 else 0)
            
    #     maxgap = max(max(abs(houses[0] - heaters[0]), abs(houses[n-1] - heaters[m-1])), maxgap)
    #     return maxgap

#     Input:
# [1]
# [1,2,3,4]
# Output:
# 3
# Expected:
# 0