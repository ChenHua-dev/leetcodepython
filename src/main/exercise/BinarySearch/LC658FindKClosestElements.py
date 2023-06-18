from typing import List


class Solution:
    def searchClosestElementToTarget(self, arr: List[int], target: int) -> int:
        if target <= arr[0]:
            return 0
        if target >= arr[len(arr) - 1]:
            return len(arr) - 1

        lo, hi = 0, len(arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target > arr[mid]:
                lo = mid + 1
            elif target < arr[mid]:
                hi = mid - 1
            else:
                return mid
        return lo if abs(target - arr[lo]) < abs(target - arr[hi]) else hi

    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     if len(arr) == k:
    #         return arr
    #
    #     boundary = self.searchClosestElementToTarget(arr, x)
    #     left = boundary - 1
    #     right = left + 1
    #
    #     # k is the window size
    #     while right - left - 1 < k:
    #         # Be careful to not go out of bounds
    #         if left == -1:
    #             right += 1
    #             continue
    #
    #         # Expand the window towards the side with the closer number
    #         # Be careful to not go out of bounds with the pointers
    #         if right == len(arr) or abs(arr[left] - x) <= abs(arr[right] - x):
    #             left -= 1
    #         else:
    #             right += 1
    #
    #     # Return the window
    #     return arr[left + 1:right]

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr

        index_closest_to_target = self.searchClosestElementToTarget(arr, x)
        left = index_closest_to_target
        right = left

        window_size = right - left + 1
        while window_size < k:
            if left <= 0:
                right += 1
            elif right >= len(arr) - 1:
                left -= 1
            elif abs(arr[left-1] - x) <= abs(arr[right+1] - x):
                left -= 1
            else:
                right += 1
            window_size = right - left + 1
        # Return the window
        return arr[left:right+1]


if __name__ == '__main__':
    s = Solution()
    print(s.findClosestElements([1, 2, 3, 4, 5], 4, 3))  # expect [1,2,3,4]
    print(s.findClosestElements([1, 2, 3, 4, 5], 4, -1))  # expect [1,2,3,4]
    print(s.findClosestElements([1, 1, 1, 10, 10, 10], 1, 9))  # expect [10]
    print(s.findClosestElements([0, 0, 1, 2, 3, 3, 4, 7, 7, 8], 3, 5))  # expect [3,3,4]
    print(s.findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9))  # expect [3,6,8,8,9]
