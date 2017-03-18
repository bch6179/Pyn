only one index is needed

    def shortestDistance(self, words, word1, word2):
        ans = len(words)
        current_word, current_index = None, 0
        for index, word in enumerate(words):
            if word != word1 and word != word2: continue
            if current_word and word != current_word:
                ans = min(ans, index - current_index)
            current_word, current_index = word, index
        return ans