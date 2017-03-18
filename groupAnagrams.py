    def groupAnagrams(self, strs):
        # write your code here
        dict = {}
        if strs == [""]:
            return [[""]]
        for word in strs:
            sortedword = ''.join(sorted(word))
            dict[sortedword] = [word] if sortedword not in dict else dict[sortedword] + [word]
        res = []
        for item in dict:
            if len(dict[item]) >= 1:
                res.append(dict[item])
        return res

     def groupAnagrams(self, strs): #for 2+ anagrams
        # write your code here
        dict = {}
        res = []
        if strs == [""]:
            return [[""]]
        for word in strs:
            sortedword = ''.join(sorted(word))
            if sortedword not in dict:
                
                dict[sortedword] = i  
            else:
                
                res.append(word)
                if dict[sortedword] >= 0:
                    res.append(strs[dict[sortedword]])
                dict[sortedword] = -1