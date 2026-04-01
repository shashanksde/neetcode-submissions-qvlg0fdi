class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        maxArea = (right-left)*min(heights[left], heights[right])

        while left<right:
            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
            
            #calculate area
            area = (right-left)*min(heights[left], heights[right])
            maxArea = max(maxArea, area)
        return maxArea
        