class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i >= k - 1:
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)
                output.append(-heap[0][0])
        return output
        # maxHeap = [-nums[i] for i in range(k)]
        # heapq.heapify(maxHeap)
        # res = []
        # res.append(-maxHeap[0])
        # l=0
        # for r in range(k, len(nums)):
        #     heapq.heappush(maxHeap, -nums[r])

        #     while r-l+1<k and len(maxHeap)>k:
        #         maxele = heapq.heappop(maxHeap)*-1
            
        #     res.append(maxele)
        # return res
            
        #have a constant size map
        #every time we see a new element we push to the heap 
        #while the size of heap >k we pop from heap
        #as we move the window insert new element remove the element from left, peek top to have the highest element