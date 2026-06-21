class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resmap = defaultdict(list)
        for word in strs:
            chararr = [0]*26
            for c in word:
                chararr[ord(c)-ord('a')]+=1
            chararr = tuple(chararr)
            resmap[chararr].append(word)
        
        res = []
        for val in resmap.values():
            res.append(val)
        return res