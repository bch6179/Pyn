 
 https://leetcode.com/problems/sort-characters-by-frequency/#/description
Create a hashmap H1 of character to character frequency for the input string.
Iterate H1 to create hashmap H2 with key as frequency and value as substrings of repeated strings with length as the frequency.
Finally lookup all potential frequencies in decreasing order in H2 and produce the final result.
from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c1, c2 = Counter(s), {}
        for k,v in c1.items():
            c2.setdefault(v, []).append(k*v)
        return "".join(["".join(c2[i]) for i in range(len(s), -1, -1) if i in c2])


S shengyi2 
Reputation:  23
 public String frequencySort(String str) {
        if (str == null || str.length() <= 2) return str;
        Map<Character, Integer> map = new HashMap<>();
        char[] list = str.toCharArray();
        for (char c : list) {
            map.putIfAbsent(c, 0);
            map.put(c, map.get(c) + 1);
        }
        
        PriorityQueue<Character> heap = new PriorityQueue<>(str.length(), new Comparator<Character>() {
            public int compare(Character c1, Character c2) {
                return map.get(c2) - map.get(c1);
            }
        });
        
        for (char c : map.keySet()) {
            heap.offer(c);
        }
        
        StringBuilder sb = new StringBuilder();
        while (!heap.isEmpty()) {
            char c = heap.poll();
            int count = map.get(c);
            for (int i = 0; i < count; ++i) sb.append(c);
        }
        return sb.toString();

         Error Message:
Line 14: TypeError: bad operand type for unary -: 'unicode'
Last executed input:
"tree"

    def frequencySort2(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = collections.defaultdict(int)
        heap = []
        res = ''
        for c in s:
            dict[c] += 1
        
        for k, v in dict.iteritems():
            heapq.heappush(heap, (-v, k))
        while heap:
            v, k = heapq.heappop(heap)
            res += k*(-v)
        return res