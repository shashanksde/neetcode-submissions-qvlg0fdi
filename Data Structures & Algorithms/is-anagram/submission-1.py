class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_arr = [0]*26
        t_arr = [0]*26

        for i in range(len(s)):
            #get index of char at i for s and t
            idx_s = ord(s[i])-ord('a')
            idx_t = ord(t[i])-ord('a')
            s_arr[idx_s]+=1
            t_arr[idx_t]+=1
        
        for i in range(len(s_arr)):
            if s_arr[i] != t_arr[i]:
                return False
        return True

#TC: O(n) but two pass solution
#SC: O(1) since for any string we will have atmost 26 len array
