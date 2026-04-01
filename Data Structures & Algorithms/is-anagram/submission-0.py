class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        sMap = {}
        for c in s:
            sMap[c] = 1 + sMap.get(c,0)
        
        for c in t:
            if c in sMap:
                sMap[c]-=1
        
        for val in sMap.values():
            if val!=0:
                return False
        return True