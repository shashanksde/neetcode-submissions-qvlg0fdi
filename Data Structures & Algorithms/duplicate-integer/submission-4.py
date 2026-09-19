class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        '''
        iterate over the array
        as you see new numbers check in the set if already exists
            if yes return true
            if no add to set
        at the end if true is not returned return false

        TC: O(n)
        SC: O(n)
        '''
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False