class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1: #this means that we can split the nums group into two equal parts such that their sums are equal
            return False
        
        dp = set() #memoization step
        dp.add(0)
        target = sum(nums)//2 #eg:if sum of entire array is 10 , individual arrays should sum to 5
        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for t in dp:
                nextDP.add(t+nums[i]) #including the number at i 
                nextDP.add(t) #not including the number at i
            dp = nextDP #update cache with all the possible sums that we can arrive
        
        return True if target in dp else False