Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"


From here we can easily fill the whole grid: for each (x, y), we check if S[x] == T[y] we add the previous item and the previous item in the previous row, otherwise we copy the previous item in the same row. The reason is simple:

if the current character in S doesn't equal to current character T, then we have the same number of distinct subsequences as we had without the new character.
if the current character in S equal to the current character T, then the distinct number of subsequences: the number we had before plus the distinct number of subsequences we had with less longer T and less longer S.
An example:
S: [acdabefbc] and T: [ab]



first we check with a:

           *  *
      S = [acdabefbc]
mem[1] = [0111222222]
then we check with ab:

               *  * ]
      S = [acdabefbc]
mem[1] = [0111222222]
mem[2] = [0000022244]
And the result is 4, as the distinct subsequences are:

      S = [a   b    ]
      S = [a      b ]
      S = [   ab    ]
      S = [   a   b ]


state: f[i][j] first i of S choose first j of T
 • function: f[i][j] = f[i - 1][j] + f[i - 1][j - 1]  // S[i-1] == T[j-1],means current b useful,so remove privious  b to see how many+
  •                     = f[i - 1][j]         //  S[i-1] != T[j-1] remove 
  
   • initialize: f[i][0] = 1, f[0][j] = 0 (j > 0) • answer: f[n][m] (n = sizeof(S), m = sizeof(T))
 

# O(m*n) space 
def numDistinct1(self, s, t):
    l1, l2 = len(s)+1, len(t)+1
    dp = [[1] * l2 for _ in xrange(l1)]
    for j in xrange(1, l2):
        dp[0][j] = 0
    for i in xrange(1, l1):
        for j in xrange(1, l2):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*(s[i-1] == t[j-1]) #Mistake on dp[i][j-1]
    return dp[-1][-1]
  
# O(n) space  
def numDistinct(self, s, t):
    l1, l2 = len(s)+1, len(t)+1
    cur = [0] * l2
    cur[0] = 1
    for i in xrange(1, l1):
        pre = cur[:]
        for j in xrange(1, l2):
            cur[j] = pre[j] + pre[j-1]*(s[i-1] == t[j-1])
    return cur[-1]
