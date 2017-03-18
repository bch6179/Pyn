 Mini Parser
Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.
Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.
#Mistake
#Mistake# 

#Mistake 
integer is added N()
For each [, create a new N() as Cur 
for , check not after a ], check edge cases


# An Java Iterative Solution
This approach will just iterate through every 
char in the string (no recursion).

If encounters '[', push current NestedInteger to stack and start a new one.
If encounters ']', end current NestedInteger and pop a NestedInteger from stack to continue.
If encounters ',', append a new number to curr NestedInteger, if this comma is not right after a brackets.
Update index l and r, where l shall point to the start of a integer substring, while r shall points to the end+1 of substring.
Java Code:

public NestedInteger deserialize(String s) {
    if (s.isEmpty())
        return null;
    if (s.charAt(0) != '[') // ERROR: special case
        return new NestedInteger(Integer.valueOf(s));
        
    Stack<NestedInteger> stack = new Stack<>();
    NestedInteger curr = null;
    int l = 0; // l shall point to the start of a number substring; 
               // r shall point to the end+1 of a number substring
    for (int r = 0; r < s.length(); r++) {
        char ch = s.charAt(r);
        if (ch == '[') {
            if (curr != null) {
                stack.push(curr);
            }
            curr = new NestedInteger();
            l = r+1;
        } else if (ch == ']') {
            String num = s.substring(l, r);
            if (!num.isEmpty())
                curr.add(new NestedInteger(Integer.valueOf(num)));
            if (!stack.isEmpty()) {
                NestedInteger pop = stack.pop();
                pop.add(curr);
                curr = pop;
            }
            l = r+1;
        } else if (ch == ',') {
            if (s.charAt(r-1) != ']') {
                String num = s.substring(l, r);
                curr.add(new NestedInteger(Integer.valueOf(num)));
            }
            l = r+1;
        }
    }
    
    return curr;
}


//eval() interprets a string as code
def deserialize(self, s):
    def nestedInteger(x):
        if isinstance(x, int):
            return NestedInteger(x)
        lst = NestedInteger()
        for y in x:
            lst.add(nestedInteger(y))
        return lst
    return nestedInteger(eval(s))
Python one-liner
def deserialize(self, s):
    return NestedInteger(s) if isinstance(s, int) else reduce(lambda a, x: a.add(self.deserialize(x)) or a, s, NestedInteger()) if isinstance(s, list) else self.deserialize(eval(s))

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if s[0] != '[':
            return NestedInteger(int(s))
        nested = NestedInteger()
        numP, start = 0, 1
        for i in range(1, len(s)):
            if (numP == 0 and s[i] == ',') or i == len(s) - 1:
                # make sure it is not an empty string
                if start < i:
                    nested.add(self.deserialize(s[start:i]))
                start = i + 1
            elif s[i] == '[':
                numP += 1
            elif s[i] == ']':
                numP -= 1
        return nested
I was a bit confused by add() and setInteger() both for adding integer element. I think add() can do what setInteger does.

Please note that this is not a very fast solution since it requires scanning elements multiple times according to this element's depth.

Using stack would use space as a trade-off for multiple scanning.

My stack solution, as many people have similar solutions:

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        stack, start = [], -1
        for i, c in enumerate(s):
            if c == '[':
                stack.append(NestedInteger())
            elif c == ']':
                # for last ], it is possible that there is only one NestedInteger
                if len(stack) > 1:
                    t = stack.pop()
                    stack[-1].add(t)
            elif c.isdigit() or c == '-':
                if start == -1:
                    start = i
                if i == len(s) - 1 or not s[i + 1].isdigit():
                    if stack:
                        stack[-1].add(NestedInteger(int(s[start:i + 1])))
                    else:
                        stack.append(NestedInteger(int(s[start:i + 1])))
                    start = -1
        return stack.pop()

        The problem comes to recursion is to identify what is one NestedInteger element. I used numP to balance the number of parentheses to get the actual NestedInteger element for my current level, then leave this element to next recursion level.