
import sys
class Solution(object):
    def getMoneyAmount(self, n):
        def dfs(n, i, j):
            if n <= 1:
                return 0 
        
            if i >= j: 
                return 0 
                
            if DP[i][j] != -1:
                return DP[i][j]
            
            gMin =sys.maxsize
            for k in range(i+1, j): # 1 3 2 , 2:5
                localMax = k + max(dfs(n, i, k-1), dfs(n, k+1, j))
                gMin = min(gMin, localMax)
                
            DP[i][j] = i if i+1 == j else gMin
            return DP[i][j] #Mistake not DP[i,j]
                 
        DP = [[-1 for i in range(n+1)] for j in range(n+1)] 
        return dfs(n, 1, n) #Mistake  forgot return
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [[0 for i in range(n+1)] for j in range(n+1)]
        for j in range(2, n+1): #Mistake use for in stead of while
            for i in range(j-1, 0, -1): # i 1, 2:1, 3:2:1
                gMin = sys.maxsize
                for k in range(i+1, j): # i = 1 ,skip this loop, i: =2, j=3 ,skip, i=1, j=3, k= 2; 3:4, i=2, j=4; i=1, j=4; 
                    localMax = k+ max(table[i][k-1],  table[k+1][j])
                    gMin = min(gMin, localMax)
                table[i][j] = i if i+1==j else gMin
        return table[1][n]



public class Solution {
    public int getMoneyAmount(int n) {
        int[][] table = new int[n+1][n+1];
        return DP(table, 1, n);
    }
    
    int DP(int[][] t, int s, int e){
        if(s >= e) return 0;
        if(t[s][e] != 0) return t[s][e];
        int res = Integer.MAX_VALUE;
        for(int x=s; x<=e; x++){
            int tmp = x + Math.max(DP(t, s, x-1), DP(t, x+1, e));
            res = Math.min(res, tmp);
        }
        t[s][e] = res;
        return res;
    }
}
Here is a bottom up solution.

public class Solution {
    public int getMoneyAmount(int n) {
        int[][] table = new int[n+1][n+1];
        for(int j=2; j<=n; j++){
            for(int i=j-1; i>0; i--){
                int globalMin = Integer.MAX_VALUE;
                for(int k=i+1; k<j; k++){
                    int localMax = k + Math.max(table[i][k-1], table[k+1][j]);
                    globalMin = Math.min(globalMin, localMax);
                }
                table[i][j] = i+1==j?i:globalMin;
            }
        }
        return table[1][n];
    }
}

this difference from a tree structure. The solution structure is actually a binary recursion tree: For t[1][15], the root is 12. left child is rooted t[1][11] and right child is rooted at t[13][15]. However, for t[101][115], the cost of this structure is no longer optimal, because the left tree has more levels, and for each level, you need to add an additional cost 100 to the subroot, which makes the cost in left subtree much larger than the right subtree.

he bottom-up approach is nice. Could you explain why we need to check i+1==j? Thanks

4 months ago reply quote 
3
F Free9   @dukeforever
Reputation:  30
@dukeforever It would be the case that you only have two coins to choose from. For example [5, 6], are you going to choose 5 or 6? Obviously you will choose 5, since it is smaller. That's why when i + 1 == j, dp[i][j] = i.


a typical AI MinMax problem, https://en.wikipedia.org/wiki/Minimax illustrates it really well. And I think the recursive way is more straightforward:

int[][] dp;
public int getMoneyAmount(int n) {
    dp = new int[n+1][n+1];
    return getMoneyAmount(1, n);
}
It is the case that whether we could choose from two consecutive number or multiple numbers.

Two consectuive number i + 1 == j
For example, dp[1][2] is the case that you can only choose from 1 and 2. Obviously you will choose the smaller number since you want to minimize the loss.

Multiple numbers, range i - j
In this case, we assign globalMin to dp[i][j] since globalMin is the minimum loss we got so far.
private int getMoneyAmount(int lower, int upper) {
    if (lower >= upper) {
        return 0;
    }
    if (dp[lower][upper] != 0) {
        return dp[lower][upper];
    }
    
    int maximum = Integer.MAX_VALUE;
    for (int i = lower; i <= upper; i++) {
        maximum = Math.min(maximum, Math.max(getMoneyAmount(lower, i-1), getMoneyAmount(i+1, upper)) + i);
    }
    dp[lower][upper] = maximum;
    
    return maximum;
}