#1)try * possible location substrings and decrease and conquer
#2) classic reverse Metrics DP

# leetcode Question 123: Wildcard Matching
# Wildcard Matching#[Note]
#=====DFS, while helper() , anyof the case work then break
#but for RE, need check
# Implement wildcard pattern matching with support for '?' and '*'.
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") â†’ false
# isMatch("aa","aa") â†’ true
# isMatch("aaa","aa") â†’ false
# isMatch("aa", "*") â†’ true
# isMatch("aa", "a*") â†’ true
# isMatch("ab", "?*") â†’ true
# isMatch("aab", "c*a*b") â†’ false
Method 2:

We could use recursive method. Recursive: we just check one step. Iterative: we use while to check all steps
Function: starting from l and r, the left part do match.
Base Case: If r reaches the end of str, we need to check if l also reaches the end of pattern. If so, match.
Reduction: check the current char in pattern string
If regular, just increase l and r by 1;
If *, first, go to the last *, and then check if match. (we have to use while loop to find the correct starting point.)
public class Solution {
    public boolean isMatch(String s, String p) {
        return helper(s,p,0,0);
         
    }
   //Method 3 use DP
public class Solution {
    public boolean isMatch(String s, String p) {
        int width = s.length();
        int height = p.length();
         
        boolean[][] dp = new boolean[width + 1][height + 1];
        dp[0][0] = true;
         
        for (int i = 1; i <= width; i++){
            for (int j = 1; j <= height; j++){
                if (s.charAt(i-1) == p.charAt(j-1) || p.charAt(j-1) == '?'){
                    dp[i][j] = dp[i-1][j-1];
                }else if (p.charAt(j-1) == '*'){
                    int cur = i;
                    while (cur > 0){
                        if (dp[cur-1][j-1]){
                            dp[i][j]= true;
                            break;
                        }
                        cur--;
                    }
                }
            }
        }
         
        return dp[width][height];
    }
}  
     
    boolean helper(String s, String p, int l, int r) {//forward recursion
           if(r == p.length()) return l == s.length();
            
           if(p.charAt(r) == '*') {
                 while(r < p.length() && p.charAt(r) == '*') r++;   // Move the index at p to a non-start char.
                 while(l < s.length()) {
                     if(helper(s, p, l, r)) return true; // Find one match, return true.
                      l++; // Try the next one.
                  }
                 return helper(s, p, l, r);
            }else if(l < s.length() && (p.charAt(r) == '?' || s.charAt(l) == p.charAt(r))){
                return helper(s, p, l + 1, r + 1);
            }else{
                 return false;
            }
    }
 
}


The reason that the iterative solution is much faster for this case is we only need to save (and deal with) the positions (iStar for s, jStar for p) of the last "" we met. We only need to do traceback using iStar and jStar and all the previous "" can be ignored since the last "" will cover all the traceback cases for the previous "".
What we need to do are

if the current p character is '' (i.e. p[j]==''), then we update iStar and jStar with the cureent i and j values. iStar/jStar will be used for traceback. Also we do --i to start the depth first search with the case that '*' represents a null string.
if p[j]!='', then we check if mismatch occurs (i.e. p[j]!=s[i] and p[j]!='?'), if so we check if we met a '' before (iStar>=0), if not, then we return false since no match can achieve. Otherwise, we traceback to the positions at which the last '*' happens and do the next possible dfs search (i.e. i = iStar++; j = jStar; remember to update iStar too to save the i position to try in the next traceback).
The loop will quit when we reach the end of s. At last, we need to skip all the '*' in p to see if we can reach the end of p. if so, match, otherwise mismatch
class Solution {
public:
    bool isMatch(string s, string p) {
        int  slen = s.size(), plen = p.size(), i, j, iStar=-1, jStar=-1;

        for(i=0,j=0 ; i<slen; ++i, ++j)
        {
            if(p[j]=='*')
            { //meet a new '*', update traceback i/j info
                iStar = i;
                jStar = j;
                --i;
            }
            else
            { 
                if(p[j]!=s[i] && p[j]!='?')
                {  // mismatch happens
                    if(iStar >=0)
                    { // met a '*' before, then do traceback
                        i = iStar++;
                        j = jStar;
                    }
                    else return false; // otherwise fail
                }
            }
        }
        while(p[j]=='*') ++j;
        return j==plen;
    }
};



