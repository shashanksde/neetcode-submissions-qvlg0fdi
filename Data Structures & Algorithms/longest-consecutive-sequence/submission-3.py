class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numset: #start calculating length if its a start of a sequence.
                #it means start of a sequence
                length=0
                while (n+length) in numset:
                    length+=1
                longest = max(longest, length)

        return longest