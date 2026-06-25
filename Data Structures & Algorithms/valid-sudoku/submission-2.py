class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])
        rowset = [set() for _ in range(ROWS)]
        colset = [set() for _ in range(COLS)]
        boxset = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val==".":
                    continue
                if val in rowset[r] or val in colset[c] or \
                    val in boxset[r//3][c//3]:
                    return False
                else:
                    rowset[r].add(val)
                    colset[c].add(val)
                    boxset[r//3][c//3].add(val)
        return True