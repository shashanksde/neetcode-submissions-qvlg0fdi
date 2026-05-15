class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(row):
            left, right = 0, len(matrix[row])-1
            while left<=right:
                mid = (left+right)//2 #index
                val = matrix[row][mid]
                if val>target:
                    right = mid-1
                elif val<target:
                    left = mid+1
                else:
                    return True
            return False

        #find row to search
        top, bot = 0 , len(matrix)-1
        while top<=bot:
            row = (top+bot)//2
            firstval , lastval= matrix[row][0], matrix[row][-1] #first and last val of that row
            
            if target<firstval:
                bot = row-1
            elif target>lastval:
                top = row+1
            else:
                break

        if not (top<=bot):
            return False
        
        row = (top+bot)//2
        return binary_search(row)


