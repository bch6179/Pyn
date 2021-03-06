Largest Rectangle in Histogram(直方图最大面积)

具体的题目描述为：
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height =[2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area =10 unit.
For example,
Given height = [2,1,5,6,2,3],
return 10.
这道题可以有两个解法。
解法一是穷举法，对于直方图的每一个右边界，穷举所有的左边界。将面积最大的那个值记录下来。时间复杂度为O(n^2). 单纯的穷举在LeetCode上面过大集合时会超时。可以通过选择合适的右边界，做一个剪枝(Pruning)。观察发现当height[k] >= height[k - 1]时，无论左边界是什么值，选择height[k]总会比选择height[k - 1]所形成的面积大。因此，在选择右边界的时候，首先找到一个height[k] < height[k - 1]的k，然后取k - 1作为右边界，穷举所有左边界，找最大面积。
Java代码：
[java] view plain copy
// O(n^2) with pruning  
public int largestRectangleArea1(int[] height) {  
  // Start typing your Java solution below  
  // DO NOT write main() function  
  int area = 0;  
  for (int i = 0; i < height.length; i++) {  
    for (int k = i + 1; k < height.length; k++) {  
      if (height[k] < height[k - 1]) {  
        i = k - 1;  
        break;  
      } else {  
        i = k;  
      }  
    }  
    int lowest = height[i];  
    for (int j = i; j >= 0; j--) {  
      if (height[j] < lowest) {  
        lowest = height[j];  
      }  
      int currArea = (i - j + 1) * lowest;  
      if (currArea > area) {  
        area = currArea;  
      }  
    }  
  }  
  return area;  
}  

虽然上面的解法可以过大集合，但是不是最优的方法，下面介绍使用两个栈的优化解法。时间复杂度为O(n).
此解法的核心思想为：一次性计算连续递增的区间的最大面积，并且考虑完成这个区间之后，考虑其前、后区间的时候，不会受到任何影响。也就是这个连续递增区间的最小高度大于等于其前、后区间。
这个方法非常巧妙，最好通过一个图来理解：

假设输入直方图为：int[] height = {2,7,5,6,4}.
这个方法运行的时候，当遇到height[2] == 5的时候，发现其比之前一个高度小，则从当前值（5）开始，向左搜索比当前值小的值。当搜索到最左边（2）时，比5小，此时计算在height[0]和height[2]之间的最大面积，注意不包括height[0]和和height[2]。height[1]以红色标出的这个区域就被计算完成。同样的方法，计算出绿色和粉色的面积。
因此这个方法需要使用两个栈。第一个栈为高度栈heightStack，用于记录还没有被计算过的连续递增的序列的值。第二个栈为下标栈indexStack，用于记录高度栈中对应的每一个高度的下标，以计算宽度。
算法具体执行的步骤为：
若heightStack为空或者当前高度大于heightStack栈顶，则当前高度和当前下标分别入站。所以heightStack记录了一个连续递增的序列。
若当前高度小于heightStack栈顶，heightStack和indexStack出栈，直到当前高度大于等于heightStack栈顶。出栈时，同时计算区间所形成的最大面积。注意计算完之后，当前值入栈的时候，其对应的下标应该为最后一个从indexStack出栈的下标。比如height[2]入栈时，其对应下标入栈应该为1，而不是其本身的下标2。如果将其本身下标2入栈，则计算绿色区域的最大面积时，会忽略掉红色区域。
Java代码：
[java] view plain copy
// O(n) using two stacks  
public int largestRectangleArea(int[] height) {  
  // Start typing your Java solution below  
  // DO NOT write main() function  
  int area = 0;  
  java.util.Stack<Integer> heightStack = new java.util.Stack<Integer>();  
  java.util.Stack<Integer> indexStack = new java.util.Stack<Integer>();  
  for (int i = 0; i < height.length; i++) {  
    if (heightStack.empty() || heightStack.peek() <= height[i]) {  
      heightStack.push(height[i]);  
      indexStack.push(i);  
    } else if (heightStack.peek() > height[i]) {  
      int j = 0;  
      while (!heightStack.empty() && heightStack.peek() > height[i]) {  
        j = indexStack.pop();  
        int currArea = (i - j) * heightStack.pop();  
        if (currArea > area) {  
          area = currArea;  
        }  
      }  
      heightStack.push(height[i]);  
      indexStack.push(j);  
    }  
  }  
  while (!heightStack.empty()) {  
    int currArea = (height.length - indexStack.pop()) * heightStack.pop();  
    if (currArea > area) {  
      area = currArea;  
    }  
  }  
  return area;  
}  

更新：
在网上发现另外一个使用一个栈的O(n)解法，代码非常简洁，栈内存储的是高度递增的下标。对于每一个直方图高度，分两种情况。1：当栈空或者当前高度大于栈顶下标所指示的高度时，当前下标入栈。否则，2：当前栈顶出栈，并且用这个下标所指示的高度计算面积。而这个方法为什么只需要一个栈呢？因为当第二种情况时，for循环的循环下标回退，也就让下一次for循环比较当前高度与新的栈顶下标所指示的高度，注意此时的栈顶已经改变由于之前的出栈。
Java代码：
[java] view plain copy
// O(n) using one stack  
public int largestRectangleArea(int[] height) {  
  // Start typing your Java solution below  
  // DO NOT write main() function  
  int area = 0;  
  java.util.Stack<Integer> stack = new java.util.Stack<Integer>();  
  for (int i = 0; i < height.length; i++) {  
    if (stack.empty() || height[stack.peek()] < height[i]) {  
      stack.push(i);  
    } else {  
      int start = stack.pop();  
      int width = stack.empty() ? i : i - stack.peek() - 1;  
      area = Math.max(area, height[start] * width);  
      i--;  
    }  
  }  
  while (!stack.empty()) {  
    int start = stack.pop();  
    int width = stack.empty() ? height.length : height.length - stack.peek() - 1;  
    area = Math.max(area, height[start] * width);        
  }  
  return area;  
}  

======not correct one
public class Solution {
    public int largestRectangleArea(int[] height) {
        if (height == null || height.length == 0) {
            return 0;
        }
        
        Stack<Integer> stack = new Stack<Integer>();
        int max = 0;
        for (int i = 0; i <= height.length; i++) {
            int curt = (i == height.length) ? -1 : height[i];
            while (!stack.isEmpty() && curt <= height[stack.peek()]) {
                int h = height[stack.pop()];
                int w = stack.isEmpty() ? i : i - stack.peek() - 1;
                max = Math.max(max, h * w);
            }
            stack.push(i);
        }
        
        return max;
    }
}

package Algorithms.array;



import java.util.Stack;



public class LargestRectangleArea {

    public static void main(String[] strs) {

        int[] height = {0};

        System.out.println(largestRectangleArea(height));

    }

    

    public static int largestRectangleArea(int[] height) {

        if (height == null || height.length == 0) {

            return 0;

        }

        

        Stack<Integer> s = new Stack<Integer>();

        

        int max = 0;

        

        int len = height.length;

        int i = 0;

        

        while (i <= len) {

            // BUG 1: should use height[s.peek()] instead of s.peek().

            // BUG 2: should put i < length after the s.isEmpty.

            // The last step: Length is also put into the stack and will break at last.

            if (s.isEmpty() || (i < len && height[i] >= height[s.peek()])) {

                s.push(i);

                i++;

            // Keep a Ascending sequence in the stack.    

            } else {

                // Stack is not empty, and the current node is smaller than the one in the stack.

                // When we come to the end of the array, we will also should count all the solutions.

                // BUG 3: should use height[s.pop] instead of s.pop

                // When the i come to the end, the rectangle will be counted again.

                int h = height[s.pop()];

                int width = s.isEmpty() ? i: i - s.peek() - 1;

                max = Math.max(max, h * width);

            } 

        }

        

        return max;

    }

}
return 10.
SOLUTION 1:
http://fisherlei.blogspot.com/2012/12/leetcode-largest-rectangle-in-histogram.html
使用递增栈来处理。每次比较栈顶与当前元素。如果当前元素小于栈顶元素，则入站，否则合并现有栈，直至栈顶元素小于当前元素。结尾入站元素0，重复合并一次。
1. 当遇到一个违反递增关系的元素时，例如：
2， 1， 5， 6， 2， 3
（1）. S: 2
 (2).   S: 2    新的元素1比2要小，表示Index = 0的这个直方图的右边界到达了，我们可以计算以它高度的最大直方。那么这个宽度如何计算呢？
     i = 1,   而2弹出后，栈为空，宽度是从i到最左边（因为这是一个递增栈，如果现在栈为空，表示我们取出的当前直方是最低的直方，它的宽度可以一直延展到最左边。）
                                假如栈不为空，则宽度是 i - s.peek() - 1 (因为要减去s.peek()这个直方本身，它比s.pop()要低，阻止了s.pop()这个直方向左边延展)
        2 弹出后，栈为空。 
(3).  S: 1， 5， 6（这三个是连续递增，就让它们一直入栈）
(4).  S: 1, 5, 6 现在我们遇到2， 6 出栈，它的宽度是6本身（i - 5所在的索引- 1)。5出栈，宽度是i - 1所在的索引 - 1
(5).  因为2比1要高，所以我们停止计算直方，把2继续入栈。然后3入栈。
(6).  这时index = len. 我们直接到第二个分支，把1， 2， 3 这三个直方计算了。
(7).  栈为空，index = len 会入栈，然后index++ 越界，下一次就退出了。这里我们不可以把index < len 放在第一个判断的前面来判断，因为这样的话，当index = len,
会直接再进入第二个分支，引发越界错误。其实我们就是假设在整个直方的最后存在一个height = 0的直方，所以我们要在一直计算到Index = len为止。而且因为它高度为0比谁都要低，所以可以把这个索引直接入栈

