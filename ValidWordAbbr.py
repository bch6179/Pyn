https://leetcode.com/problems/valid-word-abbreviation/?tab=Description

Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:
Given s = "apple", abbr = "a2e":

Return false.

F fschaffa 
Reputation:  2
 class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, n = 0, ''
        for c in abbr:
            if c.isalpha():
                i += int('0'+n)
                if i >= len(word) or c != word[i]: return False
                i, n = i+1, ''
            else:
                if n == '' and c == '0': return False
                n += c
        return i+int('0'+n) == len(word)

        def validWordAbbreviation(self, word, abbr):
            """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, n = 0, "0"
        for c in abbr:
            if c.isdigit():
                if n == c:
                    return False
                n += c
            else:
                i += int(n)
                if i>=len(word) or word[i] != c:
                    return False
                i += 1
                n = '0'
                
        return i+int(n)== len(word)
   
  public boolean validWordAbbreviation(String word, String abbr) {
        int i = 0, j = 0;
        while (i < word.length() && j < abbr.length()) {
            if (word.charAt(i) == abbr.charAt(j)) {
                ++i;++j;
                continue;
            }
            if (abbr.charAt(j) <= '0' || abbr.charAt(j) > '9') {
                return false;
            }
            int start = j;
            while (j < abbr.length() && abbr.charAt(j) >= '0' && abbr.charAt(j) <= '9') {
                ++j;
            }
            int num = Integer.valueOf(abbr.substring(start, j));
            i += num;
        }
        return i == word.length() && j == abbr.length();
    }


public boolean validWordAbbreviation(String word, String abbr) {
        if (word.length() == 0 || abbr.length() == 0) {
            return word.length() == 0 && abbr.length() == 0;
        }
        
        if (word.charAt(0) == abbr.charAt(0)) {
            return validWordAbbreviation(word.substring(1), abbr.substring(1));
        } else if (Character.isDigit(abbr.charAt(0))) {
            //deal with special case like ('a' & '01')
            if (abbr.charAt(0) == '0') {
                return false;
            }
            int num = 0;
            int idx = 0;
            while (idx < abbr.length() && Character.isDigit(abbr.charAt(idx))) {
                num = num * 10 + abbr.charAt(idx++) - '0';
            }
            if (num > word.length() || idx > abbr.length()) {
                return false;
            }
            return validWordAbbreviation(word.substring(num), abbr.substring(idx));
        } 
        return false;
    }
