from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        is_contained = False
        if not matrix: return is_contained
        m, n = len(matrix), len(matrix[0])

        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            row = mid // n
            col = mid % n
            if target > matrix[row][col]:
                lo = mid + 1
            elif target < matrix[row][col]:
                hi = mid - 1
            else:
                is_contained = True
                break
        return is_contained


if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
