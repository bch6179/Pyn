class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for c in tokens:
            if c not in ["+", "-", "*", "/"]:#c.lstrip('+-').isdigit():
                stack.append(int(c))
            else:
                r = stack.pop() #Mistake pull this ahead to share, and meaning ful name
                l = stack.pop()
                if c == "+":
                     stack.append(l+r)
                elif c == "-":
                 
                    stack.append(l-r)
                elif c == "*":
                    stack.append(l*r)
                elif c == "/":
                    if l*r < 0 and l % r != 0:
                        stack.append(l/r+1)
                    else:
                        stack.append(l/r)
                    #stack.append(  num2/num1 + (1 if (num1 * num2 < 0 and num1 % num2 !=0)  else 0))
                    # -4/2, -1/10  #Mistake order or /, and () for if else
                    #Mistake divide by zero, two pops() has no order, check keys 2-3 related possible mistake could make
        return stack.pop()
                    # "1" "1" "+"  # 0, 1, /
s = Solution() 
print s.evalRPN(["4","-2","/","2","-3","-","-"])
print s.evalRPN(["4","13","5","/","+"])
print s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print s.evalRPN(["3","-4","+"])