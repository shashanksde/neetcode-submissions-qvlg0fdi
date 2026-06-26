class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_complete(rate):
            if rate == 0: return False
            hours_taken = 0
            for p in piles:
                hours = math.ceil(p/rate)
                hours_taken+=hours
            if hours_taken<=h:
                return True
            else:
                return False

        min_rate, max_rate = 1, max(piles)
        res = max_rate
        while min_rate<=max_rate:
            mid_rate = (min_rate+max_rate)//2

            if can_complete(mid_rate):
                max_rate = mid_rate-1
                res = mid_rate
            else:
                min_rate = mid_rate+1
        return res