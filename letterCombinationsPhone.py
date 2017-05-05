class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        def dfs(num, string, res):
            if num == length:
                res.append(string)
                return
            for letter in dict[digits[num]]:
                    dfs(num+1, string+letter, res)
        
        dict = {'2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']
                }
        res = []
        length = len(digits)
        if length == 0:
            return res
        dfs(0, '', res)
        return res
// version 2
class Solution(object):
    '''
    题意：输出电话号码对应的所有可能的字符串
    可以递归或直接模拟
    '''
    def letterCombinations(self, digits):
        chr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = []
        for i in range(0, len(digits)):
            num = int(digits[i])
            tmp = []
            for j in range(0, len(chr[num])):
                if len(res):
                    for k in range(0, len(res)):
                        tmp.append(res[k] + chr[num][j])
                else:
                    tmp.append(str(chr[num][j]))
            res = copy.copy(tmp)
        return res

class Solution(object):
    def letterCombinations(self, digits):
    dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl',\
            '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    return [a+b for a in dic.get(digits[:1],'')
                for b in self.letterCombinations(digits[1:]) or ['']] or []
about a year ago reply quote 
0
H huxley 
Reputation:  34
It's a functional way which uses a middle variable to make the recursion possible.

about a year ago reply quote 
6
B Baoyx007 
Reputation:  -9
Here is another version without reduce:

if '' == digits: return []
    kvmaps = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    ret=['']
    for c in digits:
        tmp=[]
        for y in ret:
            for x in kvmaps[c]:
                tmp.append(y+x)
        ret=tmp
    
    return ret

    class Solution {
public:
    vector<string> letterCombinations(string digits) {
    	vector<string> ret;
    	if(0>=digits.size()) return ret;
    
    	const string map[]={"0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
    	backTrackingFun(map,digits,"",ret);
    
    	return ret;
    }
    
    void backTrackingFun(const string m[], const string &digits, string r, vector<string> &ret){
    	int c=r.size();
    	if(digits.size()==c){
    		ret.push_back(r);
    		return;
    	}
    
    	auto str = m[digits.at(c)-48];
    	for(auto it=str.cbegin();it!=str.cend();++it){
    		r.push_back(*it);
    		backTrackingFun(m,digits,r,ret);
    		r.pop_back();
    	}
    }
};
2 years ago reply quote 
0
Q qeatzy   @redace85
Reputation:  176
actually, by introducing a few data member, one param does suffice.

2 years ago reply quote 
1
T tju_xu97 
Reputation:  188
A more concise recursive solution with only one function:

    string num2alpha[8] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    vector<string> letterCombinations(string digits) {
        vector<string> result;
        if(digits.empty()) return result;
        char curDigit = digits[0];
        string curStr = num2alpha[curDigit-'2'];
        vector<string> subResult = letterCombinations(digits.substr(1));
        if(subResult.empty()) subResult.emplace_back("");
        for(int i = 0; i < curStr.length(); ++i)
        {
            for(int j = 0; j < subResult.size(); ++j)
            {
                string tmp = "";
                tmp += curStr[i];
                tmp = tmp + subResult[j];
                result.emplace_back(tmp);
            }
        }
        return result;
}
 class Solution(object):
      def letterCombinations(self, digits):
    if not digits:
        return []
    results = ['']
    map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    
    for digit in digits:
        results = [result+d for result in results for d in map[digit]]
        
    return results