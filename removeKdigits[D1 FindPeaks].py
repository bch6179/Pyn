I am able to see the "peaks" numbers are to be removed, but come up aalgorithm to pick up the top k largest  
 first algorithm is straight-forward. Let's think about the simplest case: how to remove 1 digit from the number so that the new number is the smallest possible？ Well, one can simply scan from left to right, and remove the first "peak" digit; the peak digit is larger than its right neighbor. One can repeat this procedure k times, and obtain the first algorithm:

 stack pop can play the same effect of removing the peaks
 
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        while k > 0:
            k -= 1
            i = 0
            while i < len(num)-1:
                if num[i] > num[i+1]:
                    break
                i += 1
            num = num[:i] + num[i+1:]
        
        if len(num) == 0:
            return "0"
        else:
            return str(int(num))
string removeKdigits(string num, int k) {
        while (k > 0) {
            int n = num.size();
            int i = 0;
            while (i+1<n && num[i]<=num[i+1])  i++;
            num.erase(i, 1);
            k--;
        }
        // trim leading zeros
        int s = 0;
        while (s<(int)num.size()-1 && num[s]=='0')  s++;
        num.erase(0, s);
        
        return num=="" ? "0" : num;
    }
The above algorithm is a bit inefficient because it frequently remove a particular element from a string and has complexity O(k*n).

One can simulate the above procedure by using a stack, and obtain a O(n) algorithm. Note, when the result stack (i.e. res) pop a digit, it is equivalent as remove that "peak" digit.
string removeKdigits(string num, int k) {
        string res;
        int keep = num.size() - k;
        for (int i=0; i<num.size(); i++) {
            while (res.size()>0 && res.back()>num[i] && k>0) {
                res.pop_back();
                k--;
            }
            res.push_back(num[i]);
        }
        res.erase(keep, string::npos);
        
        // trim leading zeros
        int s = 0;
        while (s<(int)res.size()-1 && res[s]=='0')  s++;
        res.erase(0, s);
        
        return res=="" ? "0" : res;
    }