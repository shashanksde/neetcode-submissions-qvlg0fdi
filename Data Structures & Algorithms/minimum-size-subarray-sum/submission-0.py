class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        minlength = float('inf') #also can be len(nums)+1
        l=0
        for r in range(len(nums)):
            total+=nums[r]
            while total >=target:
                minlength = min(minlength, r-l+1)
                total-=nums[l]
                l+=1

        return minlength if minlength!=float('inf') else 0