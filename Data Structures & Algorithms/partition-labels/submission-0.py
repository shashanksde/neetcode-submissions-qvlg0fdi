class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexMap = defaultdict(list)
        for i in range(len(s)):
            if s[i] not in indexMap:
                indexMap[s[i]].append(i)
        for i in range(len(s)-1,-1,-1):
            if len(indexMap[s[i]]) == 1:
                indexMap[s[i]].append(i)
        
        indexList = list(indexMap.values())
        stack = [indexList[0]]
        for i in range(1,len(indexList)):
            curStart = indexList[i][0]
            curEnd = indexList[i][1]
            prevStart = stack[-1][0]
            prevEnd = stack[-1][1]
            if curStart<=prevEnd:
                prevEnd = max(prevEnd, curEnd)
                stack[-1][1] = prevEnd
            else:
                stack.append([curStart, curEnd])
        res = []
        for val in stack:
            window = val[1]-val[0]+1
            res.append(window)
        return res
        #get the start and end index of each character
        # x:[0,3] y:[1,4] ->merge to get[0,4]
        # z:[5,7] b:[6,9]
        # i:[10,10] s:[11,11] l:[12,12]