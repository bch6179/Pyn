#[0216]
[Greedy-TargetDriving]while each potential i:
    while condition for i-left be the window required
        change window left if overqualified
    i - left added to res if satisfy

#use spectrum for repetitive application , maintain a window, transform and conquer
# word as unit to compare, consider coverage, instead of seeing a non word char moving forward one, moving forward as word unit length
#not avoiding complicating
#pattern and count
# Substring with Concatenation of All Words     
 
# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

# For example, given:
# s: "barfoothefoobarman"
# words: ["foo", "bar"]

# You should return the indices: [0,9].
import copy
class Solution(object):
    def findSubstring(self, s, words):# abcbcba abbc  #aaa aaa #babc abcb  #spectrum
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
    
        
        if not s or not words:
            return []
        req = {}
        for w in words:
            req[w] = req.get(w,0)+1   
        m = len(words)
        n = len(words[0])
      
        res = set()
       
         
        for j in range(n):
            i = j
            left = j
        
            cur = {} #copy.deepcopy(oridict) #Mistake
            while i < len(s)-n+1:  #should avoid duplicate result
                str =  s[i:i+n] 
                i+=n  
                if str in req:
                    cur[str] = cur.get(str,0)+1   
                 
                    
                    
                    while cur[str] > req[str]:
                        cur[s[left:left+n]]  -= 1   
                         #move out left one
                        left += n  
                        
                    if  i-left == m*n:
                        res.add(left)
            
                else:
                    #i+=1#Mistake should not +=1 ,mi ss is si and m is si ss 
                    left = i
                    cur.clear()
        return list(res)
    def _findSubstring(self, l, r, n, k, t, s, req, ans):
    curr = {}
    while r + k <= n:
        w = s[r:r + k]
        r += k
        if w not in req:
            l = r
            curr.clear()
        else:
            curr[w] = curr[w] + 1 if w in curr else 1
            while curr[w] > req[w]:
                curr[s[l:l + k]] -= 1
                l += k
            if r - l == t:
                ans.append(l)

def findSubstring(self, s, words):
    if not s or not words or not words[0]:
        return []
    n = len(s)
    k = len(words[0])
    t = len(words) * k
    req = {}
    for w in words:
        req[w] = req[w] + 1 if w in req else 1
    ans = []
    for i in xrange(min(k, n - t + 1)):
        self._findSubstring(i, i, n, k, t, s, req, ans)
    return ans


# 169 / 169 test cases passed.
# Status: Accepted
# Runtime: 80 ms
# 98.60%
First of all consider s as several series of words with length k starting at [0, k-1]. For example "barfoothe" with k = 3, can be view as ["bar", "foo", "the"] for i=0 and ["arf", "oot"] for i = 1 and ["rfo", "oth"] for i = 2.
Thus we need to check each of these series and find out the valid index by definition.

For each series, we just need to check if there exist a range [l, r) where the occurrence or "spectrum" of the words in the range is the same as our given word list's "spectrum". We use dictionary to store the spectrum and maintain it as we loop through s.

collections.Counter class may save a bit of code on updating the counts of the dictionary. However plain dict wins on the speed.
    def findSubstring_wrong(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def findword(i):
            return ''.join(s[i:i+len(words[0])])
        
        if not s or not words:
            return []
        dict = {}
        for w in words:
            dict[w] = -1
        m = len(words)
        n = len(words[0])
      
        res = []
        left = -1
        i = 0
        while i < len(s)-n+1:
            str = ''.join(s[i:i+n]) 
            if str in dict:
                if  dict[str] == -1 or dict[str] < left: #for not repetitive # abca
                    if left == -1:
                        left = i
                    dict[str] = i
                    if i+n-left == m*n:
                        res.append(left)
                        #move out left one
                        left += n 
                else:
                    left = dict[str]+n #repetitive
                i+=n   
            else:
                i+=1
                left = i
        return res
    "lingmindraboofooowingdingbarrwingmonkeypoundcake"
["fooo","barr","wing","ding","wing"]
Output:
[]
Expected:
[13]
    def findSubstring_failed(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        def findword(i):
            return ''.join(s[i:i+len(words[0])])
        
        if not s or not words:
            return []
        oridict = {}
        for w in words:
            if w in oridict:
                oridict[w][1] += 1
            else:
                oridict[w] = [-1, 1]
        m = len(words)
        n = len(words[0])
      
        res = []
       
         
        for j in range(n):
            i = j
            left = -1
        
            dict = copy.deepcopy(oridict) #Mistake
            while i < len(s)-n+1:
                str = ''.join(s[i:i+n]) 
                if str in dict:
                    if  dict[str][0] == -1 or dict[str][0] < left: #for not repetitive # abca
                        if left == -1:
                            left = i
                        dict[str][0] = i
                        dict[str][1] -= 1
                
                    else:
                        if dict[str][1] == 0:
                            left = dict[str][0]+n #repetitive
                            dict[str][0] = i
                        else:
                            dict[str][1] -= 1 #foobarbar
                    i+=n   
                    if left != -1 and i-left == m*n:
                        res.append(left)
                        #move out left one
                        left += n 
                else:
                    i+=1
                    left = i
        return res
s = Solution() 
print s.findSubstring("aaaaaaaa",["aa","aa","aa"])
print s.findSubstring("aaa",["a","b"])
# print s.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",
# ["fooo","barr","wing","ding","wing"])


#  // travel all the words combinations to maintain a window
#     // there are wl(word len) times travel
#     // each time, n/wl words, mostly 2 times travel for each word
#     // one left side of the window, the other right side of the window
#     // so, time complexity O(wl * 2 * N/wl) = O(2N)
#     vector<int> findSubstring(string S, vector<string> &L) {
#         vector<int> ans;
#         int n = S.size(), cnt = L.size();
#         if (n <= 0 || cnt <= 0) return ans;
        
#         // init word occurence
#         unordered_map<string, int> dict;
#         for (int i = 0; i < cnt; ++i) dict[L[i]]++;
        
#         // travel all sub string combinations
#         int wl = L[0].size();
#         for (int i = 0; i < wl; ++i) {
#             int left = i, count = 0;
#             unordered_map<string, int> tdict;
#             for (int j = i; j <= n - wl; j += wl) {
#                 string str = S.substr(j, wl);
#                 // a valid word, accumulate results
#                 if (dict.cout(str)) {
#                     tdict[str]++;
#                     if (tdict[str] <= dict[str]) 
#                         count++;
#                     else {
#                         // a more word, advance the window left side possiablly
#                         while (tdict[str] > dict[str]) {
#                             string str1 = S.substr(left, wl);
#                             tdict[str1]--;
#                             if (tdict[str1] < dict[str1]) count--;
#                             left += wl;
#                         }
#                     }
#                     // come to a result
#                     if (count == cnt) {
#                         ans.push_back(left);
#                         // advance one word
#                         tdict[S.substr(left, wl)]--;
#                         count--;
#                         left += wl;
#                     }
#                 }
#                 // not a valid word, reset all vars
#                 else {
#                     tdict.clear();
#                     count = 0;
#                     left = j + wl;
#                 }
#             }
#         }
        
#         return ans;
#     }