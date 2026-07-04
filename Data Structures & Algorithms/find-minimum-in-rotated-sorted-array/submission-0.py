import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        m= sys.maxsize
        for i in nums:
            if (i<m):
                m = i
        return m
        