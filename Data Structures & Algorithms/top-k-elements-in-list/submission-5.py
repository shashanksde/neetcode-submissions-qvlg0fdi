class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = defaultdict(int)
        for num in nums:
            freqmap[num] = 1+freqmap.get(num,0)
        
        maxheap = [] #[-freq, val]
        heapq.heapify(maxheap)
        for num, freq in freqmap.items():
            heapq.heappush(maxheap, [-freq, num])
        
        #now form the results
        res = []
        while k>0:
            nums = heapq.heappop(maxheap)[1]
            res.append(nums)
            k-=1

        return res