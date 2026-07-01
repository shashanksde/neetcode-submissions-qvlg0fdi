class Solution:
    def trap(self, height: List[int]) -> int:
        trap = 0
        leftmax = [-1]*len(height)
        rightmax = [-1]*len(height)

        #update leftmax array
        curr_max = 0
        for i in range(len(height)):
            curr_max = max(curr_max, height[i])
            leftmax[i] = curr_max
        
        curr_max = 0
        for i in range(len(height)-1,-1,-1):
            curr_max = max(curr_max, height[i])
            rightmax[i] = curr_max
        
        for i in range(len(height)):
            trap += min(leftmax[i], rightmax[i]) - height[i]
        
        return trap