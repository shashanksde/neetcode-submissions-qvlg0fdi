import math
class Solution:
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(rate):
            hoursTaken = 0
            for bananas in piles:
                #print(math.ceil(bananas/rate))
                hoursTaken+= math.ceil(float(bananas)/rate) 
                #i had to float division, i was doing int division and expecting ceil to work
            
            if hoursTaken>h:
                return False
            else:
                return True


        minrate, maxrate = 1, max(piles)
        while minrate<=maxrate:
            midrate = (minrate+maxrate)//2
            if canFinish(midrate):
                maxrate = midrate - 1
            else:
                minrate = midrate + 1

        return minrate

        '''
        goal is to find minimum eating rate such that i can eat all piles in h number of hours
        arange from 1 to max(piles) as array 
        pick a random mid eating rate , check how many hours it will take to complete all bananas
        eg : 25 bananas at eating rate of 4 will take ceil(25//4) = 7 hours which is already greater than hours allowed
        if cant finish increase eating rate
        if can finish decrease eating rate to see if there is any minimum rate at which it can be finished
        '''