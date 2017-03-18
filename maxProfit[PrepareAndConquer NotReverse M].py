class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1: return 0
        
        minprice = prices[0]
        ml = [0 for i in range(len(prices))]
        for  i in range(1, len(prices)):
            ml[i] = max(ml[i-1], prices[i] - minprice)
            minprice = min(prices[i], minprice)
        
        mr = [0 for i in range(len(prices))]
        maxGlobal = 0
        maxprice = prices[-1]
        for j in range(len(prices)-2, -1, -1):
            mr[j] = max(mr[j+1],  maxprice-prices[j]) #bad mr[j] = max(mr[j-1],
            maxprice = max(prices[j], maxprice)
        for i in range(len(prices)):
            maxGlobal = max(maxGlobal, mr[i]+ml[i])
        return maxGlobal
            