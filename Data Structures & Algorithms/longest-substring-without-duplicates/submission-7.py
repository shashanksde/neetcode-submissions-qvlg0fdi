class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        res = float('-inf')
        l = 0
        for r in range(len(s)):
            #while the current char exists in set we shrink from left
            while s[r] in charset:
                charset.remove(s[l])
                l+=1

          # add current char to set 
            charset.add(s[r])
            #update len
            res = max(res, r-l+1) #this was why I was not getting the right answer, forgot to calculate correct window length
        return res if res!=float('-inf') else 0