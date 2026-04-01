class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        l=0
        freqmap = {}
        for r in range(len(s)):
            freqmap[s[r]] = 1+freqmap.get(s[r],0)

            while l<=r and (r-l+1)-max(freqmap.values())>k:
                freqmap[s[l]] -= 1
                l+=1
            
            maxLen = max(maxLen, r-l+1)
        return maxLen
            