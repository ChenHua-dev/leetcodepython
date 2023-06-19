from typing import List

class Solution:
    # def findPeakElement(self, nums: List[int]) -> int:
    #     if len(nums) <= 1: return 0
    #     index = -1
    #     lo, hi = 0, len(nums) - 1
    #     while lo <= hi:
    #         mid = lo + (hi - lo) // 2
    #         if nums[mid-1] > nums[mid]: # peak found
    #             index = mid - 1
    #             hi = mid - 1
    #         else:
    #             lo = mid + 1
    #     return len(nums) - 1 if index == -1 else index

    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] > nums[mid+1]:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    s = Solution()
    print(s.findPeakElement([1,2,3,1]))
    print(s.findPeakElement([1,2,1,3,5,6,4]))
    print(s.findPeakElement([1,2]))
    print(s.findPeakElement([2,1]))
    print(s.findPeakElement([1]))
    print(s.findPeakElement([6,5,4,3,2,3,2]))

