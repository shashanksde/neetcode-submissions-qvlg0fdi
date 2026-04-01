class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()
        def bfs(row, col):
            q = deque()
            visited.add((row, col))   # ← mark here, not just in the loop
            q.append([row, col])
            directions = [[1,0],[0,1],[-1,0],[0,-1]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newr, newc = row+dr, col+dc
                    if 0<=newr<ROWS and 0<=newc<COLS and grid[newr][newc]=="1" and (newr,newc) not in visited:
                        visited.add((newr, newc))
                        q.append([newr, newc])
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]=="1" and (row, col) not in visited:
                    bfs(row, col)
                    islands+=1

        return islands
