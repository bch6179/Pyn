class Solution(object):
    def maxProduct(self, A):
        MinTemp = A[0]
        MaxTemp = A[0]
        Max = A[0]
        for i in xrange(1, len(A)):
            MaxTemp, MinTemp  = max(A[i], A[i] * MaxTemp, A[i] * MinTemp), min(A[i], A[i] * MaxTemp, A[i] * MinTemp)
            Max = max(Max, MaxTemp)

         # 2 -3 4  #Mistake -2 * 3 = -6 maintain min