class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        for i in range(m-1): #loop through m-1 rows only since row=[1]*n means from the last row
        #there is only one way to move right towards the goal
            newRow = [1]*n #this one is needed to calculate the value above
            for j in range(n-2,-1,-1):
                #_this value depends on value in next col-> 1
                #and the row below it  
                #1
                newRow[j] = newRow[j+1]+row[j]
            row = newRow
        return row[0]
