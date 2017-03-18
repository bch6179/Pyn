class Solution:
    # @return a list of lists of integers
    def pascalstriangle(self, numRows):
        list = [[] for i in range(numRows)]
        # for i in range(numRows):
        #     list[i] = [1 for j in range(i+1)]
        for i in range(0,numRows):
            list[i] = [1 for j in range(i+1)]
            for j in range(1, i):
                list[i][j] = list[i-1][j-1] + list[i-1][j]
        return list
    def pascalstriangle2(self, numRows):
        res = []
        for i in range(numRows):
            list = []
            list.append(1)
            for j in range(1, i):
                list.append(res[i-1][j-1]+res[i-1][j])
            if (numRows > 1): list.append(1)
            res.append(list)
        return res


    def pascalstriangleII(self, numRows):
        prev = []
        for i in range(numRows):
            list = []
            list.append(1)
            for j in range(1, i):
                list.append(prev[j-1]+prev[j])
            if (numRows > 1): list.append(1)
            prev = list
        return list

    def pascalstriangleII2(self, numRows):
        list = []
        for i in range(numRows):
            list.append(1)
            for j in range(i-1, 0, -1):
                list[j] = list[j] + list[j-1]
            
        return list
s = Solution() 
print s.pascalstriangleII2(4)