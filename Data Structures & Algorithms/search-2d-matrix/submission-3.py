class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        def findRow(matrix):
            rows = len(matrix)
            low = 0
            high= rows-1
            while low<=high:
                mid = (low+high)//2
                row = matrix[mid]
                firstval, lastval = row[0], row[-1]
                print(firstval,lastval)
                if firstval<=target<=lastval:
                    #exists in this row, return row itself
                    return row
                elif target>lastval:
                    #exists in row next to mid
                    low=mid+1
                else:
                    high=mid-1
            return []
        
        def exists(row):
            low,high=0,len(row)-1
            while low<=high:
                mid = (low+high)//2
                midval = row[mid]
                if target<midval:
                    high=mid-1
                elif target>midval:
                    low=mid+1
                else:
                    return True
            return False
        
        rowtosearch = findRow(matrix)
        if len(rowtosearch)==0:
            return False
        if exists(rowtosearch):
            return True
        else:
            return False
