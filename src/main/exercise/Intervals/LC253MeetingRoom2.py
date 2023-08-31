from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        res = 0
        count = 0

        s = 0
        e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
