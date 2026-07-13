class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, sum_val, comb):
            nonlocal res
            if sum_val == target:
                res.append(comb.copy())
                return
            
            if i >= len(candidates) or sum_val > target:
                return
            
            # make a decision to add current number to the comb
            comb.append(candidates[i])
            dfs(i+1, sum_val+candidates[i], comb)
            comb.pop()

            # skip duplicates for the "not include" branch
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, sum_val, comb)
            return

        dfs(0,0,[])
        return res