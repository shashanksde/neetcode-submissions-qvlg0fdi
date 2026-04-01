class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, maxLength = 0,0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            maxLength = max(maxLength, r-l+1)
        return maxLength 

            