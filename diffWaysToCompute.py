Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
    

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def calc(op, a, b):
            if op == '+':
                return a+b
            elif op == '-':
                return a-b
            elif op == '*':
                return a*b
            else:
                return 0
                
        if input.isdigit():
            return [int(input)]
            
        res = []
        for i, c in enumerate(input):
            if c in '+-*':
                for a in self.diffWaysToCompute(input[:i]):
                    for b in self.diffWaysToCompute(input[i+1:]):
                        res.append(calc(c,  a , b) )
        return res
    
def diffWaysToCompute(self, input):
    if input.isdigit():
        return [int(input)]
    res = []        
    for i in xrange(len(input)):
        if input[i] in "-+*":
            res1 = self.diffWaysToCompute(input[:i])
            res2 = self.diffWaysToCompute(input[i+1:])
            res += [eval(str(k)+input[i]+str(j)) for k in res1 for j in res2]            
    return res
                