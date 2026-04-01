class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = 0
        if len(grid)==0:
            return islands
        maxArea = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        def bfs(r,c,area):
            q = deque()
            q.append((r,c))
            visit.add((r,c)) #added the row, col where it started
            while q:
                row, col = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for r, c in directions:
                    r,c = r+row, c+col
                    if r>=0 and c>=0 and r<rows and c<cols and grid[r][c]==1 and (r,c) not in visit:
                        area+=1
                        visit.add((r,c)) #adding row and col where it went
                        q.append((r,c))

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    islands+=1
                    area = bfs(r,c,1)
                    maxArea = max(maxArea, area)
        
        return maxArea if islands else 0


