class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        min eating rate would be smallest pile
        max eating rate would be max pile
        if i chose a random k in this range and check if at that rate I can finish the entire pile
        try to move as low k rate as possible if we find then update
        '''
        low = 1 
        high = max(piles)
        res = high
        while low<=high:
            k = (low+high)//2
            hourstaken = 0
            for p in piles:
                hourstaken+=math.ceil(p/k) #number of hours it will take to finish that pile
            if hourstaken<=h:
                #can potentially be the result
                res = min(res,k)
                high=k-1
            else:
                low=k+1
        
        return res