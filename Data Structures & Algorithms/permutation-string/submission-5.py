class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        s1map,s2map = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            s1map[s1[i]] = 1+s1map.get(s1[i],0)
            s2map[s2[i]] = 1+s2map.get(s2[i], 0)
        
        for r in range(len(s1), len(s2)):
            if s1map==s2map:
                return True
            
            s2map[s2[r]] +=1
            s2map[s2[r-len(s1)]]-=1
            if s2map[s2[r-len(s1)]] == 0: 
                del s2map[s2[r-len(s1)]]
        return s1map == s2map