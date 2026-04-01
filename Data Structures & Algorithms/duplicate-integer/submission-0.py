class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)
        # seen = set()
        # for num in nums:
        #     if num not in seen:
        #         seen.add(num)
        #     else:
        #         return True

        # return False