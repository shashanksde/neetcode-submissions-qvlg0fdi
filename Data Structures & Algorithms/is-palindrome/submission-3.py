class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<r:
            #we need whilee and not a if condition because 
            #as long as we see a nonalphanumeric value we move our pointers
            while l<r and not self.alphanum(s[l]):
                l+=1
            while r>l and not self.alphanum(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l,r=l+1, r-1
        return True
    
    #tells true if the current char is actually alphanumeric or not
    def alphanum(self, c):
        return (ord('A')<=ord(c)<=ord('Z') or
                ord('a')<=ord(c)<=ord('z') or
                ord('0')<=ord(c)<=ord('9'))
        '''
        consider only alphanumeric values 
        left and right pointer at the end of the string
        while s[left]!=alphanumeric we do l+=1
        else fo r-=1
        if it is a valid char at left and right we compare them, if they differ
        we return False
        - if they match we return True

        Bottleneck in brute force approach was that it made use of extra space
        while taking SC:O(n)
        but in the optimal approach we resolve that issue with the help of pointers
        '''