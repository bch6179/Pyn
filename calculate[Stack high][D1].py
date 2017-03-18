

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        sign = 1
        stack = []
        num = 0
        for i in xrange(len(s)):
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord('0')
            
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if s[i] == '+':
                    res += num*sign
                    sign = 1
                elif s[i] == '-':
                    res += num*sign
                    sign = -1
                elif s[i] == '(':
                    stack.append(res)
                    stack.append(sign)
                    res = 0
                    sign = 1
                elif s[i] == ')':
                    res += num*sign#Mistake  not save 1 to res, extend a bit termination sign, and consider any other similar changing points, (1)  
                    sign = 1
                    sign = stack.pop()
                    res = stack.pop() + res* sign
                else:
                    res += num*sign
                num = 0

        return res
s = Solution() 
print s.calculate("(1)")
#(12-((2+3)-(5+4)))