对于每一个height，遍历前面所有的height，求取面积最大值。时间复杂度是O(n*n)

[Code]
1:  int largestRectangleArea(vector<int> &height) {  
2:      // Start typing your C/C++ solution below  
3:      // DO NOT write int main() function  
4:      //int result[height.size()];  
5:      int maxV = 0;  
6:      for(int i =0; i< height.size(); i++)  
7:      {  
8:        int minV = height[i];  
9:        for(int j =i; j>=0; j--)  
10:        {  
11:          minV = std::min(minV, height[j]);  
12:          int area = minV*(i-j+1);  
13:          if(area > maxV)  
14:            maxV = area;  
15:        }  
16:      }  
17:      return maxV;  
18:    }  

可以过小数据，但是大数据超时。可以理解，这个解法包含了很多重复计算。一个简单的改进，是只对合适的右边界（峰顶），往左遍历面积。

1:  int largestRectangleArea(vector<int> &height) {   
2:       int maxV = 0;   
3:       for(int i =0; i< height.size(); i++)  
4:       {  
5:            if(i+1 < height.size()   
6:                      && height[i] <= height[i+1]) // if not peak node, skip it  
7:                 continue;  
8:            int minV = height[i];   
9:            for(int j =i; j>=0; j--)   
10:            {   
11:                 minV = std::min(minV, height[j]);   
12:                 int area = minV*(i-j+1);   
13:                 if(area > maxV)   
14:                 maxV = area;   
15:            }   
16:       }  
17:       return maxV;   
18:  }   

