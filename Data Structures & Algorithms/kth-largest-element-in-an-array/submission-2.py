class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        heapq.heapify(minheap) #has the number as it is in it
        for num in nums:
            heapq.heappush(minheap, num)
            if len(minheap)>k:
                heapq.heappop(minheap)
        
        #here we will be left with k largest elements in the array,
        #so the top element will be the largest
        res = heapq.heappop(minheap)
        return res