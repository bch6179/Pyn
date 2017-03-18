87. Scramble String
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Subscribe to see which companies asked this question
ssume the strings are all lower case letters


def isScramble(self, s1, s2):
    n, m = len(s1), len(s2)
    if n != m or sorted(s1) != sorted(s2):
        return False
    if n < 4 or s1 == s2:
        return True
    f = self.isScramble
    for i in range(1, n):
        if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \
           f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
            return True
    return False
    
class Solution {
public:
    bool isScramble(string s1, string s2) {
        if(s1==s2)
            return true;
            
        int len = s1.length();
        int count[26] = {0};
        for(int i=0; i<len; i++)
        {
            count[s1[i]-'a']++;
            count[s2[i]-'a']--;
        }
        
        for(int i=0; i<26; i++)
        {
            if(count[i]!=0)
                return false;
        }
        
        for(int i=1; i<=len-1; i++)
        {
            if( isScramble(s1.substr(0,i), s2.substr(0,i)) && isScramble(s1.substr(i), s2.substr(i)))
                return true;
            if( isScramble(s1.substr(0,i), s2.substr(len-i)) && isScramble(s1.substr(i), s2.substr(0,len-i)))
                return true;
        }
        return false;
    }
};

My C++ solutions (recursion with cache , DP, recursion with cache and pruning) with explanation (4ms)
The basic idea is to divide s1(s2) into two substrings with length k and len-k and check if the two substrings s1[0..k-1] and s1[k, len-1] are the scrambles of s2[0..k-1] and s2[k,len-1] or s2[len-k, len-1] and s2[0..len-k-1] via recursion. The straigtforward recursion will be very slow due to many repeated recursive function calls. To speed up the recursion, we can use an unordered_map isScramblePair to save intermediate results. The key used here is s1+s2, but other keys are also possible (e.g. using indices)

    class Solution {
        bool DP_helper(unordered_map<string, bool> &isScramblePair, string s1, string s2)
        {
            int i,len = s1.size();
            bool res = false;
            if(0==len) return true;
            else if(1==len) return s1 == s2;
            else
            {
                if(isScramblePair.count(s1+s2)) return isScramblePair[s1+s2]; // checked before, return intermediate result directly
                if(s1==s2) res=true;
                else{
                    for(i=1; i<len && !res; ++i)
                    {
//check s1[0..i-1] with s2[0..i-1] and s1[i..len-1] and s2[i..len-1]
                        res = res || (DP_helper(isScramblePair, s1.substr(0,i), s2.substr(0,i)) && DP_helper(isScramblePair, s1.substr(i,len-i), s2.substr(i,len-i)));
 //if no match, then check s1[0..i-1] with s2[len-k.. len-1] and s1[i..len-1] and s2[0..len-i]
                       res = res || (DP_helper(isScramblePair, s1.substr(0,i), s2.substr(len-i,i)) && DP_helper(isScramblePair, s1.substr(i,len-i), s2.substr(0,len-i)));
                    }
                }
                return isScramblePair[s1+s2]= res; //save the intermediate results
                
            }
        }
    public:
        bool isScramble(string s1, string s2) {
           unordered_map<string, bool> isScramblePair;
           return DP_helper(isScramblePair, s1, s2);
        }
    };
The recursive version has exponential complexity. To further improve the performance, we can use bottom-up DP, which is O(N^4) complexity. Here we build a table isS[len][i][j], which indicates whether s1[i..i+len-1] is a scramble of s2[j..j+len-1].

class Solution {
public:
    bool isScramble(string s1, string s2) {
        int sSize = s1.size(), len, i, j, k;
        if(0==sSize) return true;
        if(1==sSize) return s1==s2;
        bool isS[sSize+1][sSize][sSize];

        for(i=0; i<sSize; ++i)
            for(j=0; j<sSize; ++j)
                isS[1][i][j] = s1[i] == s2[j];
                
        for(len=2; len <=sSize; ++len)
            for(i=0; i<=sSize-len; ++i)
                for(j=0; j<=sSize-len; ++j)
                {
                    isS[len][i][j] = false;
                        for(k=1; k<len && !isS[len][i][j]; ++k)
                        {
                            isS[len][i][j] = isS[len][i][j] || (isS[k][i][j] && isS[len-k][i+k][j+k]);
                            isS[len][i][j] = isS[len][i][j] || (isS[k][i+len-k][j] && isS[len-k][i][j+k]);
                        }
                }
        return isS[sSize][0][0];            

    }
}; 
Furhtermore, in many cases, we found we can terminate our recursion early by pruning: i.e. by first checking if s1 and s2 have the same character set before we do recursion: if not, just terminate without recursion. This observation leads us to the following Recursion+cache+pruning version. Here the key of the cache changes to idx1sSize +idx2 + lensSize*sSize;

class Solution {
private:
    bool DP_helper(string &s1, string &s2, int idx1, int idx2, int len, char isS[])
    {
        int sSize = s1.size(),i, j, k, hist[26] , zero_count =0;
        if(isS[(len*sSize+idx1)*sSize+idx2]) return isS[(len*sSize+idx1)*sSize+idx2]==1;
        bool res = false;
        
        fill_n(hist, 26, 0);
        for(k=0; k<len;++k)
        { // check if s1[idx1:idx1+len-1] and s2[idx2:idx2+len-1] have same characters
            zero_count +=  (0==hist[s1[idx1+k]-'a']) - (0== ++hist[s1[idx1+k]-'a']);
            zero_count +=  (0==hist[s2[idx2+k]-'a']) - (0== --hist[s2[idx2+k]-'a']);
        }
        if(zero_count) {isS[(len*sSize+idx1)*sSize+idx2] = 2; return false;} //if not, return directly
        if(len==1)     {isS[(len*sSize+idx1)*sSize+idx2] = 1; return true;}
        for(k=1;k<len && !res;++k) //otherwise, recursion with cache
        {
            res = res || (DP_helper(s1, s2, idx1, idx2, k, isS) && DP_helper(s1, s2, idx1+k, idx2+k, len-k, isS) );
            res = res || (DP_helper(s1, s2, idx1+len-k, idx2, k, isS) && DP_helper(s1, s2, idx1, idx2+k, len-k, isS) );
        }
        isS[(len*sSize+idx1)*sSize+idx2] = res?1:2;
        return res;
    }
public:
    bool isScramble(string s1, string s2) {
        const int sSize = s1.size();
        if(0==sSize) return true;
        char isS[(sSize+1)*sSize*sSize];
        fill_n(isS, (sSize+1)*sSize*sSize, 0);
        return DP_helper(s1, s2, 0, 0, sSize, isS);
    }
};