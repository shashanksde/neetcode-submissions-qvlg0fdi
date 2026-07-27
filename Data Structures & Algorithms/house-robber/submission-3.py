class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])

        for num in nums[2:]:
            tmp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = tmp
        return rob2