class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def dfs(s, level, ip):
            if level == 4:
                if s == '':
                    res.append(ip[1:])
                return
            for i in range(1, 4):
                if i <= len(s):
                    if int(s[:i]) <= 255:
                        dfs(s[i:], level+1, ip+'.'+s[:i])
                    if s[0] == '0': break # Mistake not checking 00. (error)
        res = []
        dfs(s, 0, '')
        return res