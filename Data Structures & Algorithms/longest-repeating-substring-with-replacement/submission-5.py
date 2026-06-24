class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqmap = defaultdict(int) #char->occurence
        maxlen = 0
        l = 0
        for r in range(len(s)):
            freqmap[s[r]]+=1
            maxfreq = max(freqmap.values())
            windowlen = r-l+1
            while (windowlen-maxfreq) > k:
                freqmap[s[l]]-=1
                l+=1
                windowlen = r-l+1
                maxfreq = max(freqmap.values())
            maxlen = max(maxlen, r-l+1)
        return maxlen