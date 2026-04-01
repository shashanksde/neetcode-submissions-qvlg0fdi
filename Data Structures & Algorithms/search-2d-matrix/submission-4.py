class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        find which row to look at 
        within that row apply binary search 
        if found return True else False
        '''
        def binarysearch(row, l,r):
            while l<=r:
                mid = (l+r)//2
                if target>matrix[row][mid]:
                    l = mid+1
                elif target<matrix[row][mid]:
                    r = mid-1
                else:
                    return True
            return False


        lrow, rrow = 0, len(matrix)-1
        while lrow<=rrow:
            mid = (lrow+rrow)//2
            cols = len(matrix[mid])
            if target>matrix[mid][0] and target>matrix[mid][cols-1]:
                lrow = mid+1
            elif target<matrix[mid][0]:
                rrow = mid-1 
            else:
                return binarysearch(mid, 0, len(matrix[mid])-1)
        
        return False
