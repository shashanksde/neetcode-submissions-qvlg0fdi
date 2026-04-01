class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #build a min heap with (distances and co-ordinates)
        #after building pop k times and add to res
        if k>len(points):
            return []
        distances = [[math.sqrt(x**2+y**2), [x,y]] for x,y in points]
        heapq.heapify(distances)
        res = []
        while k>0:
            _, points = heapq.heappop(distances)
            res.append(points)
            k-=1

        return res