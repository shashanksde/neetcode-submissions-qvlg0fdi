class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = set()
        colSet = set()
        boxSet = set()
        '''
        Iterate through the board and add it to the row, col and the box in which the number belongs to 
        - number shouldnt be duplicated in the same box [num, box]
        - number shouldnt be duplicated in the same column [num, col]
        - number shouldnt be duplicated in the same row [num, row]
        '''
        ROWS, COLS = len(board), len(board[0])
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col]==".":
                    continue
                box_row, box_col = row//3, col//3 #[1,0] for 4th row and 0th col
                num = int(board[row][col]) 
                if ((num, box_row, box_col) in boxSet) or ((num, row) in rowSet) or ((num, col) in colSet):
                    return False
                
                boxSet.add((num, box_row, box_col))
                rowSet.add((num, row))
                colSet.add((num,col))

        return True
