class MedianFinder:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            return
        left = 0
        right = len(self.nums) - 1
        while left < right:
            mid = (left + right) // 2
            if self.nums[mid] == num:
                self.nums.insert(mid, num)
                return
            elif self.nums[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        if self.nums[left] < num:
            self.nums.insert(left + 1,num)
        else:
            self.nums.insert(left, num)

    def findMedian(self) -> float:
        mid = (0 + len(self.nums) - 1) // 2
        if (len(self.nums) - 1) % 2 == 0:
            return self.nums[mid]
        else:
            return (self.nums[mid] + self.nums[mid+1]) / 2
