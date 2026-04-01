class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_w1,len_w2 = len(word1), len(word2)
        p1,p2 = 0, 0
        res = ""
        while p1<len_w1 and p2<len_w2:
            res+=word1[p1]
            res+=word2[p2]
            p1+=1
            p2+=1
        
        if p1<len_w1:
            res+=word1[p1:]
        
        if p2<len_w2:
            res+=word2[p2:]
        
        return res