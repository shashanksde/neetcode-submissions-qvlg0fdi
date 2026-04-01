class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            res[tuple(count)].append(word)
        
        return list(res.values())
        # for word in strs:
        #     sorted_word = sorted(word)
        #     sorted_word = "".join(sorted_word)
        #     anagramDict[sorted_word].append(word)
        
        # res = []
        # for val in anagramDict.values():
        #     res.append(val)
        # return res