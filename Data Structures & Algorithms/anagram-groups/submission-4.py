class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #prepare a hashmap with key as (0,1,0,0) - > ["words"]
        #to get index where to put that use [0]*26 as the key
        #get ord of each character and place them at that index
        #finally return the values of the hashmap

        anagrams = {}
        for word in strs:
            key = [0]*26
            for c in word:
                idx = ord(c)-ord('a')
                key[idx] += 1
            key = tuple(key)
            if key not in anagrams:
                anagrams[key] = [word]
            else:
                anagrams[key].append(word)
        res = []
        for _, values in anagrams.items():
            res.append(values)
        
        return res