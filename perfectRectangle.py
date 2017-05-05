https://leetcode.com/problems/perfect-rectangle/#/description
 
[Note]:
0)any node can't map the second time to the same postion
 direction: 1) points have to stay on the borders 2) hit two times 
   _>reverse    in other covers 2) hit one time but on the border
       two many conditions, go back to direction, easy to setup model bits, something satisfy both by math, 2+4 = 6, has to satisfy 6 like having both 2 and 4 (2), can't be other value for (1) 
       map points to encoded values , decide complete or not by decide the values satisfy above two conditions, which is the property of this graph problem
LeetCode 391. Perfect Rectangle

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
 

 

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
 

 

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
 

 

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.
 

题目大意：
给定N个与坐标轴对齐的矩形（其中N > 0），判断它们是否恰好围成一个矩形区域。

每一个矩形通过左下角和右上角的坐标表示。例如，一个单位正方形用[1,1,2,2]表示。（左下角坐标(1, 1)，右上角坐标(2, 2)）.

测试用例如题目描述。

解题思路：
解法I “顶点检查法”：

参考LeetCode Discuss，链接地址：

https://discuss.leetcode.com/topic/55923/o-n-solution-by-counting-corners-with-detailed-explaination

利用points记录各个顶点被矩形的覆盖情况

记矩形的左下、右下、右上、左上顶点为A、B、C、D，则有：

左下顶点A的坐标为(l, b)
右下顶点B的坐标为(r, b)
右上顶点C的坐标为(r, t)
左上顶点D的坐标为(l, t)
如下图所示：

        G
D |-----|-----| C
  |     |     |  
H |-----I-----| F
  |     |     |  
A |-----|-----| B
        E
将左下A、右下B、右上C、左上D分别标号为1、2、4、8（这样标号便于位运算），则有：

points[A] |= 1
points[B] |= 2
points[C] |= 4
points[D] |= 8

points[E] = points[A] | points[B] = 3 （左下顶点、右下顶点的并）
points[F] = points[B] | points[C] = 6 （右下顶点、右上顶点的并）
points[G] = points[C] | points[D] = 12 （右上顶点、左上顶点的并）
points[H] = points[A] | points[D] = 9 （左下顶点、左上顶点的并）
points[I] = points[A] | points[B] | points[C] | points[D] = 15（四个顶点的并）
Python代码：
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        left = min(x[0] for x in rectangles)
        bottom = min(x[1] for x in rectangles)
        right = max(x[2] for x in rectangles)
        top = max(x[3] for x in rectangles)

        points = collections.defaultdict(int)
        for l, b, r, t in rectangles:
            A, B, C, D = (l, b), (r, b), (r, t), (l, t)
            for p, q in zip((A, B, C, D), (1, 2, 4, 8)):
                if points[p] & q: return False
                points[p] |= q

        for px, py in points:
            if left < px < right or bottom < py < top:
                if points[(px, py)] not in (3, 6, 9, 12, 15):
                    return False
        return True

解法II 扫描线法

参阅LeetCode Discuss：https://discuss.leetcode.com/topic/55944/o-n-log-n-sweep-line-solution


Consider how the corners of all rectangles appear in the large rectangle if there's a perfect rectangular cover.
Rule 1: The local shape of the corner has to follow one of the three following patterns

Corner of the large rectangle (blue): it occurs only once among all rectangles
T-junctions (green): it occurs twice among all rectangles
Cross (red): it occurs four times among all rectangles
Rule 2: A point can only be the top-left corner of at most one sub-rectangle. Similarly it can be the top-right/bottom-left/bottom-right corner of at most one sub-rectangle. Otherwise overlaps occur.

Proof of correctness

Obviously, any perfect cover satisfies the above rules. So the main question is whether there exists an input which satisfy the above rules, yet does not compose a rectangle.

First, any overlap is not allowed based on the above rules because

aligned overlap like [[0, 0, 1, 1], [0, 0, 2, 2]] are rejected by Rule 2.
unaligned overlap will generate a corner in the interior of another sub-rectangle, so it will be rejected by Rule 1.
Second, consider the shape of boundary for the combined shape. The cross pattern does not create boundary. The corner pattern generates a straight angle on the boundary, and the T-junction generates a straight border.
So the shape of the union of rectangles has to be rectangle(s).

Finally, if there are more than two non-overlapping rectangles, at least 8 corners will be found, and cannot be matched to the 4 bounding box corners (be reminded we have shown that there is no chance of overlapping).
So the cover has to be a single rectangle if all above rules are satisfied.

Algorithm

Step1: Based on the above idea we maintain a mapping from (x, y)->mask by scanning the sub-rectangles from beginning to end.

(x, y) corresponds to corners of sub-rectangles
mask is a 4-bit binary mask. Each bit indicates whether there have been a sub-rectangle with a top-left/top-right/bottom-left/bottom-right corner at (x, y). If we see a conflict while updating mask, it suffice to return a false during the scan.
In the meantime we obtain the bounding box of all rectangles (which potentially be the rectangle cover) by getting the upper/lower bound of x/y values.
Step 2: Once the scan is done, we can just browse through the unordered_map to check the whether the mask corresponds to a T junction / cross, or corner if it is indeed a bounding box corner.
(note: my earlier implementation uses counts of bits in mask to justify corners, and this would not work with certain cases as @StefanPochmann points out).

Complexity

The scan in step 1 is O(n) because it loop through rectangles and inside the loop it updates bounding box and unordered_map in O(1) time.

Step2 visits 1 corner at a time with O(1) computations for at most 4n corners (actually much less because either corner overlap or early stopping occurs). So it's also O(n).

https://discuss.leetcode.com/topic/55923/o-n-solution-by-counting-corners-with-detailed-explaination