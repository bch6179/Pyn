Replacement 最长重复字符置换

时间：2016-10-26 09:25:00      阅读：153      评论：0      收藏：0      [点我收藏+] 
原文：http://www.cnblogs.com/grandyang/p/5999050.html
 

Given a string that consists of only uppercase English letters, you can replace any letter in the string with another letter at most k times. Find the length of a longest substring containing all repeating letters you can get after performing the above operations.

Note:
Both the string‘s length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two ‘A‘s with two ‘B‘s or vice versa.
Example 2:

Input:
s = "AABAbBBA", k = 1

Output:
4

Explanation:
Replace the one ‘A‘ in the middle with ‘B‘ and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
 

这道题给我们了一个字符串，说我们有k次随意置换任意字符的机会，让我们找出最长的重复字符的字符串。这道题跟之前那道Longest Substring with At Most K Distinct Characters很像，都需要用滑动窗口Sliding Window来解。我们首先来想，如果没有k的限制，让我们求把字符串变成只有一个字符重复的字符串需要的最小置换次数，那么就是字符串的总长度减去出现次数最多的字符的个数。如果加上k的限制，我们其实就是求满足(子字符串的长度减去出现次数最多的字符个数)<=k的最大子字符串长度即可，搞清了这一点，我们也就应该知道怎么用滑动窗口来解了吧我们用一个变量start记录滑动窗口左边界，初始化为0，然后我们遍历字符串，每次累加出现字符的个数，然后更新出现最多字符的个数，然后我们判断当前滑动窗口是否满足之前说的那个条件，如果不满足，我们就把滑动窗口左边界向右移动一个，并注意去掉的字符要在counts里减一，直到满足条件，我们更新结果res即可，参见代码如下：

 

class Solution {
public:
    int characterReplacement(string s, int k) {
        int res = 0, maxCnt = 0, start = 0;
        vector<int> counts(26, 0);
        for (int i = 0; i < s.size(); ++i) {
            maxCnt = max(maxCnt, ++counts[s[i] - ‘A‘]);
            while (i - start + 1 - maxCnt > k) { #read from <- changeable k less than the needed, we need to adjust, otherwise keeping increasing
                --counts[s[start] - ‘A‘];
                ++start;
            }
            res = max(res, i - start + 1);
        }
        return res;
    }
};
 

类似题目：

Longest Substring with At Least K Repeating Characters

Longest Substring with At Most K Distinct Characters

Longest Substring with At Most Two Distinct Characters

Longest Substring Without Repeating Characters

 [Sliding window](similar to finding longest substring with k distinct characters)

Similar idea in Python but allowing any character, not just uppercase English letters [Updated based on comments below]:

def characterReplacement(self, s, k):
    res = lo = hi = 0
    counts = collections.Counter()
    for hi in range(1, len(s)+1):
        counts[s[hi-1]] += 1
        max_char_n = counts.most_common(1)[0][1]
        if hi - lo - max_char_n > k:
            counts[s[lo]] -= 1
            lo += 1
    return hi - lo
[Original code in order to understand comment from @StefanPochmann was:]

def characterReplacement(self, s, k):
    res = lo = 0
    counts = collections.Counter()
    for hi in range(len(s)):
        counts[s[hi]] += 1
        max_char_n = counts.most_common(1)[0][1]
        while (hi - lo - max_char_n + 1 > k):
            counts[s[lo]] -= 1
            lo += 1
        res = max(res, hi - lo + 1)
    return res
2 months ago reply quote 
4
POSTS 504
VIEWS Reply Back To Leetcode    Mark unread   Not Watching   Sort by 
2
  StefanPochmann  
Reputation:  11,649
I don't think you need while, because from one for-loop iteration to the next, hi - lo - max_char_n + 1 can grow by at most 1, and each while-loop iteration decreases it by 1. So you can also use if instead. It also means that your window never shrinks, so you can just return the length of the final window:

def characterReplacement(self, s, k):
    res = lo = 0
    counts = collections.Counter()
    for hi in range(len(s)):
        counts[s[hi]] += 1
        max_char_n = counts.most_common(1)[0][1]
        if hi - lo - max_char_n + 1 > k:
            counts[s[lo]] -= 1
            lo += 1
    return hi - lo + 1
Only problem would be if s were the empty string, but while the problem doesn't rule that out, it's also not in the test suite. Anyway, the C++ solution I made out of it doesn't have that problem and is also a bit shorter.

onquer this problem using Python && sliding window && dictionary && heap

0
  Ipeq1 
Reputation:  19
Idea:
Step 1. Just welcome the new comer.
Step 2. Relocation the starting point trying to make the window a largest and valid expanded window.
Step 3. Update the answer

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        window, strt, charcnt, ans = [], 0, {}, 0
        for i in xrange(len(s)):
            #Step 1
            tmp = None
            if s[i] in charcnt:
                tmp = charcnt[s[i]]
                tmp[0] -= 1
            else:
                tmp = [-1, s[i]]
                charcnt[s[i]] = tmp
                heapq.heappush(window, tmp)
            #Step 2
            while (i - strt + 1) + (heapq.nsmallest(1, window))[0][0] > k:
                charcnt[s[strt]][0] += 1
                strt += 1
            #Step 3
            ans = max(ans, 1 + i - strt)
        return ans