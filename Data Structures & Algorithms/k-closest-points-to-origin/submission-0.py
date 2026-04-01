class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #first calculate distances from points p to origin
        #push the distance and point to the heap
        # heap will have min distances anyway
        #we can only keep track of the k minimum distance at all times 
        #as optimization.
        heap = []
        heapq.heapify(heap)
        for p in points:
            x, y = p[0], p[1]
            dist = math.sqrt(x**2+y**2)
            heapq.heappush(heap, [dist, [x,y]])
        #now pop
        res = []
        while k>0:#edge case 
            points = heapq.heappop(heap)
            res.append(points[1])
            k-=1
        return res 
        

