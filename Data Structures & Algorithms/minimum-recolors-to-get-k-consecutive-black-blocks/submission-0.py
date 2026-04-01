class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #minimum number of flips I need to make in order to have 7 blacks in a row
        #expand first window of length k -> count W in it 
        #just count how many 'W's in each window
        #return the count in min window
        whites = 0
        minlen = float('inf')
        l=0
        for r in range(len(blocks)):
            if blocks[r]=="W":
                whites+=1
            if r-l+1==k:
                minlen = min(whites, minlen)
                if blocks[l]=="W":
                    whites-=1
                l+=1
        return minlen