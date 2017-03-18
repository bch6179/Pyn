Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordList.add(endWord)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        d = construct_dict(wordList | set([beginWord, endWord]))
        return bfs_words(beginWord, endWord, d)

I came up with the exact same way to find neighbors! I originally tried to use a mapping of both the patterns to the words and the words to their patterns, but the overhead of building the second mapping (just the appending cost) was high enough to offset the benefits (at least on shorter wordlists).

Even though your posted solution definitely doesn't beat 95% of solution at the time of my writing (the best I got with it as you have it posted was around 77%) it's still a great solution and I wanted to share some of my modifications (got the run time down to 196ms which is just above 88%). I have some fundamental improvements to the algorithm, and a few pythonic changes as well.

Algorithmic improvements:
In BFS you should always check a node to determine if it meets the goal criteria BEFORE adding it to the queue. If you wait to check till you pop the node your time complexity goes from O(b^d) to O(b^(d+1)). This makes a pretty big difference.

Second, because this is a BFS, once a node has been seen, that is the earliest it could have possibly been seen so nodes should be added to the visited set as soon as they are seen, not after they are popped from the queue. This reduces the size of the queue and the number of append operations.

Third, a simple pythoninc improvement is to use collections.defaultdict instead of the dict.get method. This is for a couple of reasons, the first is that it makes the code a bit simpler, and the second is that dict.get is slow in comparison.

That's pretty much it. Thanks again for sharing your solution!

Here's my code:

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
                
        def make_p2w(word_list, w_idxs):
            """Creates a map of all combinations of words with missing letters mapped 
            to all words in the list that match that pattern.
            E.g. hot -> {'_ot': ['hot'], 'h_t': ['hot'], 'ho_': ['hot']}
            """
            p2w = collections.defaultdict(list)
            
            for word in word_list:
                for i, j in w_idxs:
                    p = word[:i] + "_" + word[j:]
                    p2w[p].append(word)
            return p2w
            
        def bfs_words(begin, end, w_idxs, p2w):
            queue = collections.deque([(begin, 1)])
            visited = set([begin])
                        
            while queue:
                # Get the next node to explore from the top of the queue
                word, depth = queue.popleft()
                
                # Get the node's children 
                # By recreating all possible patterns for that string
                for i,j in w_idxs:
                    p = word[:i] + "_" + word[j:]
                    neighbor_words = p2w[p]
                    # Iterate through children
                    for nw in neighbor_words:
                        if nw not in visited:
                            # Goal check (before adding to the queue)
                            if nw == end:
                                return depth+1
                            # Add to visited
                            # These is no reason to wait to mark nodes as visited. Because this is 
                            # a BFS, once a node has been seen that is the earliest it could have
                            # possibly been seen so any other path to that node would either be 
                            # longer or the same length as what we've already observed.
                            visited.add(nw)                            
                            # Add to the end of the queue
                            queue.append((nw, depth+1))
            return 0
        
        # Get word length and character indexes
        wl = len(beginWord)
        w_indexes = zip(range(wl), range(1, wl+1))
        # Preprocess words into a map
        patterns2words = make_p2w(wordList | set([beginWord, endWord]), w_indexes)
        # Do the search
        return bfs_words(beginWord, endWord, w_indexes, patterns2words)


