class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        maxArea = 0
        visited = set()
        def bfs(row, col):
            q = deque()
            visited.add((row, col))   # ← mark here, not just in the loop
            q.append([row, col])
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            area = 1 #this is for the cell we just added
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newr, newc = row+dr, col+dc
                    if 0<=newr<ROWS and 0<=newc<COLS and grid[newr][newc]==1 and (newr,newc) not in visited:
                        visited.add((newr, newc))
                        q.append([newr, newc])
                        area+=1
            print(area)
            return area
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]==1 and (row, col) not in visited:
                    area = bfs(row, col)
                    islands+=1
                    print(islands)
                    maxArea = max(maxArea, area)

        return maxArea if islands else 0
