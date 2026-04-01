class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        if len(prices)==1:
            return maxprofit
        l=0
        for r in range(1,len(prices)):
            if prices[r]>prices[l]:
                profit = prices[r]-prices[l]
                maxprofit = max(maxprofit, profit)
            else:
                l=r
        return maxprofit   