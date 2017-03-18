class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i,n = 0,'0'
        for c in abbr:
            if c.isalpha():
                i += int(n)
                n = '0'
                if i >= len(word) or word[i] != c:
                    return False
                i += 1
            elif c.isdigit():
                if c == '0': return False
                n += c    
        return i+int(n) == len(word)
s = Solution() 
print s.validWordAbbreviation("abbreviation","a10n")