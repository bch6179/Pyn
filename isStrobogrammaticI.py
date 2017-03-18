def isStrobogrammatic(self, num):
    return all(num[i] + num[~i] in '696 00 11 88' for i in range(len(num)/2+1))