class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS,COLS = len(heights), len(heights[0])
        pacific_set = set()
        atlantic_set = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(row,col,visited):
            if (row, col) in visited:
                return
            
            visited.add((row,col))

            for r,c in directions:
                newr, newc = row+r, col+c
                #this will only explore valid cells and with a certain condition only
                if 0<=newr<ROWS and 0<=newc<COLS and heights[newr][newc]>=heights[row][col]:
                    dfs(newr, newc, visited)
            return

        #pacific
        for r in range(ROWS):
            #column 0
            dfs(r,0, pacific_set)
        
        for c in range(COLS):
            #row 0
            dfs(0, c, pacific_set)
        
        #atlantic
        for r in range(ROWS):
            #last column
            dfs(r, COLS-1,atlantic_set)
        
        for c in range(COLS):
            #last row
            dfs(ROWS-1, c, atlantic_set)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific_set and (r,c) in atlantic_set:
                    # print("entering here")
                    res.append([r,c])
        
        return res
        '''
        for top row and left col from pacific ocean side see 
        which cells can be reached by moving up,left,down and right
        movement condition is next cell has to be >= current cell value
        once visited add it to pacific visit set

        similarly for last row and last column see which cells can be visited
        and add it to atlantic set

        finally traverse the grid and see which row and col is in both set and
        add to result

        return the result.
        '''