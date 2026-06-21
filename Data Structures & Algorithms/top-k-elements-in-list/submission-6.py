class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = defaultdict(int)
        for num in nums:
            freqmap[num] = 1+freqmap.get(num,0)
        
        minheap = [] #[-freq, val]
        heapq.heapify(minheap)
        for num, freq in freqmap.items():
            heapq.heappush(minheap, [freq, num])
            if len(minheap) > k: #keeps only k size 
                heapq.heappop(minheap)
        
        #now form the results
        res = []
        while minheap:
            res.append(heapq.heappop(minheap)[1])
        return res