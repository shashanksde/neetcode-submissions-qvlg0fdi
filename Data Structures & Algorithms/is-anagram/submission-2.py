class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        smap, tmap = defaultdict(int), defaultdict(int)
        for c in s:
            smap[c] = 1+smap.get(c,0)
        for c in t:
            tmap[c] = 1+tmap.get(c,0)
        
        for c, cnt in smap.items():
            if c not in tmap or smap[c]!=tmap[c]:
                return False
        return True