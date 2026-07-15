class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        intervals.sort(key=lambda x:x.start)
        for i in range(len(intervals)-1):
            cur_start, cur_end = intervals[i].start, intervals[i].end
            next_start, next_end = intervals[i+1].start, intervals[i+1].end
            if next_start < cur_end:
                return False
        return True