class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charmap = defaultdict(int)
        res = 0
        maxval = 0
        l=0
        for r in range(len(s)):
            charmap[s[r]]+=1
            maxval = max(maxval, charmap[s[r]])
            while (r-l+1) - maxval > k:
                charmap[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res