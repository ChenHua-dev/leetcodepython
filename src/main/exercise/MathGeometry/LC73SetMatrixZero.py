from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW = len(matrix)
        COL = len(matrix[0])
        rows, cols = set(), set()

        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(ROW):
            for j in range(COL):
                if i in rows or j in cols:
                    matrix[i][j] = 0
