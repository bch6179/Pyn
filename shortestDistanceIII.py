1 ... Java "short"

i1 and i2 are the indexes where word1 and word2 were last seen. Except if they're the same word, then i1 is the previous index.

public int shortestWordDistance(String[] words, String word1, String word2) {
    long dist = Integer.MAX_VALUE, i1 = dist, i2 = -dist;
    for (int i=0; i<words.length; i++) {
        if (words[i].equals(word1))
            i1 = i;
        if (words[i].equals(word2)) {
            if (word1.equals(word2))
                i1 = i2;
            i2 = i;
        }
        dist = Math.min(dist, Math.abs(i1 - i2));
    }
    return (int) dist;
}
Solution 2 ... Java "fast"

Same as solution 1, but minimizing the number of string comparisons.

public int shortestWordDistance(String[] words, String word1, String word2) {
    long dist = Integer.MAX_VALUE, i1 = dist, i2 = -dist;
    boolean same = word1.equals(word2);
    for (int i=0; i<words.length; i++) {
        if (words[i].equals(word1)) {
            if (same) {
                i1 = i2;
                i2 = i;
            } else {
                i1 = i;
            }
        } else if (words[i].equals(word2)) {
            i2 = i;
        }
        dist = Math.min(dist, Math.abs(i1 - i2));
    }
    return (int) dist;
}