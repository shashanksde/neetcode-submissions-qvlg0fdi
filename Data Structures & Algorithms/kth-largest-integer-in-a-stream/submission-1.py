class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        self.maxheap = [-num for num in nums]
        heapq.heapify(self.maxheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.maxheap, -val)
        cnt = self.k
        res = 0
        addback = []
        while cnt:
            num = heapq.heappop(self.maxheap)
            addback.append(num) #will be negative
            res = -num
            cnt-=1
        
        for i in range(len(addback)):
            heapq.heappush(self.maxheap, addback[i])

        return res

        

            
