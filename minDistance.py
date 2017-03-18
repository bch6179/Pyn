class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # know deletion the first a for aab , ab after drawing metrics, but don't know how to relate to the DP equation, actually [i-1] [j-1]
        if word1 == word2: return 0
        
        DP = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        
        for j in range(len(word2)+1):
            DP[0][j] = j
        for i in range(len(word1)+1):
            DP[i][0] = i
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]: #Mistake word index overflow
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = min(DP[i-1][j-1], DP[i][j-1], DP[i-1][j])+1
        return DP[len(word1)][len(word2)]

# Well, you may have noticed that each time when we update dp[i][j], we only need dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]. In fact, we need not maintain the full m*n matrix. Instead, maintaing one column is enough. The code can be optimized to O(m) or O(n) space, depending on whether you maintain a row or a column of the original matrix.

# The optimized code is as follows.

# class Solution { 
# public:
#     int minDistance(string word1, string word2) {
#         int m = word1.length(), n = word2.length();
#         vector<int> cur(m + 1, 0);
#         for (int i = 1; i <= m; i++)
#             cur[i] = i;
#         for (int j = 1; j <= n; j++) {
#             int pre = cur[0];
#             cur[0] = j;
#             for (int i = 1; i <= m; i++) {
#                 int temp = cur[i];
#                 if (word1[i - 1] == word2[j - 1])
#                     cur[i] = pre;
#                 else cur[i] = min(pre + 1, min(cur[i] + 1, cur[i - 1] + 1));
#                 pre = temp;
#             }
#         }
#         return cur[m]; 
#     }
# }; 
# Well, if you find the above code hard to understand, you may first try to write a two-column version that explicitly maintains two columns (the previous column and the current column) and then simplify the two-column version into the one-column version like the above code :-)