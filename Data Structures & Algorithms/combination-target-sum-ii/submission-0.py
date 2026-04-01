class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #the same index cannot be chosen multiple times
        #and the combination base case is that the target is reached,
        #if idx goes out of bounds or total > target happens we need to stop
        res = []
        candidates.sort() #this step is important for skipping duplicates
        def backtrack(comb, idx, cursum):
            if cursum==target:
                res.append(comb.copy())
                return
            
            if cursum>target or idx==len(candidates):
                return
            
            comb.append(candidates[idx])
            backtrack(comb,idx+1,cursum+candidates[idx])
            comb.pop()
            
            #this loop is important to skip duplicates
            while idx+1<len(candidates) and candidates[idx]==candidates[idx+1]:
                idx+=1
            backtrack(comb, idx+1, cursum) #here I have skipped all of the values and not included in the cursum
        
        backtrack([],0,0)
        return res
        



