from heapq import heapify, heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k: #to keep the size of the min heap constant
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #first add to the min heap
        if len(self.minHeap) > self.k: #if the length of the min heap goes over the k length we pop again
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


