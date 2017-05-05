class Solution(object):
    #too abstract to understand
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        self.size = len(target)
        self.wlist = [self.toNumber(target, d) \
                      for d in dictionary \
                      if len(d) == self.size]
        self.ans = (1 << self.size) - 1
        self.length = self.size
        self.dfs(0, 0, 0)
        return self.toWord(self.ans, target)
    def dfs(self, number, depth, length):
        if length >= self.length: return
        if depth == self.size:
            if not any(number & w == number for w in self.wlist):
                self.ans = number
                self.length = length
            return
        self.dfs((number << 1) + 1, depth + 1, length + 1)
        if length == 0 or number & 1:
            for x in range(2, self.size - depth + 1):
                self.dfs(number << x, depth + x, length + 1)
    def toNumber(self, target, word):
        ans = 0
        for x in range(self.size):
            ans <<= 1
            ans += target[x] == word[x]
        return ans
    def toWord(self, number, target):
        ans = ''
        cnt = 0
        for x in range(self.size):
            if number & (1 << self.size - x - 1):
                if cnt:
                    ans += str(cnt)
                    cnt = 0
                ans += target[x]
            else:
                cnt += 1
        return ans + str(cnt or '')
s = Solution()
print s.minAbbreviation("apple", ["plain", "amber", "blade"])

# I really like this solution in that:

# It pre-process dictionary into list of bit representations of words for efficient match checking
# It prunes the DFS tree aggressively as the algorithm proceeds
# It has clear logic separations e.g. toNumber() and toWrod()
