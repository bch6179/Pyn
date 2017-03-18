class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
         
        up, left = 0, 0
        down, right = n - 1, n - 1
        res = [[0 for i in range(n)] for j in range(n)]
        direct,count = 0,0
        
        while True:   # Mistake for i in range(n*n):
            if direct == 0:
                for j in range(left, right+1):
                    count += 1; res[up][j] = count      # Mistake     count start from 1          
                up += 1          
            elif direct == 1:
                for j in range(up, down+1):
                    count += 1;res[j][right] = count
                 
                right -= 1
            
            elif direct == 2:
                for j in range(right, left-1, -1):
                    count += 1;res[down][j] = count
                    
                down -= 1
            
            elif direct == 3:
                for j in range(down, up-1, -1):
                    count += 1;res[j][left] = count
                    
                left+=1
            
            if up > down or left > right:
                break
        
            direct= (direct + 1) % 4
            
        return res
s = Solution()
print(s.generateMatrix(3))       
        
                