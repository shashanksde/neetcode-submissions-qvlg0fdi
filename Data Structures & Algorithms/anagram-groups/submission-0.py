class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)
            anagramDict[sorted_word].append(word)
        
        res = []
        for val in anagramDict.values():
            res.append(val)
        return res