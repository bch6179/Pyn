class Solution(object):
 
    def maximalSquare1(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """ 
        res = 0 
        prev ,cur= [0]*len(matrix),[0]*len(matrix)

        if not matrix or not matrix[0]: return 0
        for i in range(len(matrix)):
            prev[i] = ord(matrix[i][0])-ord('0')
            res = max(res, prev[i]) #not forgot edge case
            
        for j in range(1, len(matrix[0])): #col
            cur[0] = ord(matrix[0][j])-ord('0')    #Mistake maxtrix is char
            res = max(res, cur[0])   #Mistake '01' need to return 1 
            for i in range(1, len(matrix)):
                if matrix[i][j] == '1': 
                    cur[i] = min(cur[i-1], prev[i],prev[i-1])+1  #   current cell i,j max square since 0 0
                    res = max(res, cur[i])  
            #Mistake
            prev = cur #Mistake pre : prev
            cur = [0]*len(matrix)         
        return res*res    
  
    def __init__(self):
        self.res = 0
        
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
          
            self.res = max(1, self.res)
            
            k = 1
            while k+i < len(matrix) and k+j < len(matrix[0]):
                for m in range(i, k+i+1):
                    if matrix[m][k+j] == '0':
                        return
                for n in range(j, k+j+1):
                    if matrix[k+i][n] == '0':
                        return
                self.res = max(self.res, (k+1)*(k+1))
                k+=1
          
            
        if not matrix or not matrix[0]: return 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                if matrix[i][j] == '1':
                    dfs(i, j)
        return self.res
s = Solution() 
print s.maximalSquare(["1111","1111","1111"])
#print s.maximalSquare(["01"])