public class Solution {
    public boolean isMatch(String s, String p) {
        boolean[][] match=new boolean[s.length()+1][p.length()+1];
        match[s.length()][p.length()]=true;
        for(int i=p.length()-1;i>=0;i--){
            if(p.charAt(i)!='*')
                break;
            else
                match[s.length()][i]=true;
        }
        for(int i=s.length()-1;i>=0;i--){
            for(int j=p.length()-1;j>=0;j--){
                if(s.charAt(i)==p.charAt(j)||p.charAt(j)=='?')
                        match[i][j]=match[i+1][j+1];
                else if(p.charAt(j)=='*')
                        match[i][j]=match[i+1][j]||match[i][j+1];
                else
                    match[i][j]=false;
            }
        }
        return match[0][0];
    }
}


A DP solution is also given here. It has O(N^2) time complexity and O(N) space

class Solution {
public:
    bool isMatch(string s, string p) {
        int pLen = p.size(), sLen = s.size(), i, j, k, cur, prev;
        if(!pLen) return sLen == 0;
        bool matched[2][sLen+1];
        fill_n(&matched[0][0], 2*(sLen+1), false);
        
        matched[0][0] = true;
        for(i=1; i<=pLen; ++i)
        {
            cur = i%2, prev= 1-cur;
            matched[cur][0]= matched[prev][0] && p[i-1]=='*';
            if(p[i-1]=='*') for(j=1; j<=sLen; ++j) matched[cur][j] = matched[cur][j-1] || matched[prev][j];
            else for(j=1; j<=sLen; ++j)            matched[cur][j] =  matched[prev][j-1] && (p[i-1]=='?' || p[i-1]==s[j-1]) ;
        }
            return matched[cur][sLen];
    }
};
A recursion version. A typical recursion version will give us TLE due to too many unnecessary recursive calls. As we explained, all the traceback recursive calls at the '' we met (except the last '') are unneccessary and should be avoided. In the below version, we use recLevel to track the recursion level (i.e the total '' we met) and we also use curLevel to save the order of '' we currently process. If it is not the last '' we met (i.e if(recLevel>curLevel+1) ), then we will return false directly ( if(recLevel>curLevel+1) return false;) to skip all unneccessary recursion call at the '' before the last '*'.

class Solution {
private:
    bool helper(const string &s, const string &p, int si, int pi, int &recLevel)
    {
        int sSize = s.size(), pSize = p.size(), i, curLevel = recLevel;
        bool first=true;
        while(si<sSize && (p[pi]==s[si] || p[pi]=='?')) {++pi; ++si;} //match as many as possible
        if(pi == pSize) return si == sSize; // if p reaches the end, return
        if(p[pi]=='*')
        { // if a star is met
            while(p[++pi]=='*'); //skip all the following stars
            if(pi>=pSize) return true; // if the rest of p are all star, return true
            for(i=si; i<sSize; ++i)
            {   // then do recursion
                if(p[pi]!= '?' && p[pi]!=s[i]) continue;
                if(first) {++recLevel; first = false;}
                if(helper(s, p, i, pi, recLevel)) return true;
                if(recLevel>curLevel+1) return false; // if the currently processed star is not the last one, return
            }
        }
        return false;
    }
public:
    bool isMatch(string s, string p) {
        int recLevel = 0;
        return helper(s, p, 0, 0, recLevel);
    }
};
# Analysis:

# For each element in s
# If *s==*p or *p == ? which means this is a match, then goes to next element s++ p++.
# If p=='*', this is also a match, but one or many chars may be available, so let us save this *'s position and the matched s position.
# If not match, then we check if there is a * previously showed up,
#        if there is no *,  return false;
#        if there is an *,  we set current p to the next element of *, and set current s to the next saved s position.

# e.g.

# abedd
# ?b*d**

