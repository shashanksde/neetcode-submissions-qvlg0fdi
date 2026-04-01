class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)  #key=freqs val=words

        for word in strs:
            freq = [0]*26
            for c in word:
                freq[ord(c)-ord('a')]+=1  #67-65 = 2
            freq = tuple(freq)
            anagrams[freq].append(word)

        return list(anagrams.values())
        
