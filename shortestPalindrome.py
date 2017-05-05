https://leetcode.com/problems/shortest-palindrome/#/description

Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".


KMP apply to this: 相当于在除去字符D(the first difference)的模式串子串中寻找相同的前缀和后缀，然后根据前缀后缀求出next 数组，最后基于next 数组进行匹配. by getting next tables,so we always get the max matching prefix and sufix, while we extending the end to the left of the merged abc#cba; if the last char not matching its next is 0; for each i as the last end, get the next table and DP

KMP:
①寻找前缀后缀最长公共元素长度
对于P = p0 p1 ...pj-1 pj，寻找模式串P中长度最大且相等的前缀和后缀。如果存在p0 p1 ...pk-1 pk = pj- k pj-k+1...pj-1 pj，那么在包含pj的模式串中有最大长度为k+1的相同前缀后缀。举个例子，如果给定的模式串为“abab”，那么它的各个子串的前缀后缀的公共元素的最大长度如下表格所示：

比如对于字符串aba来说，它有长度为1的相同前缀后缀a；而对于字符串abab来说，它有长度为2的相同前缀后缀ab（相同前缀后缀的长度为k + 1，k + 1 = 2）。
②求next数组
next 数组考虑的是除当前字符外的最长相同前缀后缀，所以通过第①步骤求得各个前缀后缀的公共元素的最大长度后，只要稍作变形即可：将第①步骤中求得的值整体右移一位，然后初值赋为-1，如下表格所示：

比如对于aba来说，第3个字符a之前的字符串ab中有长度为0的相同前缀后缀，所以第3个字符a对应的next值为0；而对于abab来说，第4个字符b之前的字符串aba中有长度为1的相同前缀后缀a，所以第4个字符b对应的next值为1（相同前缀后缀的长度为k，k = 1）。

3)根据next数组进行匹配
匹配失配，j = next [j]，模式串向右移动的位数为：j - next[j]。

class Solution(object):
    def shortestPalindrome(self, s):
        def isP(s, lo, hi):
            while lo<hi:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
            return True
        for i in range(len(s), -1, -1):
            if isP(s, 0, i-1):
                return s[i:][::-1] + s

def shortestPalindrome(self, s):
    r = s[::-1]
    for i in range(len(s) + 1):
        if s.startswith(r[i:]):
            return r[:i] + s
Example: s = dedcba. Then r = abcded and I try these overlays (the part in (...) is the prefix I cut off, I just include it in the display for better understanding):

  s          dedcba
  r[0:]      abcded    Nope...
  r[1:]   (a)bcded     Nope...
  r[2:]  (ab)cded      Nope...
  r[3:] (abc)ded       Yes! Return abc + dedcba
bab bab
bbdde eddbb
mimissisisip #  dsisip
aacecaaa  aaacecaa

aaacecaaa"

abc dedcba abcded

adcedcba
abdedcba
abcdedcba
abcdeddedcba



  Build a KMP Partial match table of the string and match it with its reverse. When reaching the end, the unmatched suffix is the part that should be added to the left of the string.

public class Solution {
    public String shortestPalindrome(String s) {
        if (s.length() <= 1)
            return s;
        char[] c_str = s.toCharArray();
        // the next array stores the failure function of each position.
        int[] next = new int[c_str.length];
        next[0] = -1;
        int i = -1, j = 0;
        while (j < c_str.length-1) {
            if (i == -1 || c_str[i] == c_str[j]) {
                i ++;
                j ++;
                next[j] = i;
                if (c_str[j] == c_str[i]) . # THIS IS due to original KMP set the next value for non-matching, so to counter-act
            } else i = next[i];
        }
        // match the string with its reverse.
        i = c_str.length - 1; j = 0;
        while (i >= 0 && j < c_str.length) {
            if (j == -1 || c_str[i] == c_str[j]) {
                i --;
                j ++;
            } else {
                j = next[j];
            }
        }
        StringBuilder sb = new StringBuilder();
        for (i = c_str.length-1; i >= j; i --) sb.append(c_str[i]);
        for (char c : c_str) sb.append(c);
        return sb.toString();
    }
}

{  
    int pLen = strlen(p);  
    next[0] = -1;  
    int k = -1;  
    int j = 0;  
    while (j < pLen - 1)  
    {  
        //p[k]表示前缀，p[j]表示后缀  
        if (k == -1 || p[j] == p[k])   
        {  
            ++k;  
            ++j;  
            next[j] = k;  
        }  
        else   
        {  
            k = next[k];  
        }  
    }  
}  
    用代码重新计算下“ABCDABD”的next 数组，以验证之前通过“最长相同前缀后缀长度值右移一位，然后初值赋为-1”得到的next 数组是否正确，计算结果如下表格所示：



    从上述表格可以看出，无论是之前通过“最长相同前缀后缀长度值右移一位，然后初值赋为-1”得到的next 数组，还是之后通过代码递推计算求得的next 数组，结果是完全一致的。
int KmpSearch(char* s, char* p)  
{  
    int i = 0;  
    int j = 0;  
    int sLen = strlen(s);  
    int pLen = strlen(p);  
    while (i < sLen && j < pLen)  
    {  
        //①如果j = -1，或者当前字符匹配成功（即S[i] == P[j]），都令i++，j++      
        if (j == -1 || s[i] == p[j])  
        {  
            i++;  
            j++;  
        }  
        else  
        {  
            //②如果j != -1，且当前字符匹配失败（即S[i] != P[j]），则令 i 不变，j = next[j]      
            //next[j]即为j所对应的next值        
            j = next[j];  
        }  
    }  
    if (j == pLen)  
        return i - j;  
    else  
        return -1;  
}  

  1 out of 4   
Home   OJ   Shortest Palindrome   Python solution(KMP) 
New users please read the instructions to format your code properly. Discuss is a place to post interview questions or share solutions / ask questions related to OJ problems.
Python solution(KMP)

8
S sisie 
Reputation:  8
 class Solution:
# @param {string} s
# @return {string}
def shortestPalindrome(self, s):
    A=s+"*"+s[::-1]
    cont=[0]
    for i in range(1,len(A)):
        index=cont[i-1]
        while(index>0 and A[index]!=A[i]):
            index=cont[index-1]
        cont.append(index+(1 if A[index]==A[i] else 0))   # no need to counteract
    return s[cont[-1]:][::-1]+s . #prefix as pattern , next adjust the postion in prefix 


    #s becomes the pattern, index refer to the next of already matched pattern location ,
    search in the mirror of pattern, which has to be matched to the end