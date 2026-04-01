class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #store [index, height]

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index # the incoming height can be extended left until the one we popped
            stack.append((start, h))

        #at the end some elements can remain in stack
        #these are the ones which can be extended all the way to the right
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i)) 
        return maxArea
        