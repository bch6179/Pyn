https://leetcode.com/problems/sentence-screen-fitting/#/description
418. Sentence Screen Fitting Add to List
DescriptionSubmissionsSolutions
Total Accepted: 9409
Total Submissions: 34475
Difficulty: Medium
Contributors: Admin
Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.

Note:

A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.
Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.
Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output: 
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.
Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output: 
2

Explanation:
a-bcd- 
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.
Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output: 
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.
ate: See @iambright's post below for optimized code.

public class Solution {
    public int wordsTyping(String[] sentence, int rows, int cols) {
        String s = String.join(" ", sentence) + " ";
        int start = 0, l = s.length();
        for (int i = 0; i < rows; i++) {
            start += cols;
            if (s.charAt(start % l) == ' ') {
                start++;
            } else {
                while (start > 0 && s.charAt((start-1) % l) != ' ') {
                    start--;
                }
            }
        }
        
        return start / s.length();
    }
}
Update: As many people like this solution, let me explain by an example.

Say sentence=["abc", "de", "f], rows=4, and cols=6.
The screen should look like

"abc de"
"f abc "
"de f  "
"abc de"
Consider the following repeating sentence string, with positions of the start character of each row on the screen.

"abc de f abc de f abc de f ..."
 ^      ^     ^    ^      ^
 0      7     13   18     25
Our goal is to find the start position of the row next to the last row on the screen, which is 25 here. Since actually it's the length of everything earlier, we can get the answer by dividing this number by the length of (non-repeated) sentence string. Note that the non-repeated sentence string has a space at the end; it is "abc de f " in this example.

Here is how we find that position. In each iteration, we need to adjust start based on spaces either added or removed.

"abc de f abc de f abc de f ..." // start=0
 012345                          // start=start+cols+adjustment=0+6+1=7 (1 space removed in screen string)
        012345                   // start=7+6+0=13
              012345             // start=13+6-1=18 (1 space added)
                   012345        // start=18+6+1=25 (1 space added)
                          012345
Hope this helps.

5 months ago reply quote 
29
POSTS 11.6k
VIEWS Reply Back To Leetcode    Mark unread   Not Watching   Sort by 
37
F Free9 
Reputation:  60
Good job! Nice solution.

Let me explain a little to help others understand this solution well.

String s = String.join(" ", sentence) + " " ;. This line gives us a formatted sentence to be put to our screen.
start is the counter for how many valid characters from s have been put to our screen.
if (s.charAt(start % l) == ' ') is the situation that we don't need an extra space for current row. The current row could be successfully fitted. So that we need to increase our counter by using start++.
The else is the situation, which the next word can't fit to current row. So that we need to remove extra characters from next word.
start / s.length() is (# of valid characters) / our formatted sentence.
5 months ago reply quote 
int wordsTyping(vector<string>& sentence, int rows, int cols) {
        string s = "";                                          // s is the formatted sentence to be put to our screen
        for (string word : sentence) { s += " " + word; }
        
        int start = 1;                                          // skip the very first space char ' '
        for (int r = 0; r < rows; r++, start++) {               // advance start by one so s[start & s.length()] != ' '
            start += cols;                                      // full fill current collumn, so start advance by cols
            while (s[start % s.length()] != ' ') { start--; }   // make sure s[start & s.length()] == ' '
        }
        
        return --start / s.length();                            // we began with start == 1, so (start-1) is the valid length
}

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = " ".join(sentence) + " "
        start, n = 0, len(s)
        for i in range(0, rows):
            start += cols
            if s[start % n] == " ":
                start += 1
            else:
                while start > 0 and s[(start-1) % n] != " ":
                    start -= 1
        return start / n

        or last char in the row, you can test "s.charAt((start + l - 1) % l) != ' '" instead of start > 0 && ...

5 months ago reply quote 
41
I iaming 
Reputation:  271
Optimized to 12ms. O(m + n), m: length of sentence by char, n: rows.

public int wordsTyping(String[] sentence, int rows, int cols) {
    String s = String.join(" ", sentence) + " ";
    int len
     = s.length(), count = 0;
    int[] map = new int[len];
    for (int i = 1; i < len; ++i) {
        map[i] = s.charAt(i) == ' ' ? 1 : map[i-1] - 1;
    }
    for (int i = 0; i < rows; ++i) {
        count += cols;
        count += map[count % len];
    }
    return count / len;
}