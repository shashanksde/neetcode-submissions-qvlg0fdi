class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights: return 0
        
        l,r = 0 , len(heights)-1
        leftMax = heights[l]
        rightMax = heights[r]
        res = 0
        while l<r:
            if leftMax<rightMax:
                l+=1
                leftMax = max(leftMax, heights[l])
                res+=leftMax-heights[l]
            else:
                r-=1
                rightMax = max(rightMax, heights[r])
                res+=rightMax-heights[r]
            

        return res





                




        '''
        insight:
        water can only be trapped if there are two peaks 
        water can only be filled upto minimum of two heights between any two pointers
        move pointers toward higher value but l<r
        move right pointer toward equal height or higher
        calculate area between l and r only when r is equal to higher than l until then accumulate water
        if we reach the end cannot find a r that is higher than l then area=0
        '''