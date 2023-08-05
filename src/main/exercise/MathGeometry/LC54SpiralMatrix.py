from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix:
            return res
        top_index = 0
        bottom_index = len(matrix) - 1
        left_index = 0
        right_index = len(matrix[0]) - 1

        while top_index <= bottom_index and left_index <= right_index:
            for i in range(left_index, right_index + 1):
                res.append(matrix[top_index][i])
            top_index += 1

            for i in range(top_index, bottom_index + 1):
                res.append(matrix[i][right_index])
            right_index -= 1

            if top_index <= bottom_index:
                for i in range(right_index, left_index - 1, -1):
                    res.append(matrix[bottom_index][i])
                bottom_index -= 1

            if left_index <= right_index:
                for i in range(bottom_index, top_index - 1, -1):
                    res.append(matrix[i][left_index])
                left_index += 1
        return res
