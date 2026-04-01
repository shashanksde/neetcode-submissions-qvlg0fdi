class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1,rob2=0,0
        for n in nums:
            temp = max(n+rob1,rob2) #at the third house we can 
            #pick from third house and first or just second and move
            rob1 = rob2
            rob2 = temp
        return rob2 #as this will be the last value stored