class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        if len(prices)==1:
            return maxp
        l,r=0,0
        while r<len(prices):
            if prices[r]<prices[l]:
                l=r
            else:
                maxp = max(maxp, prices[r]-prices[l])
                r+=1
        return maxp
