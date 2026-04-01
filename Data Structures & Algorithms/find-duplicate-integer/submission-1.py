class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        [1,2,3,2,2] if I multiply them its 120 
        but i get 24 
        expected [1,2,6,12,24]
                 [1,2,6,24,120]
        '''
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return nums[i]
        