class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            countMap[num] = 1+countMap.get(num,0)

        top_k = [k for k,_ in sorted(countMap.items(), key=lambda x:x[1], reverse=True)][:k]
        return top_k