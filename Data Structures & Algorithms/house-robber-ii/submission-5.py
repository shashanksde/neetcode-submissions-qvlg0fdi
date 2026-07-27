class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        def helper(arr):
            if not arr: return 0
            if len(arr) == 1: return arr[0]
            rob1 = arr[0]
            rob2 = max(arr[0], arr[1])

            for num in arr[2:]:
                tmp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2
        
        return max(helper(nums[:len(nums)-1]), helper(nums[1:]))