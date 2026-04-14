class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: #new intervals ends before the start of the current interval
                res.append(newInterval)
                return res+intervals[i:] 
            elif newInterval[0]>intervals[i][1]: #new intervals begin sometime after the current interval ends
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res