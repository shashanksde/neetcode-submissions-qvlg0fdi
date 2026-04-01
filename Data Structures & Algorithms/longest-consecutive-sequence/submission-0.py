class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        max_length = 0
        for n in nums:
            if (n-1) not in numset: #that means this n is the beginning of the sequence
            #count how many numbers occur until it breaks
                length=1
                while (n+length) in numset:
                    length+=1
                max_length = max(max_length, length) 
        return max_length