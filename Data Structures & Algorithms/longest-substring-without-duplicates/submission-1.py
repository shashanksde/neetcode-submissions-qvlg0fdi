class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        seen = set()
        l = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l]) #start removing from the left
                l+=1 # move pointer towards right
            seen.add(s[r])
            maxlength = max(maxlength, r-l+1)
        return maxlength

        