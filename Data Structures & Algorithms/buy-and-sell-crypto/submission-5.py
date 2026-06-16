class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        if len(prices)==1:
            return maxp
        
        l, r = 0, 1
        while r<len(prices):
            p = prices[r]-prices[l]
            maxp = max(maxp, p)
            if prices[r]<=prices[l]:
                l=r
            r+=1
        return maxp