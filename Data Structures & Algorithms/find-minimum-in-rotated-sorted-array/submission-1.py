class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        res = nums[0]
        while l<=r:
            if nums[l]<nums[r]:
                res = min(res, nums[l])
                break

            mid = (l+r)//2
            res = min(res, nums[mid])

            if nums[mid]>=nums[l]:
                l = mid+1
            else:
                r = mid-1

        return res
            # if mid is greater than first element and first element is greater than last element
            #min must be in the right half
            # if [6,1,2,3,4,5]
            #if mid is smaller than first element search in the left half
