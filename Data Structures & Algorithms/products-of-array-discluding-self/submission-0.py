class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        if i take a prefix product array and postfix product array

        prefix array   [1, 2,  8,  48]
        postfix array  [6, 24, 48, 48] 
                       [48, 48, 24, 6] in reverse
        output 

        '''
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
            
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix *=nums[i]
        return res


