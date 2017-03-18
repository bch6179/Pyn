
# reverse recur  divide to 2 cases
#forward recur see if for each c before *, :b match sub d: or not; otherwise see if b: match d: or not . comparing to wildcast, extra last step and also wildcast has strict prefix check
#Forward DP divide to 3 cases
# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.

# The matching should cover the entire input string (not partial).

# The function prototype should be:
# bool isMatch(const char *s, const char *p)

# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true

cache = {}
def isMatch(self, s, p):
    if (s, p) in self.cache:
        return self.cache[(s, p)]
    if not p:
        return not s
    if p[-1] == '*':
        if self.isMatch(s, p[:-2]): #null usage of *
            self.cache[(s, p)] = True
            return True
        if s and (s[-1] == p[-2] or p[-2] == '.') and self.isMatch(s[:-1], p): # this includes one and two+matching
            self.cache[(s, p)] = True
            return True
    if s and (p[-1] == s[-1] or p[-1] == '.') and self.isMatch(s[:-1], p[:-1]):
        self.cache[(s, p)] = True
        return True
    self.cache[(s, p)] = False
    return False
DP version:

def isMatch(self, s, p):
    dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
    dp[0][0] = True
    for i in range(1, len(p)):
        dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
    for i in range(len(p)):
        for j in range(len(s)):
            if p[i] == '*':
                dp[i + 1][j + 1] = dp[i - 1][j + 1]   #a*  a : * match null   a* not exist
                                    or dp[i][j + 1]  # a*  aa: * match one  * not exist
                if p[i - 1] == s[j] or p[i - 1] == '.': #a* aaa : a* aa as a == last a
                    dp[i + 1][j + 1] |= dp[i + 1][j]
            else:
                dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')  
    return dp[-1][-1]

思路1: DP

关键在于如何处理这个'*'号。

状态：和Mininum Edit Distance这类题目一样。
dp[i][j]表示s[0:i-1]是否能和p[0:j-1]匹配。

递推公式：由于只有p中会含有regular expression，所以以p[j-1]来进行分类。
p[j-1] != '.' && p[j-1] != '*'：dp[i][j] = dp[i-1][j-1] && (s[i-1] == p[j-1])
p[j-1] == '.'：dp[i][j] = dp[i-1][j-1]

而关键的难点在于 p[j-1] = '*'。由于星号可以匹配0，1，乃至多个p[j-2]。
1. 匹配0个元素，即消去p[j-2]，此时p[0: j-1] = p[0: j-3]
dp[i][j] = dp[i][j-2]   #a*a -> a

2. 匹配1个元素，此时p[0: j-1] = p[0: j-2]
dp[i][j] = dp[i][j-1]   # a* -> a

3. 匹配多个元素，此时p[0: j-1] = { p[0: j-2], p[j-2], ... , p[j-2] }
dp[i][j] = dp[i-1][j] && (p[j-2]=='.' || s[i-1]==p[j-2])  # a a*

“s[i-2]==p[j-2]” 应该是s[i-1]==p[j-2]。 是s当前的字符等于p当前(就是*号)的前面一个字符


 
class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        int m = strlen(s), n = strlen(p);
        vector<vector<bool>> dp(m+1, vector<bool>(n+1,false));
        dp[0][0] = true;
        
        for(int i=0; i<=m; i++) {
            for(int j=1; j<=n; j++) {
                if(p[j-1]!='.' && p[j-1]!='*') {
                    if(i>0 && s[i-1]==p[j-1] && dp[i-1][j-1])
                        dp[i][j] = true;
                }
                else if(p[j-1]=='.') {
                    if(i>0 && dp[i-1][j-1])
                        dp[i][j] = true;
                }
                else if(j>1) {  //'*' cannot be the 1st element
                    if(dp[i][j-1] || dp[i][j-2])  // match 0 or 1 preceding element
                        dp[i][j] = true;
                    else if(i>0 && (p[j-2]==s[i-1] || p[j-2]=='.') && dp[i-1][j]) // match multiple preceding elements
                        dp[i][j] = true;
                }
            }
        }
        return dp[m][n];
    }
};
http://www.cnblogs.com/yuzhangcmu/p/4105529.html
class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    hash = None
    def isMatch(self, s, p):
        if self.hash is None:
            self.hash = {}
        key = s + p
        if key in self.hash:
            return self.hash[key]
            
        if p == '':
            return s == ''
        if s == '':
            if len(p) % 2 == 1:
                return False
            i = 1
            while i < len(p):
                if p[i] != '*':
                    return False
                i += 2
            return True
        
        if len(p) > 1 and p[1] == '*':
            if p[0] == '.':
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            elif p[0] == s[0]:
                self.hash[key] = self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                self.hash[key] = self.isMatch(s, p[2:])
        elif p[0] == '.':
            self.hash[key] = self.isMatch(s[1:], p[1:])
        else:
            self.hash[key] = s[0] == p[0] and self.isMatch(s[1:], p[1:])
        
        return self.hash[key]

class Solution(object):
    # DP
    def isMatch(self, s, p):
        dp = [[False for i in range(0,len(p) + 1)] for j in range(0, len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(p) + 1):
            if (p[i - 1] == '*'):
                dp[0][i] = dp[0][i - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i-1][j]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
    
        return dp[len(s)][len(p)]

    # 懒癌版
    def isMatch(self, s, p):
        return re.match(p + '$', s) != None

        If the next character of p is NOT ‘*’, then it must match the current character of s. Continue pattern matching with the next character of both s and p.
If the next character of p is ‘*’, then we do a brute force exhaustive matching of 0, 1, or more repeats of current character of p… Until we could not match any more characters.
You would need to consider the base case carefully too. That would be left as an exercise to the reader. :)

Below is the extremely concise code (Excluding comments and asserts, it’s about 10 lines of code).


bool isMatch(const char *s, const char *p) {
  assert(s && p);
  if (*p == '\0') return *s == '\0';

  // next char is not '*': must match current character
  if (*(p+1) != '*') {
    assert(*p != '*');
    return ((*p == *s) || (*p == '.' && *s != '\0')) && isMatch(s+1, p+1);
  }
  // next char is '*'
  while ((*p == *s) || (*p == '.' && *s != '\0')) {
    if (isMatch(s, p+2)) return true;
    s++;
  }
  return isMatch(s, p+2);
}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
bool isMatch(const char *s, const char *p) {
  assert(s && p);
  if (*p == '\0') return *s == '\0';
 
  // next char is not '*': must match current character
  if (*(p+1) != '*') {
    assert(*p != '*');
    return ((*p == *s) || (*p == '.' && *s != '\0')) && isMatch(s+1, p+1);
  }
  // next char is '*'
  while ((*p == *s) || (*p == '.' && *s != '\0')) {
    if (isMatch(s, p+2)) return true; #        aab c    see if :b == d:
                                      # .      a* d .    
    s++;
  }
  return isMatch(s, p+2);  #when get to b, see if b: == d:
}
Further Thoughts:
Some extra exercises to this problem:

If you think carefully, you can exploit some cases that the above code runs in exponential complexity. Could you think of some examples? How would you make the above code more efficient?
Try to implement partial matching instead of full matching. In addition, add ‘^’ and ‘$’ to the rule. ‘^’ matches the starting position within the string, while ‘$’ matches the ending position of the string.
Try to implement wildcard matching where ‘*’ means any sequence of zero or more characters.

