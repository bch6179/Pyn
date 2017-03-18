# [LeetCode] Strobogrammatic Number III 对称数之三
 

# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

# For example,
# Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.

# Note:
# Because the range might be a large number, the low and high numbers are represented as string.

 

# Show Tags
# Show Similar Problems
 
# 这道题是之前那两道Strobogrammatic Number II和Strobogrammatic Number的拓展，又增加了难度，让我们找到给定范围内的对称数的个数，我们当然不能一个一个的判断是不是对称数，我们也不能直接每个长度调用第二道中的方法，保存所有的对称数，然后再统计个数，这样OJ会提示内存超过允许的范围，所以我们的解法是基于第二道的基础上，不保存所有的结果，而是在递归中直接计数，根据之前的分析，需要初始化n=0和n=1的情况，然后在其基础上进行递归，递归的长度len从low到high之间遍历，然后我们看当前单词长度有没有达到len，如果达到了，我们首先要去掉开头是0的多位数，然后去掉长度和low相同但小于low的数，和长度和high相同但大于high的数，然后结果自增1，然后分别给当前单词左右加上那五对对称数，继续递归调用，参见代码如下：



# Strobogrammatic Number III 对称数之三count = 0
pairs = ["00","11","69","88","96"]

def strobogrammaticInRange(self, low, high):
    """
    :type low: str
    :type high: str
    :rtype: int
    """
    for i in range(len(low),len(high)+1):
        self.dfs(low,high,["#"]*i,0,i-1)
    return self.count
    
def dfs(self,low,high,c,left,right):
    if left > right:
        s = "".join(c)
        if (len(s) == len(low) and int(s) < int(low)) or (len(s) == len(high) and int(s) > int(high)):
            return
        self.count += 1
        return
    for p in self.pairs:
        c[left] = p[0]
        c[right] = p[1]
        if len(c) != 1 and c[0] == "0":
            continue
        if left < right or (left == right and p[0] == p[1]):
            self.dfs(low,high,c,left+1,right-1)

    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        maps={"0":"0","1":"1","6":"9","8":"8","9":"6"}
        cl,ch=len(low), len(high)
        if cl>ch or (cl==ch and low>high): return 0
        
        ans=["","0","1","8"]
        count=0
        while ans:
            tmp=[]
            for w in ans:
                if len(w)<ch or (len(w)==ch and w<=high):
                    if len(w)>cl or (len(w)==cl and w>=low):  
                        if len(w)>1 and w[0]=="0":##leading zeros
                            pass
                        else:
                            count+=1
                    
                    if ch-len(w)>=2:                
                        for key in maps:
                            res=key+w+maps[key]
                            tmp.append(res)
            ans=tmp
        return count
        
class Solution {
public:
    int strobogrammaticInRange(string low, string high) {
        int res = 0;
        find(low, high, "", res);
        find(low, high, "0", res);
        find(low, high, "1", res);
        find(low, high, "8", res);
        return res;
    }
    void find(string low, string high, string w, int &res) {
        if (w.size() >= low.size() && w.size() <= high.size()) {
            if ((w.size() == low.size() && w.compare(low) < 0) || (w.size() == high.size() && w.compare(high) > 0)) {
                return;
            }
            if (!(w.size() > 1 && w[0] == '0')) ++res;
        }
        if (w.size() + 2 > high.size()) return;
        find(low, high, "0" + w + "0", res);
        find(low, high, "1" + w + "1", res);
        find(low, high, "6" + w + "9", res);
        find(low, high, "8" + w + "8", res);
        find(low, high, "9" + w + "6", res);
    }
};

class Solution(object):
    def __init__(self):
        self.res = 0
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        def dfs(cur, low, high):
            
            if len(cur) >= len(low) and len(cur) <= len(high):    
                if len(cur) == len(low) and int(cur) < int(low) or len(cur) == len(high) and int(cur) > int(high):
                    return
                if not(len(cur) > 1 and cur[0] == '0'): #should be '0' instead of 0
                    self.res += 1
                  
            if len(cur) + 2 > len(high): return
            
            dfs('0'+cur+'0', low, high)
            dfs('6'+cur+'9', low, high)
            
            dfs('9'+cur+'6', low, high)
            
            dfs('8'+cur+'8', low, high)
            
            dfs('1'+cur+'1', low, high)
            
        dfs('', low,high)
        dfs('0', low, high)
        
        dfs('1', low, high)
        
        dfs('8', low, high)
            
        return self.res