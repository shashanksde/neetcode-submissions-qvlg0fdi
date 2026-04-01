class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {point:[] for point in range(N)}

        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1, N):
                x2,y2=points[j]
                dist = abs(x1-x2)+abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])

        visit = set()
        res = 0
        minheap = [[0,0]] #[cost, point]
        while len(visit)<N:
            cost, point = heapq.heappop(minheap)
            if point in visit:
                continue
            res+=cost
            visit.add(point)
            for neicost, nei in adj[point]:
                heapq.heappush(minheap, [neicost, nei])

        return res