原题链接: http://oj.leetcode.com/problems/word-ladder/
这道题看似一个关于字符串操作的题目，其实要解决这个问题得用图的方法。我们先给题目进行图的映射，顶点则是每个字符串，然后两个字符串如果相差一个字符则我们进行连边。接下来看看这个方法的优势，注意到我们的字符集只有小写字母，而且字符串长度固定，假设是L。那么可以注意到每一个字符可以对应的边则有25个（26个小写字母减去自己），那么一个字符串可能存在的边是25*L条。接下来就是检测这些边对应的字符串是否在字典里，就可以得到一个完整的图的结构了。根据题目的要求，等价于求这个图一个顶点到另一个顶点的最短路径，一般我们用广度优先搜索（不熟悉搜索的朋友可以看看Clone Graph）即可。这个算法中最坏情况是把所有长度为L的字符串都看一下，或者把字典中的字符串都看一下，而长度为L的字符串总共有26^L，所以时间复杂度是O(min(26^L, size(dict))，空间上需要存储访问情况，也是O(min(26^L, size(dict))。代码如下：
[java] view plaincopy￼￼￼
public int ladderLength(String start, String end, HashSet<String> dict) { 
    if(start==null || end==null || start.length()==0 || end.length()==0 || start.length()!=end.length()) 
        return 0; 
    LinkedList<String> queue = new LinkedList<String>(); 
    HashSet<String> visited = new HashSet<String>(); 
    int level= 1; 
    int lastNum = 1; 
    int curNum = 0; 
    queue.offer(start); 
    visited.add(start); 
    while(!queue.isEmpty()) 
    { 
        String cur = queue.poll(); 
        lastNum--; 
        for(int i=0;i<cur.length();i++) 
        { 
            char[] charCur = cur.toCharArray(); 
            for(char c='a';c<='z';c++) 
            { 
                charCur[i] = c; 
                String temp = new String(charCur); 
                if(temp.equals(end)) 
                    return level+1; 
                if(dict.contains(temp) && !visited.contains(temp)) 
                { 
                    curNum++; 
                    queue.offer(temp); 
                    visited.add(temp); 
                } 
            } 
        } 
        if(lastNum==0) 
        { 
            lastNum = curNum; 
            curNum = 0; 
            level++; 
        } 
    } 
    return 0; 
} 

http://www.programcreek.com/2012/12/leetcode-word-ladder/
So we quickly realize that this is a search problem, and breath-first search guarantees the optimal solution.

word-ladder

Java Solution

class WordNode{
    String word;
    int numSteps;
 
    public WordNode(String word, int numSteps){
        this.word = word;
        this.numSteps = numSteps;
    }
}
 
public class Solution {
    public int ladderLength(String beginWord, String endWord, Set<String> wordDict) {
        LinkedList<WordNode> queue = new LinkedList<WordNode>();
        queue.add(new WordNode(beginWord, 1));
 
        wordDict.add(endWord);
 
        while(!queue.isEmpty()){
            WordNode top = queue.remove();
            String word = top.word;
 
            if(word.equals(endWord)){
                return top.numSteps;
            }
 
            char[] arr = word.toCharArray();
            for(int i=0; i<arr.length; i++){
                for(char c='a'; c<='z'; c++){
                    char temp = arr[i];
                    if(arr[i]!=c){
                        arr[i]=c;
                    }
 
                    String newWord = new String(arr);
                    if(wordDict.contains(newWord)){
                        queue.add(new WordNode(newWord, top.numSteps+1));
                        wordDict.remove(newWord);
                    }
 
                    arr[i]=temp;
                }
            }
        }
 
        return 0;
    }
}

Basically a solution using two "fronts" moving from start and end and trying to meet to determine the shortest path.

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        # This function uses two fronts, one starting from beginWord and moving forward while the other
        # starting from endWord and moving backward. Each time we push the smaller front and see if it will
        # touch the other front. If they meet, we have found the shortest path and return. Otherwise, we
        # update the front as well as its travelling distance (the level)
        
        # Each element is a 2-element list, representing the front and its travelling distance.
        # The first element represents the front to update while the second the front to stay on hold
        fronts = [[set([beginWord]),1],[set([endWord]),1]]
        wordList.discard(beginWord)
        wordList.discard(endWord)
        
        def updateFront():
            nextFront = set()
            for w in fronts[0][0]:
                for i in xrange(len(w)):
                    for c in string.lowercase:
                        if w[i] != c:
                            newWord = w[:i] + c + w[i+1:]
                            if newWord in fronts[1][0]:
                                return fronts[0][1]+fronts[1][1]
                            if newWord in wordList:
                                nextFront.add(newWord)
                                wordList.remove(newWord)
            fronts[0][1] += 1
            fronts[0][0] = nextFront    
            return None    
            
        while fronts[0][0] and fronts[1][0]:
            if len(fronts[0][0]) > len(fronts[1][0]):
                fronts.reverse() # start from smaller front
            ret = updateFront()
            if ret:
                return ret
        return 0
Somehow I could not get it running faster and beat the top gun (around 100ms). I submitted the same code a couple of time and it always falls around 116~120 ms. Any suggestions?

our code is really good. I did some tweak and it goes around 100ms now. Best I got is 92 ms.

def ladderLength(self, beginWord, endWord, wordList):
    fronts = [{beginWord}, {endWord}]
    levels = [1, 1]
    while fronts[0] and fronts[1]:
        if len(fronts[0]) > len(fronts[1]):
            fronts.reverse()
            levels.reverse()
        newLevel = set()
        for word in fronts[0]:
            for i in xrange(len(beginWord)):
                for char in string.lowercase:
                    newWord = word[:i] + char + word[i + 1:]
                    if newWord in fronts[1]:
                        return levels[0] + levels[1]
                    if newWord in wordList:
                        newLevel.add(newWord)
                        wordList.remove(newWord)
        fronts[0] = newLevel
        levels[0] += 1
    return 0

# 37 / 37 test cases passed.
# Status: Accepted
# Runtime: 92 ms


class Solution {
public:
struct Node;

typedef Node* NodePtr; // there is a memory leak, for some reason there is no shared_ptr :)
typedef unordered_map<string, NodePtr> KeyNodeMapT;
typedef unordered_map<string, vector<string>> PrefixMapT;

struct Node {
    unordered_set<NodePtr> children;
    string word;
};

inline NodePtr getOrCreateNode(KeyNodeMapT& nodesMap, const string& word) {
    if (nodesMap.find(word) == nodesMap.end()) {
        auto node = new Node();
        node->word = word;
        nodesMap.insert(make_pair(node->word, node));
        return node;
    }
    
    return nodesMap.at(word);
}

string shift(const string& word, int sh) {
    if (sh == 0) {
        return word;
    }
    
    sh = sh % word.length();
    
    string shWord = word.substr(sh, word.npos) + word.substr(0, sh);
    
    return shWord;
}

KeyNodeMapT createGraphM(vector<string>& dict, size_t wordLength) {
    KeyNodeMapT nodesMap;
    
    for (const string& lword : dict) {
        getOrCreateNode(nodesMap, lword);
    }
    
    for (int sh = 0; sh < wordLength; sh++) {
        
        PrefixMapT prefixMap;
        
        for (const string& word : dict) {
            if (word.length() > 1) {
                string shWord = shift(word, sh);
                string shWordPrefix = shWord.substr(0, shWord.length() - 1);
                
                prefixMap[shWordPrefix].push_back(word);
            } else if (word.length() == 1) {
                prefixMap[""].push_back(word);
            }
        }
        
        for (const auto& pr : prefixMap) {
            const auto& vecOfSimilar = pr.second;
            if (vecOfSimilar.size() > 1) {
                for (const auto& lword : vecOfSimilar) {
                    auto lnode = getOrCreateNode(nodesMap, lword);
                    
                    for (const auto& rword : vecOfSimilar) {
                        if (lword != rword) {
                            auto rnode = getOrCreateNode(nodesMap, rword);
                            lnode->children.insert(rnode);
                            rnode->children.insert(lnode);
                        }
                    }
                }
            }
        }
    }
    
    return nodesMap;
}

int dijkstra(const KeyNodeMapT& nodes, const string& start, const string& end) {
    unordered_map<string, int> costs;
    
    for (const auto& node : nodes) {
        costs[node.first] = INT_MAX;
    }
    
    const auto& startNode = nodes.at(start);
    costs.at(startNode->word) = 0;
    
    int cost = 1;
    unordered_set<NodePtr> children = startNode->children;
    
    while (children.size() > 0) {
        
        unordered_set<NodePtr> grandsons;
        
        for (const auto& child : children) {
            if (costs.at(child->word) > cost) {
                costs[child->word] = cost;
            }
            
            for (const auto& grandson : child->children) {
                if (costs.at(grandson->word) > cost + 1) {
                    grandsons.insert(grandson);
                }
            }
        }
        
        cost++;
        children = std::move(grandsons);
        
    }
    
    return costs.at(end);
}

int ladderLength(string start, string end, unordered_set<string> &dict) {
    vector<string> wordsV(dict.begin(), dict.end());
    wordsV.push_back(start);
    wordsV.push_back(end);
    
    size_t wordSize = wordsV[0].length();
    
    auto nodes = createGraphM(wordsV, wordSize);
    int length = dijkstra(nodes, start, end);
    
    if (length == INT_MAX) return 0;
    
    return length + 1;
}

};

trie

ach node has a termination symbol, which is used to detect if the parents create a valid word. We see in this structure that we can create ANTS, ANT, AND, AN, A as valid words. A trie provides efficient lookup time by allowing the ability to check prefixes of a word. i.e. if an doesn’t exist in the trie, then ants obviously can’t either.

A better dictionary has been found, but it doesn’t solve our permutation issue.

What if there was a way to calculate all permutations prior to running the search? It is a dictionary after all, and dictionaries don’t change often/at all. But then there’s the question, if we calculate all of the permutations of each word, how do we store it efficiently? We can’t have a 250,000 word dictionary listing up to 26* \text{wordlength} possible permutations per word in a file, because well for one, the file size would be too large to consider valuable, and two, the object would be too big to traverse reasonably.

New plan of attack – let’s split the dictionary up into smaller dictionaries based on word length, as a ladder can only be a specific word length anyways, then using these smaller dictionaries, provide access to permutations of each word.

We’ll look to a very low-level concept to store these permutations. 32-bit integers.

Who? What? How?

Yes. This was a concept I only vaguely understood until this problem. We will store the permutations of a single word in binary using an integer.

Let’s use our example again, Dog. Dog has 3 letters, and thus, 3 wildcards possible: ‘og’, ‘d_g’, and ‘do‘. For each of these wildcards we calculate what letters exchanged with the wildcard, create a new word.

So for ‘_og’ we have: bog, cog, fog, hog, jog, log, mog, nog, tog, wog

Or specifically, the letters: b, c, f, h, j, l, m, n, t, w

Which we can then map to binary

http://blog.acupajoe.io/word-ladder-data-structure-challenge/