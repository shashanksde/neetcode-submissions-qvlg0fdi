class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        numset = set(nums)
        if len(numset)<2:
            return len(numset)
        maxlen = 1
        for num in list(set(nums)):
            if (num-1) not in numset:
                #start counting from here
                l=1 #includes current number length
                n=num
                while (n+1) in numset:
                    l+=1
                    maxlen = max(maxlen, l)
                    n+=1
        return maxlen