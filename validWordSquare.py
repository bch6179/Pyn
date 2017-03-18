# Valid Word Square https://leetcode.com/problems/valid-word-square/
# Given a sequence of words, check whether it forms a valid word square.

# A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤k < max(numRows, numColumns).

# Note:

# The number of words given is at least 1 and does not exceed 500.
# Word length will be at least 1 and does not exceed 500.
# Each word contains only lowercase English alphabet a-z.
 

# Example 1:

# Input:
# [
#   "abcd",
#   "bnrt",
#   "crmy",
#   "dtye"
# ]

# Output:
# true

# Example 2:

# Input:
# [
#   "abcd",
#   "bnrt",
#   "crm",
#   "dt"
# ]

# Output:
# true
# Two loop solution: Time O(MN) and Space O(1)

# Use two for loops. Outer loop iterates through each word row by row. The pointer is i.
# Inner for loop iterates from 0 to length of the row word. The pointer is j.
# Now word[i,j] must be equal to word[j,i].
# We are sure that word[i,j] is valid. We must also make sure we are not accessing out of bounds for word[j,i]. Therefore we have additional checks.
class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j < len(words) and i < len(words[j]) and words[i][j] == words[j][i]:  #Mistake i < words[j] length not words[i], we switching
                    continue
                else:
                    return False
        return True