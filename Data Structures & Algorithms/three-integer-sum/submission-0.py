class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #O(nlogn)

        for i, val in enumerate(nums): #O(n^2)
            if i>0 and val == nums[i-1]:
                continue
            
            left,right = i+1, len(nums)-1
            while left<right:
                threeSum = val + nums[left] + nums[right]
                if threeSum > 0:
                    #move right pointer down
                    right-=1
                elif threeSum < 0:
                    #move left pointer up
                    left+=1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        #if they are duplicates
                        left+=1
        return res