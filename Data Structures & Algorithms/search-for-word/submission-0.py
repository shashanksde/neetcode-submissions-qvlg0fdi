class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #we iterate over the board to find the first character in the word
        #if there is match in a cell we mark that cell as visited
        #and run dfs from that location horizontally or vertically, 
        #if there is a match with the second character in the horizontal or vertical direction we continue
        #if not break and find a new start position if available
        #if through dfs we are able to reach the length of the word then we know we have found the word
        rows = len(board)
        cols = len(board[0])
        path = set()
        def dfs(i,j, idx):
            if idx==len(word):
                return True
            if i>=rows or i<0 or j>=cols or j<0 or word[idx]!=board[i][j] or (i,j) in path:
               return False
            
            path.add((i,j))
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            
            for dir_ in directions:
                row,col = dir_[0],dir_[1]
                if dfs(i+row,j+col,idx+1): #if any of the one direction results in found we return true
                    return True
                #this should run until all of the char match
            path.remove((i,j))
            return False
                
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0): #if starting from here we found the word then we can return True 
                    return True #else we can simply continue

        return False
