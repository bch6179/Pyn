class NestedInteger(object):
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """
   def __repr__(self):
        return """NestedInteger(val=%r, next=%r""" % (self.val, self.next)
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
   def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if not s: return None
        if s[0] != '[':return NestedInteger(int(s))
        stack = []
        res = NestedInteger()
        start = -1
        for i in range(1, len(s)):
            if s[i] == '[':
                stack.append(res)
                res = NestedInteger()
            
            elif s[i].isdigit() or s[i] == '-': #consider -1
                if start == -1:
                    start = i
                if i == len(s)-1 or not s[i+1].isdigit():  #mistake should not use elif : [1,2,3]
                    res.add(NestedInteger(int(s[start:i+1]))) #mistake should be i+1 , not i
                    start = -1
            elif s[i] == ']':
                if stack: # consider [] 
                    ores = stack.pop()
                    ores.add(res)
                    res = ores
        return res

s = Solution() 
print s.deserialize("[123,[24,5,6]]")