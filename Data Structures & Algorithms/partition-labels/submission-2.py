class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {} #char -> last index seen in s
        #preprocessing pass O(n)
        for i, ch in enumerate(s):
            lastIndex[ch] = i
        
        res = []
        size, end = 0, 0
        #since we know where the char will last be seen now
        #we can go ahead and find the partition length
        for i, c in enumerate(s):
            size+=1
            end = max(end, lastIndex[c])

            if i==end:
                res.append(size)
                size = 0
        return res