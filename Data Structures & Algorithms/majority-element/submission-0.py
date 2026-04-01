class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqMap = defaultdict(int)
        maxVal = float('-inf')
        maxkey = 0
        for num in nums:
            freqMap[num] = 1+freqMap.get(num,0)
            if freqMap[num]>maxVal:
                maxVal = freqMap[num]
                maxkey = num
        return maxkey
        

