class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #build a prefix tree
        # see where the words diverge
        res = ""
        for i in range(len(strs[0])):
            for s in strs: #for all strings
                if i==len(s) or s[i]!=strs[0][i]: 
                    #if any string goes out of bounds then 
                    #that is the maximum we can match
                    return res
            res+=strs[0][i] #until here its common
        return res