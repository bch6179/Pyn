class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        w = ''
        res = ''
        stack = []
        for i in range(1, len(path)):
            c = path[i]
            if c != '/':
                w = w+c
             
            if  c == '/' or i == len(path)-1:
                if w == '' or w =='.' or w.isspace():  
                    w = '' #Mistake other wise . adding to next one
                    continue
                if w == '..':
                    if stack:  #Mistake not else if
                        stack.pop() #Line 15: IndexError: pop from empty list
                else:     
                #"/..hidden" #w.isalnum() or w == '...': 
                    stack.append(w)
                w = ''
              
        if stack == []: #or not stack
            return "/"
        
        while stack:
            res = '/' + stack.pop() + res
        
        return res
s = Solution() 
print s.simplifyPath("/home/foo/./bar")
print s.simplifyPath("/.../")
print s.simplifyPath("/a/./b/../../c/")
print s.simplifyPath("/../")
print s.simplifyPath("///")

    # def simplifyPath(self, path):
    #     places = [p for p in path.split("/") if p!="." and p!=""]
    #     stack = []
    #     for p in places:
    #         if p == "..":
    #             if len(stack) > 0:
    #                 stack.pop()
    #         else:
    #             stack.append(p)
    #     return "/" + "/".join(stack)