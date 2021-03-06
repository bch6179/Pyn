# https://leetcode.com/problems/minimum-unique-word-abbreviation/#/description
# A string such as "word" contains the following abbreviations:

# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.

# Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.

# Note:
# In the case of multiple answers as shown in the second example below, you may return any one of them.
# Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.
# Examples:
# "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

# "apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
 

def minAbbreviation(self, target, dictionary):
    m = len(target)
    diffs = {sum(2**i for i, c in enumerate(word) if target[i] != c)
             for word in dictionary if len(word) == m}
    if not diffs:
        return str(m)
    bits = max((i for i in range(2**m) if all(d & i for d in diffs)),
               key=lambda bits: sum((bits >> i) & 3 == 0 for i in range(m-1)))
    s = ''.join(target[i] if bits & 2**i else '#' for i in range(m))
    return re.sub('#+', lambda m: str(len(m.group())), s)
If the target is apple and the dictionary contains apply, then the abbreviation must include the e as the letter e, not in a number. It's the only letter distinguishing these two words. Similarly, if the dictionary contains tuple, then the abbreviation must include the a or the first p as a letter.

For each dictionary word (of correct size), I create a diff-number whose bits tell me which of the word's letters differ from the target. Then I go through the 2m possible abbreviations, represented as number from 0 to 2m-1, the bits representing which letters of target are in the abbreviation. An abbreviation is ok if it doesn't match any dictionary word. To check whether an abbreviation doesn't match a dictionary word, I simply check whether the abbreviation number and the dictionary word's diff-number have a common 1-bit. Which means that the abbreviation contains a letter where the dictionary word differs from the target.

Then from the ok abbreviations I find one that maximizes how much length it saves me. Two consecutive 0-bits in the abbreviation number mean that the two corresponding letters will be encoded as the number 2. It saves length 1. Three consecutive 0-bits save length 2, and so on. To compute the saved length, I just count how many pairs of adjacent bits are zero.

Now that I have the number representing an optimal abbreviation, I just need to turn it into the actual abbreviation. First I turn it into a string where each 1-bit is turned into the corresponding letter of the target and each 0-bit is turned into #. Then I replace streaks of # into numbers.

6 months ago reply quote 
4
POSTS 1.3k
VIEWS Reply Back To Leetcode    Mark unread   Not Watching   Sort by 
0
在 在线疯狂 
Reputation:  72
short and clear, good job!

5 months ago reply quote 
1
C cwl 
Reputation:  63
Nice and clever! It took me a while to figure out the succinct implementation. I took notes and rewrote it as following

def minAbbreviation(self, target, dictionary):
    def abbr(target, num):
        word, count = '', 0
        for w in target:
            if num & 1 == 1:
                if count:
                    word += str(count)
                    count = 0
                word += w
            else:
                count += 1

            num >>= 1
        if count:
            word += str(count)
        return word

    m = len(target)

    # Figure out the different bits for a same length word in the dictionary
    diffs = []
    for word in dictionary:
        if len(word) != m:
            continue

        # The encoding is opposite
        bits = 0
        for i, char in enumerate(word):
            if char != target[i]:
                bits += 2 ** i
        diffs += bits,

    # No word in dictionary has same length, return the shortest
    if not diffs:
        return str(m)        
    
    abbrs = []
    for i in range(2 ** m):
        # This abbreviation at least has one word different to every words in the dictionary
        if all(d & i for d in diffs):
            abbrs += abbr(target, i),

    return min(abbrs, key=lambda x: len(x))


    G gabbu 
Reputation:  72
Solution

Minimum Unique Word Abbreviation https://leetcode.com/problems/minimum-unique-word-abbreviation/

Algorithm

This problem is a combination of the other two related problems.
Use the approach of “320. Generalized Abbreviation” to generate all abbreviations of “target”.
Notice how we modify process_solution so that we also return the count correctly as specified in the problem.
With each abbreviation, check whether it’s an abbreviation of any word in the dictionary using the approach of “408. Valid Word Abbreviation”
Preprocess the dictionary to remove those words which can never have same abbreviation as target. Refer to this for explanation:https://discuss.leetcode.com/topic/61349/insights-optimizing-hacking
class Solution(object):
    def extract_number(self, j, abbr, M):
        num = 0
        while j < M and abbr[j].isdigit():
            num, j = num*10 + int(abbr[j]), j+1
        return num, j
    
    def valid(self, word, abbr):
        i,j,N, M = 0,0,len(word), len(abbr)
        while i < N and j < M:
            if abbr[j].isalpha() and abbr[j] != word[i]:
                return False
            elif abbr[j].isalpha() and abbr[j] == word[i]:
                i,j = i+1,j+1
            elif abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                num, j = self.extract_number(j, abbr, M)
                i = i+num
        return (i==N and j == M)
        
    def process_solution(self, so_far):
        csofar, i, cnt = [], 0, 0
        while i < len(so_far):
            if so_far[i].isalpha():
                csofar.append(so_far[i])
                i, cnt = i+1, cnt+1
            else:
                num = 0
                while i < len(so_far) and so_far[i].isdigit():
                    num, i = num+1, i+1
                cnt = cnt + 1
                csofar.append(str(num))
        return "".join(csofar), cnt
    
    def test(self, abbr, dictionary):
        for wrd in dictionary:
            if self.valid(wrd, abbr):
                return False
        return True
    
    def helper(self, word, so_far, i, dictionary):
        if i == len(word):
            abbr, cnt = self.process_solution(so_far)
            if cnt < self.result_len and self.test(abbr, dictionary):
                self.result, self.result_len = abbr, cnt
            return
        else:
            so_far.append("1")
            self.helper(word, so_far, i+1, dictionary)
            so_far.pop()
            so_far.append(word[i])
            self.helper(word, so_far, i+1, dictionary)
            so_far.pop()

    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        
        # Remove those words which can never be an abbreviation for target.
        # This preprocessing will help us save time.
        filtered_dictionary = []
        for wrd in dictionary:
            if len(wrd) != len(target):
                continue
            filtered_dictionary.append(wrd)
        dictionary = filtered_dictionary
        if len(dictionary) == 0:
            return str(len(target))
            
        self.result_len = len(target)+1
        self.result, so_far, i = target, [], 0
        self.helper(target, so_far, i, dictionary)        
        return self.result