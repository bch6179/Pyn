#https://leetcode.com/problems/generalized-abbreviation/?tab=Description

#Maintain how many abbreviated during two branch DFS besides of pos tracking
#Nonlinear thinking tree or graph , correlation, recursive for inner structure if seeing 1ord 1o1d 1o2
#linear check list : multiple or n-for or two dfs, pass pos+1 or index+1, pass count or other variable
# Write a function to generate the generalized abbreviations of a word.
#find the recurrence relation overlapping in the examples based on the base case (last position at 4, return), from achiving results  word wor1 (first branch), decrease and conquer dfs left, dfs right;  from analysis and implementation, wxxx, 1xxx dfs recurse left and right 
# Example:
# Given word = "word", return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# The idea is: for every character, we can keep it or abbreviate it. To keep it, we add it to the current solution and carry on backtracking. To abbreviate it, we omit it in the current solution, but increment the count, which indicates how many characters have we abbreviated. When we reach the end or need to put a character in the current solution, and count is bigger than zero, we add the number into the solution.


class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def helper(word, pos, cur, count, result):
            if len(word) == pos:
                # Once we reach the end, append current to the result
                result.append(cur + str(count) if count > 0 else cur)
            else:
            
                # Skip current position, and increment count
                helper(word, pos + 1, cur, count + 1, result)
                    # Include current position, and zero-out count
                helper(word, pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0, result)

        result = []
        helper(word, 0, '', 0, result)
        return result
s= Solution()
res = s.generateAbbreviations("word")
print res


