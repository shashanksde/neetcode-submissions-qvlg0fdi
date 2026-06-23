class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        maxlen = 0
        l=0
        for r in range(len(s)):
            
            while l<=r and s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxlen = max(maxlen, r-l+1)
        return maxlen