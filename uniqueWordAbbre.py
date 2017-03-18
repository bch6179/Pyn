[LeetCode] Unique Word Abbreviation

Problem Description:

An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example: 

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true 
To check for unique abbreviation, we maintain a mapping from a specific abbreviation to all words which have the abbreviation. Then we just need to check no other words have the same abbreviation as the given word.

The code is as follows.

复制代码
class ValidWordAbbr {
public:
    ValidWordAbbr(vector<string> &dictionary) {
        for (string& d : dictionary) {
            int n = d.length();
            string abbr = d[0] + to_string(n) + d[n - 1];
            mp[abbr].insert(d);
        }
    }

    bool isUnique(string word) {
        int n = word.length();
        string abbr = word[0] + to_string(n) + word[n - 1];
        return mp[abbr].count(word) == mp[abbr].size(); 
    }
private:
    unordered_map<string, unordered_set<string>> mp;
};


import collections
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dict = collections.defaultdict(set)
        for w in dictionary:
            val = w
            if len(w) > 2:
                w = w[0] + str(len(w)-2) + w[-1]
            self.dict[w].add(val)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        val = word
        if len(word) > 2:
            word = word[0]+ str(len(word)-2) + word[-1] #-2 
        return word not in self.dict or len(self.dict[word]) == 1 and val == list(self.dict[word])[0] #Mistake , == instead of !=
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)