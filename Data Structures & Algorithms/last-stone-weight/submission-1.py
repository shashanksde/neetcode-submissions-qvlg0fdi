class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>=2:
            x = heapq.heappop(maxheap) * -1
            y = heapq.heappop(maxheap) * -1
            if x == y:
                continue
            else:
                if x<y:
                    heapq.heappush(maxheap, -(y-x))
                elif x>y:
                    heapq.heappush(maxheap, -(x-y))
        if len(maxheap)==0:
            return 0
        else:
            return -maxheap[0]

        #create a maxheap by having -ve values of stones 
        #to figure out the two highest weights pop 2 times 
        # x==y dont pushback anything
        # if x<y then push y-x
        # else push x-y
        # repeat until heapsize is atleast 2
         