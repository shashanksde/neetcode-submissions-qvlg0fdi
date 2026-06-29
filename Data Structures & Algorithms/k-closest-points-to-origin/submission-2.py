class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculate_dist(x, y):
            return math.sqrt(x**2+y**2)
        
        maxheap = []
        heapq.heapify(maxheap)
        for point in points:
            x,y = point[0], point[1]
            dist = calculate_dist(x,y)
            heapq.heappush(maxheap, [-dist, [x,y]])
            if len(maxheap)>k:
                heapq.heappop(maxheap)
        
        res = []
        while maxheap:
            point = heapq.heappop(maxheap)[1]
            res.append(point)
        return res
