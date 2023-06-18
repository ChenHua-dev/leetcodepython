from typing import List

class Solution:
    """
    <target> and an integer array <arr> sorted in non-descending order
    Find index in <arr> s.t. arr[i] is closest to given <target>.
    Return -1 if there is no element in the array.

    An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
    """
    def indexOfClosestElement(self, arr: List[int], target: int) -> int:
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


if __name__ == '__main__':
    s = Solution()
    print(s.indexOfClosestElement([1, 2, 3], 2))  # expect 1
    print(s.indexOfClosestElement([1, 4, 6], 3))  # expect 1
    print(s.indexOfClosestElement([1, 4, 6], 5))  # expect 1
    print(s.indexOfClosestElement([1, 4, 4, 5], 3))  # expect 1
    print(s.indexOfClosestElement([1, 2, 2, 4, 8], 3))  # expect 2
