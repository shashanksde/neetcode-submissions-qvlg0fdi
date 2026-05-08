class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res =[]
        nums.sort()

        for i, a in enumerate(nums):
            if a >0:
                break # break because once we reach a number that is positive
                #the following number is also positive since they are sorted, they  can never add upto zero
            if i>0 and a==nums[i-1]:
                continue
            
            l, r = i+1, len(nums)-1
            while l<r:
                threeSum =a + nums[l]+nums[r]
                if threeSum>0: #adding left and right with current became too large
                    r-=1
                elif threeSum<0: #adding left and right with current became too less
                    l+=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
