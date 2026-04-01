class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_dict = {n:0 for n in nums}
        maj_ele = 0
        maj_len = len(nums)//2
        for i,n in enumerate(nums):
            maj_dict[n]+=1
            if maj_dict[n]>maj_len:
                maj_ele = n
        return maj_ele
        

