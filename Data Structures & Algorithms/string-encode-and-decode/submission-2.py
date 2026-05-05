class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            encoded_str = str(length)+"#"+s #solves the case when # can be in the middle of the string
            res+=encoded_str
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!="#": #because length can be multiple digits long
                j+=1
            length = int(s[i:j]) #here j will be at #
            #now we need to capture the string that starts at j after # till j+length
            res.append(s[j+1:j+1+length])
            i = j+1+length #start of the next string
        return res
