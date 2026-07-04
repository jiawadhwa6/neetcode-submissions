class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1 
        l_max = height[l]
        r_max = height[r]
        res = 0 
        while (l<r):
            if (l_max < r_max):
                l+=1
                l_max = max(height[l], l_max)
                if (r_max - height[r]>=0):
                    res += l_max -height[l]
            else:
                r-=1
                r_max = max(height[r], r_max)
                if (r_max - height[r]>=0):
                    res += r_max - height[r]
        return res

        