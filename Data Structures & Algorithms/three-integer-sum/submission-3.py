class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            #helps remove
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1, len(nums)-1
            while j<k:
                target = nums[j]+nums[k]
                if target> (-nums[i]):
                    k-=1
                elif target<(-nums[i]):
                    j+=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
        return list(res)