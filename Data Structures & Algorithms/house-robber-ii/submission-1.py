class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)

        def helper(arr):
            rob1,rob2=0,0
            for n in arr:
                temp = max(n+rob1,rob2) #at the third house we can 
                #pick from third house and first or just second and move
                rob1 = rob2
                rob2 = temp
            return rob2 #as this will be the last value stored
        return max(helper(nums[:len(nums)-1]), helper(nums[1:]))      
        '''
        I can pick first house and move until last but one house 
        since the last house is adjacent to the first house

        if I pick the second house its adjacent to the first thus need to rob alternate houses
        '''