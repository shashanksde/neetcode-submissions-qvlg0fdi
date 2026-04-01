class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        
        needMap, haveMap = {}, {}
        for c in t:
            needMap[c] = 1 + needMap.get(c,0)
        
        need, have = len(needMap), 0
        res, resLen = [-1,-1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            haveMap[c] = 1 + haveMap.get(c,0)

            if c in needMap and haveMap[c]==needMap[c]:
                have+=1

            while have==need:
                #potential result, update res
                if (r-l+1)<resLen:
                    res = [l, r]
                    resLen = r-l+1
                #remove from left
                haveMap[s[l]]-=1
                if s[l] in needMap and haveMap[s[l]]<needMap[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float('inf') else ""

        