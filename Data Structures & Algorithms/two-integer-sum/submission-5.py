class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in numMap: #this is the previous number when added to val results in target
                return [numMap[diff],i]
            numMap[val] = i
        