class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_complete(rate):
            total_hours = 0
            for p in piles:
                hours_taken = math.ceil(p/rate)
                total_hours+=hours_taken
            
            if total_hours>h:
                return False
            else:
                return True
        
        min_rate, max_rate = 1, max(piles)
        res = float('inf')
        while min_rate<=max_rate:
            mid_rate = (min_rate+max_rate)//2

            if can_complete(mid_rate):
                res = min(res, mid_rate)
                max_rate = mid_rate-1
            else:
                min_rate = mid_rate+1
        return res