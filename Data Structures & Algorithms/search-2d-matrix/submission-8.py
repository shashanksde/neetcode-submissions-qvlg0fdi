class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1 #these are indices, be careful in
        def binary_search(arr):
            l,r = 0, len(arr)-1
            while l<=r:
                mid = (l+r)//2
                if target==arr[mid]:
                    return True
                elif target<arr[mid]:
                    r=mid-1
                else:
                    l=mid+1
            return False

        while top<=bot:
            mid = (top+bot)//2
            if target<matrix[mid][0]:
                bot = mid-1
            elif target>matrix[mid][-1]:
                top = mid+1
            else:
                return binary_search(matrix[mid])
        return False