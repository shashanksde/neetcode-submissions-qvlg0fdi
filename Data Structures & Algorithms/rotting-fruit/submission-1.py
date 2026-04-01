class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        time = 0
        q = deque()
        # Step 1: Seed queue with ALL initially rotten oranges
        # This is the key to multi-source BFS — we start from every
        # rotten orange simultaneously, not one at a time
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]==2:
                    q.append([row,col])
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        # Step 2: Process layer by layer (each layer = 1 minute)
        # The outer while loop represents time passing
        # The inner for loop processes all cells at the SAME time step
        while q:
            infected_this_round = False  # Track if this layer did any work
            for _ in range(len(q)):
                cell = q.popleft()
                row, col = cell[0], cell[1]
                for dr, dc in directions:
                    newr,newc = row+dr, col+dc
                    # Skip: out of bounds, empty cells (0), or already rotten (2)
                    # We ONLY want to infect fresh oranges (1)
                    if newr<0 or newc<0 or newr>=ROWS or newc>=COLS or grid[newr][newc]!=1:
                        continue
                    # Infect the fresh orange and add to next layer
                    grid[newr][newc] = 2
                    q.append([newr,newc])
                    infected_this_round = True  # ✅ new infection happened
            if infected_this_round:
                time+=1
        
        # Step 3: If any fresh orange remains, it was unreachable
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1
        
        return time
                        



        #know which cells are rotten and place them in the queue
        #start bfs from each of the cell and go deep
        #count time for each layer processed
        #while encountering a neighbor which is 1 make them as 2