# a=?, go on, b=b, go on,
# e=*, save * position star=3, save s position ss = 3, p++
# e!=d,  check if there was a *, yes, ss++, s=ss; p=star+1
# d=d, go on, meet the end.
# check the rest element in p, if all are *, true, else false;

# Note that in char array, the last is NOT NULL, to check the end, use  "*p"  or "*p=='\0'".

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        s_cur = 0;
        p_cur= 0;
        match = 0;
        star = -1;
        while s_cur<len(s):
            if p_cur< len(p) and (s[s_cur]==p[p_cur] or p[p_cur]=='?'):
                s_cur = s_cur + 1
                p_cur = p_cur + 1
            elif p_cur<len(p) and p[p_cur]=='*':
                match = s_cur
                star = p_cur
                p_cur = p_cur+1
            elif (star!=-1):
                p_cur = star+1
                match = match+1
                s_cur = match
            else:
                return False
        while p_cur<len(p) and p[p_cur]=='*':
            p_cur = p_cur+1
             
        if p_cur==len(p):
            return True
        else:
            return False
                 

#                  In my understanding, if current p is to its end, then *p ='\0' (remember the last element in a char array is '\0'). Therefore, the first two if co#[Note]ndition will be false in the code, when the 3rd if (no star exists) is also false, the while loop will halt and return false.

# ZephyrAugust 28, 2014 at 9:51 PM
# 不是DP，这个解是个二叉树结构
# if *p == '*'
# isMatch(s, p) = isMatch(s, p + 1) || isMatch(s + 1, p + 1) || ... || isMatch(s + n, p+1)
# = isMatch(s, p + 1) || isMatch(s + 1, p)
# else
# 只有一个分叉 = isMatch(s+1, p+1)

# 这个算法的关键是当左子树再遇到＊的时候，上次遇到＊分裂出来的右子树就不用搜索了。
# 例如：s = aab... p = *a*b...
# aab..., *a*b...
# aab..., a*b... ab..., *a*b...
# ab..., *b...

# 第二次遇到＊的时候 s = ab... p = *b...
# 如果s和p不匹配，那么上次遇到＊的右子树ab..., *a*b...也肯定不匹配（可以用反证法来证明）。
# 如果匹配，搜索左子树就能找到结果。 

# 假设ab...和*a*b...匹配，那么ab...和*b...肯定匹配，和条件相反。
For a 2d table, dp[i][j] would mean whether sub-pattern p[:i + 1] matches sub-string s[:j + 1].
Most tricky part is when the current pattern letter is *, suppose its index is i, p[:i + 1] will match sub-string s[:j + 1] if p[:i + 1] matches s[:j] or p[:i] matches s[:j + 1], namely current cell value is true if its top or its left is true. Since the current row only depends on the previous row, we can use two rolling lists to do the dp instead of a matrix.

def isMatch(self, s, p):
    l = len(s)
    if len(p) - p.count('*') > l:
        return False
    dp = [True]  + [False] * l
    for letter in p:
        new_dp = [dp[0] and letter == '*']
        if letter == '*':
            for j in range(l):
                new_dp.append(new_dp[-1] or dp[j + 1])
        elif letter == '?':
            new_dp += dp[:l]
        else:
            new_dp += [dp[j] and s[j] == letter for j in range(l)]
        dp = new_dp
    return dp[-1]
class Solution:
# @return a boolean
def isMatch(self, s, p):
    length = len(s)
    if len(p) - p.count('*') > length:
        return False
    dp = [True] + [False]*length
    for i in p:
        if i != '*':
            for n in reversed(range(length)):
                dp[n+1] = dp[n] and (i == s[n] or i == '?')
        else:
            for n in range(1, length+1):  # hard to under stand , see next one
                dp[n] = dp[n-1] or dp[n]
        dp[0] = dp[0] and i == '*'
    return dp[-1]
dp[n] means the substring s[:n] if match the pattern i

dp[0] means the empty string '' or s[:0] which only match the pattern '*'

use the reversed builtin because for every dp[n+1] we use the previous 'dp'

add Java O(m*n) version code
