from typing import List

class Solution:
    def firstOccurrence(self, nums: List[int], target: int) -> int:
        index = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                index = mid
                hi = mid - 1
        return index

    def lastOccurrence(self, nums: List[int], target: int) -> int:
        index = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if target > nums[mid]:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid - 1
            else:
                index = mid
                lo = mid + 1
        return index

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.firstOccurrence(nums, target), self.lastOccurrence(nums, target)]


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10], 8))  # [3, 4]
    # print(s.firstOccurrence([1,2,3,5,7,8,8,8,8,10], 8))  # [5, 8]
    # print(s.lastOccurrence([1,2,3,5,7,8,8,8,8,10], 8))  # [5, 8]
    # print(s.firstOccurrence([1,2,3,8,8,8,8,8,8,10], 8))  #
    # print(s.lastOccurrence([1,2,3,8,8,8,8,8,8,10], 8))  #
    # print(s.firstOccurrence([1,2,3,8,8], 8))  #
    # print(s.lastOccurrence([1,2,3,8,8], 8))  #
    # print(s.firstOccurrence([1,1,1,1,1,1,1,3,8,8,8,8,8,8], 1))  #
    # print(s.lastOccurrence([1,1,1,1,1,1,1,3,8,8,8,8,8,8], 1))  #
