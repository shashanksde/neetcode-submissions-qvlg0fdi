class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() #this is the trick, if I can sort then I can skip all same elements
        
        def backtrack(i, comb, total):
            if total==target:
                res.append(comb.copy())
                return

            if i>=len(candidates) or total>target:
                return

            comb.append(candidates[i])
            backtrack(i+1, comb, total+candidates[i])
            comb.pop()
            '''
            since this second choice is to skip the element at ith loc, all elements that are same as nums[i] must also 
            be skipped such that this num doesnt appear in the comb at all
            '''
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtrack(i+1, comb, total)
        
        backtrack(0,[],0)
        return res