class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1 #initial goal
        #starting from the last but one
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal: #if from ith pos we can atleast reach the goal or beyond its good
                goal = i #move the goal now here to i not the end
        return goal == 0 #could we move our goal post to the first index? if so then we can reach the end from here