class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                left_s,right_s = s[l:r],s[l+1:r+1]
                return left_s == left_s[::-1] or right_s == right_s[::-1]
        return True