这样的话，就可以通过大数据。但是这个优化只是比较有效的剪枝，算法仍然是O(n*n).

想了半天，也想不出来O(n)的解法，于是上网google了一下。
如下图所示，从左到右处理直方，i=4时，小于当前栈顶（及直方3），于是在统计完区间[2,3]的最大值以后，消除掉阴影部分，然后把红线部分作为一个大直方插入。因为，无论后面还是前面的直方，都不可能得到比目前栈顶元素更高的高度了。



这就意味着，可以维护一个递增的栈，每次比较栈顶与当前元素。如果当前元素小于栈顶元素，则入站，否则合并现有栈，直至栈顶元素小于当前元素。结尾入站元素0，重复合并一次。

思路很巧妙。代码实现如下, 大数据 76ms过。
1:     int largestRectangleArea(vector<int> &height) {  
2:      // Start typing your C/C++ solution below  
3:      // DO NOT write int main() function  
4:      int stack[height.size()+1], width[height.size()+1];  
5:      if(height.size() == 0) return 0;  
6:      int top = 0, area = INT_MIN;  
7:      stack[0] = 0;  
8:      width[0] = 0;  
9:      int newHeight;  
10:     for(int i =0; i<= height.size(); i++)  
11:     {  
12:        if(i < height.size()) newHeight = height[i];  
13:        else newHeight = -1;  
14:        if(newHeight>= stack[top])  
15:        {  
16:            stack[++top] = newHeight;  
17:            width[top] = 1;  
18:        }  
19:        else  
20:        {  
21:            int minV = INT_MAX;  
22:            int wid= 0;  
23:            while(stack[top] > newHeight)  
24:            {  
25:               minV = min(minV, stack[top]);  
26:               wid += width[top];  
27:               area = max(area, minV*(wid));  
28:               top--;  
29:             }  
30:             stack[++top] = newHeight;  
31:             width[top] = wid+1;  
32:         }  
33:      }  
34:      return area;       
35:    }  