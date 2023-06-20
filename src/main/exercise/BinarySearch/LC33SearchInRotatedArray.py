from typing import List


class Solution:
    def findPeak(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid+1]:
                return mid
            if nums[lo] < nums[hi]:
                lo = mid + 1
            else:
                if nums[mid] > nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid
        return hi

    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        peak_index = self.findPeak(nums) # binary search O(logn)

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[hi]:
                if target < nums[lo]:
                    lo = peak_index + 1
                else:
                    hi = peak_index
            elif nums[mid] < nums[lo]:
                if target > nums[hi]:
                    hi = peak_index
                else:
                    lo = peak_index + 1
            else:
                if target > nums[mid]:
                    lo = mid + 1
                elif target < nums[mid]:
                    hi = mid - 1
                else:
                    return mid
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search([4,5,6,7,0,1,2], 0))  # expect 4
    print(s.search([4,5,6,7,0,1,2], 3))  # expect -1
    print(s.search([1], 0))  # expect -1
    # print(s.findPeak([1,2,3]))  # expect 2
    # print(s.findPeak([4,5,6,7,8]))  # expect 4
    # print(s.findPeak([3,1,2]))  # expect 0
    # print(s.findPeak([2,3,1]))  # expect 1
    # print(s.findPeak([4,0,1,2,3]))  # expect 0
    # print(s.findPeak([4,5,0,1,2,3]))  # expect 1
    # print(s.findPeak([4,5,6,0,1,2,3]))  # expect 2
    # print(s.findPeak([4,5,6,7,0,1,2]))  # expect 3
    # print(s.findPeak([4,5,6,7,8,0,1,2]))  # expect 4
    # print(s.findPeak([4,5,6,7,8,1,2]))  # expect 4
    # print(s.findPeak([4,5,6,7,8,1]))  # expect 4
