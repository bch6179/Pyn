The idea is:

for zero, it's the only word has letter 'z',
for two, it's the only word has letter 'w',
......
so we only need to count the unique letter of each word, Coz the input is always valid.

Code:
 def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        ret = []
        ret.extend( ['0'] * dic.get('z', 0) )
        ret.extend( ['1'] * (dic.get('o', 0)-dic.get('z', 0)-dic.get('w', 0)-dic.get('u', 0)) )
        ret.extend( ['2'] * dic.get('w', 0) )
        ret.extend( ['3'] * (dic.get('h', 0)-dic.get('g', 0)) )
        ret.extend( ['4'] * dic.get('u', 0) )
        ret.extend( ['5'] * (dic.get('f', 0)-dic.get('u', 0)) )
        ret.extend( ['6'] * dic.get('x', 0) )
        ret.extend( ['7'] * (dic.get('s', 0)-dic.get('x', 0)) )
        ret.extend( ['8'] * dic.get('g', 0) )
        ret.extend( ['9'] * (dic.get('i', 0)-dic.get('g', 0)-dic.get('x', 0)-dic.get('f', 0)+dic.get('u', 0) ) )
        return ''.join( ret )
public String originalDigits(String s) {
    int[] count = new int[10];
    for (int i = 0; i < s.length(); i++){
        char c = s.charAt(i);
        if (c == 'z') count[0]++;
        if (c == 'w') count[2]++;
        if (c == 'x') count[6]++;
        if (c == 's') count[7]++; //7-6
        if (c == 'g') count[8]++;
        if (c == 'u') count[4]++; 
        if (c == 'f') count[5]++; //5-4
        if (c == 'h') count[3]++; //3-8
        if (c == 'i') count[9]++; //9-8-5-6
        if (c == 'o') count[1]++; //1-0-2-4
    }
    count[7] -= count[6];
    count[5] -= count[4];
    count[3] -= count[8];
    count[9] = count[9] - count[8] - count[5] - count[6];
    count[1] = count[1] - count[0] - count[2] - count[4];
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i <= 9; i++){
        for (int j = 0; j < count[i]; j++){
            sb.append(i);
        }
    }
    return sb.toString();
}

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        mp = {}
        for c in s:
           mp.setdefault(c, 0)
           mp[c] += 1
           
        ans = [0] * 10
        self.dfs(mp, ans)
        return "".join([str(num) * ans[num] for num, count in enumerate(ans)])
        
    def dfs(self, mp, ans):
        str_to_digit = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
        while mp != {}:
            if 'z' in mp:
                t = 0
            elif 'w' in mp:
                t = 2
            elif 'u' in mp:
                t = 4
            elif 'f' in mp:
                t = 5
            elif 'x' in mp:
                t = 6
            elif 'g' in mp:
                t = 8
            elif 'v' in mp:
                t = 7
            elif 'o' in mp:
                t = 1
            elif 't' in mp:
                t = 3
            else:
                t = 9
            for c in str_to_digit[t]:
                mp[c] -= 1
                if mp[c] == 0:
                    del mp[c]
            ans[t] += 1
        return ans