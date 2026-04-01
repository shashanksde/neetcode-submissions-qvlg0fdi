class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        key thing to note here is that the min val will be
        minval< nextval and minval<prevval
        check if left and right bound is valid if left bound is reached treat value as +inf same with right boundary
        '''
        res = nums[0]
        left, right = 0, len(nums)-1

        while left<=right:
            if nums[left]<nums[right]:
                #this can only happen if its already sorted
                # else it will look like this some number/ lowest| /max in a zagged manner /|/
                res = min(res, nums[left])
                break

            mid = (left+right)//2
            res = min(res, nums[mid])
            if nums[mid]>=nums[left]:
                #mid belongs to left sorted portion
                #move left pointer to right
                left = mid+1
            else:
                right = mid-1
        return res 