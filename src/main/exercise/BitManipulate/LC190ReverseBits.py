class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0b0
        mask = 0b1
        for i in range(32):
            temp = n & mask
            temp = temp << (31 - i)
            # print('{:032b}'.format(temp))
            res = res | temp
            # mask = mask << 1 # this is wrong approach, use n >> 1
            n = n >> 1
        return res
