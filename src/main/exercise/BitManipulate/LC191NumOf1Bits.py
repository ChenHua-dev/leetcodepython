class Solution:
    def hammingWeight(self, n: int) -> int:
        num_of_ones = 0
        mask = 0b1

        for _ in range(32):
            temp = n & mask
            if temp == 1:
                num_of_ones += 1
            n = n >> 1
        return num_of_ones
