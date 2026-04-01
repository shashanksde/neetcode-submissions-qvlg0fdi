class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxlen = 0
        seen = set()
        for r in range(len(s)):
            #keep window valid
            while s[r] in seen:
                seen.remove(s[l])
                l+=1

            seen.add(s[r])
            window = r-l+1
            maxlen = max(maxlen, window)
            
        return maxlen
