class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            length = len(word)
            word = str(length)+"#"+word
            res+=word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            #collect the length of the string
            j=i
            num = ""
            while j<len(s) and ord('0')<=ord(s[j])<=ord('9'):
                num += s[j]
                j+=1
            num = int(num)
            i = j
            i+=1
            word = s[i:i+num]
            res.append(word)
            i += num

        return res