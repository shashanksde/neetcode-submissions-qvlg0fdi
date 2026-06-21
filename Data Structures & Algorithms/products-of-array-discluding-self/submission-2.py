class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prearr = [1]*len(nums)
        postarr = [1]*len(nums)
        for i in range(len(nums)):
            prearr[i] = prearr[i-1]*nums[i] if i>0 else nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            postarr[i] = postarr[i+1]*nums[i] if i<len(nums)-1 else nums[i]
        
        res = [1]*len(nums)

        for i in range(len(prearr)):
            if i>0 and i<len(prearr)-1:
                res[i] = prearr[i-1]*postarr[i+1]
            else:
                if i==0:
                    res[i]= postarr[i+1]
                elif i==len(prearr)-1:
                    res[i] = prearr[i-1]
        return res