class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        directions = [[1,0],[0,1],[0,-1],[-1,0]]
        minh = [[grid[0][0],0,0]] #[height, row, col]

        while minh:
            t,r,c = heapq.heappop(minh)

            if r==N-1 and c==N-1:
                return t
            for dr, dc in directions:
                neir, neic = r+dr, c+dc
                if (neir<0 or neic<0 or neir==N or neic==N or (neir,neic) in visit):
                    continue
                visit.add((neir, neic))
                heapq.heappush(minh, [max(t,grid[neir][neic]),neir, neic])
        