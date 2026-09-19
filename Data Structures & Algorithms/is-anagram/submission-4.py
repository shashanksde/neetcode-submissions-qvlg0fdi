class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t): #if the length itself is different then they cannot match
            return False
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        #build the map
        for c in s:
            s_map[c]+=1
        for c in t:
            t_map[c]+=1
        
        if s_map != t_map: #after building if they are not the same even then we need to return false
            return False
        return True