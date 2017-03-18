#{Note}: take care two cases: 1) () 2) (())

# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# Subscribe to see which companies asked this question


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if   len(s) <= 1:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(': 
                    dp[i] = 2 + (dp[i-2] if i >= 2 else 0)
                else:                                           # i-dp[i-1]-1     i
                    if i -dp[i-1]-1 >= 0: # only consider possible pairs   x x(()))
                        if s[i-dp[i-1]-1] == '(': # #Mistake this will output 4: "())"
                            dp[i] = 2 + dp[i-1] + (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else 0)
                    #     else: #invalid case for ending up with )())
                    #         dp[i] = dp[i-dp[i-1]] + dp[i-1]
                    # else: dp[i] = dp[i-1]
        return max(dp)
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        globalRes = 0
        left  = -1
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
                 
            else:
                
                if not stack: # empty
                    left = i
                else:
                    stack.pop()
                    if not stack:
                        globalRes = max(i-left, globalRes)  # () or )()
                    else:
                        globalRes = max(i-stack[-1], globalRes) #use peek after pop to solve the problem of (()) or (() , not able to accumulated; seeing that left not changed
                    
        return globalRes
# when see invalid, res = max(gmax, res) , res = 0
# otherwise, res+= j-i when seeing valid parenthese  bad, stack (res, i) and set res = 0, when pop , res = ores + i-j+1


Simple JAVA solution, O(n) time, one stack
public class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack<Integer>();
        int max=0;
        int left = -1;
        for(int j=0;j<s.length();j++){
            if(s.charAt(j)=='(') stack.push(j);            
            else {
                if (stack.isEmpty()) left=j;
                else{
                    stack.pop();
                    if(stack.isEmpty()) max=Math.max(max,j-left);
                    else max=Math.max(max,j-stack.peek()); #Mistake (() one of my mistake , not considering this case; res += not correct for (()) 2+4,  #second thought, actually work after reset res to 0 for second (, and push (0, 1 ), when pop , ores+i-j+1, not considering current res
                }
            }
        }
        return max;
    }
}

My DP, O(n) solution without using stack
My solution uses DP. The main idea is as follows: I construct a array longest[], for any longest[i], it stores the longest length of valid parentheses which is end at i.

And the DP idea is :

If s[i] is '(', set longest[i] to 0,because any string end with '(' cannot be a valid one.

Else if s[i] is ')'

     If s[i-1] is '(', longest[i] = longest[i-2] + 2

     Else if s[i-1] is ')' and s[i-longest[i-1]-1] == '(', longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]

For example, input "()(())", at i = 5, longest array is [0,2,0,0,2,0], longest[5] = longest[4] + 2 + longest[1] = 6.


   int longestValidParentheses(string s) {
            if(s.length() <= 1) return 0;
            int curMax = 0;
            vector<int> longest(s.size(),0);
            for(int i=1; i < s.length(); i++){
                if(s[i] == ')'){
                    if(s[i-1] == '('){
                        longest[i] = (i-2) >= 0 ? (longest[i-2] + 2) : 2;
                        curMax = max(longest[i],curMax);
                    }
                    else{ // if s[i-1] == ')', combine the previous length.
                        if(i-longest[i-1]-1 >= 0 && s[i-longest[i-1]-1] == '('){
                            longest[i] = longest[i-1] + 2 + ((i-longest[i-1]-2 >= 0)?longest[i-longest[i-1]-2]:0);
                            curMax = max(longest[i],curMax);
                        }
                    }
                }
                //else if s[i] == '(', skip it, because longest[i] must be 0
            }
            return curMax;
        }
Updated: thanks to Philip0116, I have a more concise solution(though this is not as readable as the above one, but concise):

int longestValidParentheses(string s) {
        if(s.length() <= 1) return 0;
        int curMax = 0;
        vector<int> longest(s.size(),0);
        for(int i=1; i < s.length(); i++){
            if(s[i] == ')' && i-longest[i-1]-1 >= 0 && s[i-longest[i-1]-1] == '('){
                    longest[i] = +longest[i-1] + 2 + ((i-longest[i-1]-2 >= 0)?longest[i-longest[i-1]-2]:0);
                    curMax = max(longest[i],curMax);
            }
        }
        return curMax;
    }
 
    def longestValidParenthesesMyBad(self, s):
        """
        :type s: str
        :rtype: int
        """
        if   len(s) <= 1:
            return 0
        dp = [0] * len(s)
        
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(': 
                    dp[i] = 2 + (dp[i-2] if i >= 2 else 0)
                else:
                    if i -dp[i-1] > 0:
                        if s[i-dp[i-1]-1] == '(': # #Mistake this will output 4: "())"
                            dp[i] = 2 + dp[i-1] + dp[i-dp[i-1]-2]
                        else:
                            dp[i] = dp[i-dp[i-1]] + dp[i-1]
                    else: dp[i] = dp[i-1]
        return dp[len(s)-1]