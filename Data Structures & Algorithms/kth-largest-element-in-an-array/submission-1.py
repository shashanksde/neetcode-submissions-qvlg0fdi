class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #keep pushing to the max heap
        #pop k times
        #return the element
        maxheap = [-num for num in nums]
        heapq.heapify(maxheap)
        res = float('inf')
        while k>0:
            res = heapq.heappop(maxheap) * -1
            k-=1
        
        return res
            