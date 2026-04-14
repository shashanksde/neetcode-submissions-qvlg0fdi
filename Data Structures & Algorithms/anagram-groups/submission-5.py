class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        plan:
        create tuples as key (0,1,0,0,0 etc) value : word
        then go through values in the hashmap to print them out
        '''
        anamap = defaultdict(list)
        for word in strs:
            w = [0]*26
            for c in word:
                idx = ord(c)-ord('a')
                w[idx]+=1
            w = tuple(w)
            anamap[w].append(word)
        
        res = [words for words in anamap.values()]
        return res
        