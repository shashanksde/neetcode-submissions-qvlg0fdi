class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0 
        maxlength = 0
        for right in range(len(s)):
            #keep window valid
            while left<=right and s[right] in seen:
                seen.remove(s[left])
                left+=1
            
            seen.add(s[right])
            window = right - left + 1
            maxlength = max(maxlength, window)
        
        return maxlength
            