class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        def valid(char):
            c = ord(char)
            return ord('A')<=c<=ord('Z') or ord('a')<=c<=ord('z') or ord('0')<=c<=ord('9')
        l,r=0,len(s)-1
        while l<=r:
            if valid(s[l]) and valid(s[r]):
                if s[r]!=s[l]:
                    return False
                l+=1
                r-=1
            elif valid(s[l]) and not valid(s[r]):
                r-=1
            elif not valid(s[l]) and valid(s[r]):
                l+=1
            else:
                l+=1
                r-=1
        return True