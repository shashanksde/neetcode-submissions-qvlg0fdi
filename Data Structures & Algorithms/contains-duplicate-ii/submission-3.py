class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        seen = set()
        for right,num in enumerate(nums):
            while abs(right-left)>k:
                seen.remove(nums[left])
                left+=1
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False