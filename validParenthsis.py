class Solution:
    # @return a boolean
    class Solution(object):
    # @return a boolean
    def isValid(self, s):
        brackets = {"{":"}", "[":"]", "(":")"}
        stack = []
        
        for ch in s:
            if ch in brackets:
                stack.append(ch)
            else:
                if not stack: return False
                pair = stack.pop()
                if brackets[pair] != ch:
                    return False
        return not stack
    def isValid(self, s):
        brackets = {"{":"}", "[":"]", "(":")"}
        stack = []
        
        for ch in s:
            if ch == "{}" or ch == "[]"
                stack.append(ch)
            else:
                if not stack: return False
                pair = stack.pop()
                if ch == "}" and "{" != pair or ch == "]" and "[]" != pair:
                    return False
        return not stack
    def isValid(self, s):
        brackets = {"{":"}", "[":"]", "(":")"}
        stack = []
        for i in range(0, len(s)):
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                if brackets[stack[len(stack)-1]] != s[i]:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False

    def isValid_MAP(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #()[)]{}
        #must pair immediately [ ( ] ) asking what are not valid, all consider all
        #must pair in total number
        #must left first
        #have push pop sounds like stack, see if can autocancelling by more rule
        invalidStartSet = [')', ']', '}']
        prenPairs = {')':'(', ']':'[', '}':'{'}
        map = {} #orderedDict()
        for ch in s:
            if ch in invalidStartSet:
                pair =prenPairs[ch]
                if pair not in map:
                    return False
                else: 
                    map[pair] -= 1
                    if  map[pair] == 0:
                        map.delete(pair)
            else:
                if ch not in map: map[ch] = 1
                else: map[ch] += 1
        return len(map) == 0