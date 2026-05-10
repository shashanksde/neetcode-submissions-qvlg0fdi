class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charmap = defaultdict(int)
        res = 0
        l=0
        for r in range(len(s)):
            charmap[s[r]]+=1
            while (r-l+1) - max(charmap.values()) > k:
                charmap[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res