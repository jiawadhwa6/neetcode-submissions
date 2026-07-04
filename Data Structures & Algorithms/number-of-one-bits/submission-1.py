class Solution:
    def hammingWeight(self, n: int) -> int:
        s = 0
        while n > 0:
            s += n & 1  # Add 1 to the count if the least significant bit is 1
            n = n >> 1  # right shift the number to check the next bit 
            # 1101 right shift 0110
        return s

        