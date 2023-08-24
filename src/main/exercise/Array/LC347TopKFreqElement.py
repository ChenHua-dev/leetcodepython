from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        sorted_d = sorted(d.items(), key=lambda x:x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(sorted_d[i][0])
        return res
