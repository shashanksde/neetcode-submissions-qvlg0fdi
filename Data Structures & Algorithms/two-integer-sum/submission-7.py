class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxmap = {}
        for i, val in enumerate(nums):
            if target-val in idxmap:
                return [idxmap[target-val], i]
            idxmap[val] = i
            
        '''
        keep a hashmap with {val:index}
        for each value check 
            if target - num exists in the hashmap
                if yes return [idx, cur_idx]
            else:
                add current value and index to map
        
        '''