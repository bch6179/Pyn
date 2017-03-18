Solution(object):
    def printZigZagMatrix(self, A):
        n,m = len(A), len(A[0])
        x,y=0,0
        
        x = []
        for i in range(n+m):
            if i % 2 == 0:
                x = i
                while x >= 0:
                    if  x <= m and (i-x) <= n:
                        res.append(A[x][i-x])
                    x -= 1
            else:
                x = i
                while x <= m:
                    if x <= m and (i-x) <= n:
                        res.append( A[x][i-x] )
                    x += 1
        return res

    def printZMatrix(self, matrix):
        if len(matrix) == 0:
            return []
            
        x, y = 0, 0
        n, m = len(matrix), len(matrix[0])
        rows, cols = range(n), range(m)
        
        dx = [1, -1]
        dy = [-1, 1]
        direct = 1
        
        result = []
        for i in xrange(len(matrix) * len(matrix[0])):
            result.append(matrix[x][y])
            
            nextX = x + dx[direct]
            nextY = y + dy[direct]
            if nextX not in rows or nextY not in cols:
                if direct == 1:
                    if nextY >= m:
                        nextX, nextY = x + 1, y
                    else:
                        nextX, nextY = x, y + 1
                else:
                    if nextX >= n:
                        nextX, nextY = x, y + 1
                    else:
                        nextX, nextY = x + 1, y
                direct = 1 - direct
            x, y = nextX, nextY
        return result
        

