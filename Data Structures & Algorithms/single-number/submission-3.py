class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l=nums

        while len(l)>=1:
            curr = l.pop()
            if curr in l:
                l.remove(curr)
            else:
                return curr