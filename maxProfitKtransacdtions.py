
#[Note]
#=====DP+ Greedy

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/?tab=Description

# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most k transactions.

def maxProfit4(self, k, prices):
    n = len(prices)
    if n < 2:
        return 0
    # k is big enougth to cover all ramps.
    if k >= n / 2:
        return sum(i - j
                   for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
    globalMax = [[0] * n for _ in xrange(k + 1)]
    for i in xrange(1, k + 1):
        # The max profit with i transations and selling stock on day j.
        localMax = [0] * n
        for j in xrange(1, n):
            profit = prices[j] - prices[j - 1]
            localMax[j] = max(
                # We have made max profit with (i - 1) transations in
                # (j - 1) days.
                # For the last transation, we buy stock on day (j - 1)
                # and sell it on day j.
                globalMax[i - 1][j - 1] + profit,
                # We have made max profit with (i - 1) transations in
                # (j - 1) days.
                # For the last transation, we buy stock on day j and
                # sell it on the same day, so we have 0 profit, apparently
                # we do not have to add it.
                globalMax[i - 1][j - 1],  # + 0,
                # We have made profit in (j - 1) days.
                # We want to cancel the day (j - 1) sale and sell it on
                # day j.
                localMax[j - 1] + profit)
            globalMax[i][j] = max(globalMax[i][j - 1], localMax[j])
    return globalMax[k][-1]

	def maxProfit(self, k, prices):
        if not prices:
        return 0
    
    n = len(prices)
    if k >= n // 2:
        return sum(
            x - y
            for x, y in zip(prices[1:], prices[:-1])
            if x > y)
    
    profits = [0] * n
    for i in range(k):
        # Update new_profits
        max_all = max_prev = max_here = 0
        for j in range(1, n):
            profit = prices[j] - prices[j-1]
            max_here = max(max_here + profit, max_prev + profit, max_prev)
            max_prev = profits[j]
            profits[j] = max_all = max(max_all, max_here)
    return profits[-1]

/**
 * dp[i, j] represents the max profit up until prices[j] using at most i transactions. 
 * dp[i, j] = max(dp[i, j-1], prices[j] - prices[jj] + dp[i-1, jj]) { jj in range of [0, j-1] }
 *          = max(dp[i, j-1], prices[j] + max(dp[i-1, jj] - prices[jj]))
 * dp[0, j] = 0; 0 transactions makes 0 profit
 * dp[i, 0] = 0; if there is only one price data point you can't make any transaction.
 */

public int maxProfit(int k, int[] prices) {
	int n = prices.length;
	if (n <= 1)
		return 0;
	
	//if k >= n/2, then you can make maximum number of transactions.
	if (k >=  n/2) {
		int maxPro = 0;
		for (int i = 1; i < n; i++) {
			if (prices[i] > prices[i-1])
				maxPro += prices[i] - prices[i-1];
		}
		return maxPro;
	}
	
    int[][] dp = new int[k+1][n];
    for (int i = 1; i <= k; i++) {
    	int localMax = dp[i-1][0] - prices[0];
    	for (int j = 1; j < n; j++) {
    		dp[i][j] = Math.max(dp[i][j-1],  prices[j] + localMax);
    		localMax = Math.max(localMax, dp[i-1][j] - prices[j]);
    	}
    }
    return dp[k][n-1];
}

you don't really need localMax[], use single variable instead. Since localMax[j] only depend on local localMax[j-1], the one before.