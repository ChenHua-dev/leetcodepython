from typing import List


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda x:x[0])

        for i in range(1, len(intervals)):
            interval_1 = intervals[i-1]
            interval_2 = intervals[i]

            if interval_1[1] > interval_2[0]:
                return False
        return True
