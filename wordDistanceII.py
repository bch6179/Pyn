class WordDistance:
    def __init__(self, words):
        self.dic = {}
        for index, w in enumerate(words):
            self.dic[w] = self.dic.get(w, []) + [index]

    def shortest(self, word1, word2):
        return min(abs(i1 - i2) for i1 in self.dic[word1] for i2 in self.dic[word2])