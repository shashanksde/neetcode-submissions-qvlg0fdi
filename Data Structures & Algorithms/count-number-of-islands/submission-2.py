class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        approach
        1. apply bfs starting from (x,y) increment island count by 1
        2. explore all the cells that can be reached from the given cell and add to visit cell
        3. if no more cells can be visited we stop
        4. return island count

        '''
        islands = 0
        ROWS , COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        directions = [[1,0],[-1,0],[0,-1],[0,1]]

        def bfs(row,col):
            nonlocal q,visited, directions
            
            visited.add((row, col))
            q.append([row, col])
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    newr, newc = row+dr, col+dc
                    #be careful of reverting the condition, if
                    if 0 <= newr < ROWS and 0 <= newc < COLS and grid[newr][newc] == "1" and (newr, newc) not in visited:
                        visited.add((newr, newc))
                        q.append([newr, newc])
                    else:
                        continue

            

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1

        return islands