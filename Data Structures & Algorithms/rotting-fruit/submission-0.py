class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                #update fresh
                if grid[r][c]==1:
                    fresh+=1
                #append rotten to que
                if grid[r][c]==2:
                    q.append((r,c))
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while q and fresh>0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for r, c in directions:
                    newr, newc = row+r, col+c
                    if newr<0 or newr==ROWS or newc<0 or newc == COLS or grid[newr][newc]!=1:
                        continue
                    grid[newr][newc] = 2
                    q.append((newr, newc))
                    fresh-=1
            time+=1
        
        return time if fresh==0 else -1