class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)  #assign a cache to store the length of the longest sequence starting from that index
        
        for i in range(len(nums) - 1, -1, -1): #starting from the last value
            for j in range(i + 1, len(nums)): #starting from the last element the longest increasing sequence will be just one
                if nums[i] < nums[j]: #if the element at j is greater than element at i then its increasing
                    LIS[i] = max(LIS[i], 1 + LIS[j]) #this means individually lis[i] is a sequence or that+LIS of starting from next indexes
        return max(LIS)