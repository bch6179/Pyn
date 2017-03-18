#https://leetcode.com/problems/generalized-abbreviation/?tab=Description

#Maintain how many abbreviated during two branch DFS besides of pos tracking
#Nonlinear thinking tree or graph , correlation, recursive for inner structure if seeing 1ord 1o1d 1o2
#linear check list : multiple or n-for or two dfs, pass pos+1 or index+1, pass count or other variable
# Write a function to generate the generalized abbreviations of a word.
#find the recurrence relation overlapping in the examples based on the base case (last position at 4, return), from achiving results  word wor1 (first branch), decrease and conquer dfs left, dfs right;  from analysis and implementation, wxxx, 1xxx dfs recurse left and right 
# Example:
# Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# The idea is: for every character, we can keep it or abbreviate it. To keep it, we add it to the current solution and carry on backtracking. To abbreviate it, we omit it in the current solution, but increment the count, which indicates how many characters have we abbreviated. When we reach the end or need to put a character in the current solution, and count is bigger than zero, we add the number into the solution.


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, pos, cur, count, result):
            if len(word) == pos:
                # Once we reach the end, append current to the result
                result.append(cur + str(count) if count > 0 else cur)
            else:
            
                # Skip current position, and increment count
                helper(word, pos + 1, cur, count + 1, result)
                    # Include current position, and zero-out count
                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, result)

        result = []
        helper(word, 0, '', 0, result)
        return result
s= Solution()
res = s.generateAbbreviations("word")
print res


rite a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
这道题肯定是DFS/Backtracking, 但是怎么DFS不好想，跟Leetcode: Remove Invalid Parentheses的backtracking很像。

Generalized Abbreviation这道题是当前这个字母要不要abbreviate，要或者不要两种选择，Parentheses那道题是当前括号要不要keep在StringBuffer里，要或不要同样是两种选择。

 Syntax：注意27行使用StringBuffer.setLength(), 因为count一直累加可能变成两位数三位数，delete stringbuffer最后一个字母可能不行，所以干脆设置为最初进recursion的长度

参考了：https://leetcode.com/discuss/76783/easiest-14ms-java-solution-beats-100%25

复制代码
 1 public class Solution {
 2     public List<String> generateAbbreviations(String word) {
 3         List<String> res = new ArrayList<String>();
 4         dfs(0, word.toCharArray(), new StringBuffer(), 0, res);
 5         return res;
 6     }
 7     
 8     public void dfs(int pos, char[] word, StringBuffer sb, int count, List<String> res) {
 9         int len = word.length;
10         int sbOriginSize = sb.length();
11         if (pos == len) {
12             if (count > 0) {
13                 sb.append(count);
14             }
15             res.add(sb.toString());
16         }
17         else {
18             //choose to abbr word[pos]
19             dfs(pos+1, word, sb, count+1, res);
20             
21             //choose not to abbr word[pos]
22             //first append previous count to sb if count>0
23             if (count > 0) sb.append(count);
24             sb.append(word[pos]);
25             dfs(pos+1, word, sb, 0, res);
26         }
27         sb.setLength(sbOriginSize);
28     }
29 }
复制代码