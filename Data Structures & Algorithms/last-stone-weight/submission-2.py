class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        heapq.heapify(maxheap)
        for stone in stones:
            heapq.heappush(maxheap, -stone)
        
        while len(maxheap)>1:
            x,y=heapq.heappop(maxheap), heapq.heappop(maxheap)
            x,y = abs(x), abs(y)
            if x==y:
                continue
            elif x<y or y<x:
                remains = abs(y-x)
                heapq.heappush(maxheap, -remains)
        
        return -maxheap[0] if len(maxheap)==1 else 0
