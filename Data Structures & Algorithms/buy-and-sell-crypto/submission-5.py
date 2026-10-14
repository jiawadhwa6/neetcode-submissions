class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1

        maxp = 0
        while r < len(prices):
            buy = prices[l]  
            sell = prices[r]
            if buy <= sell:
                maxp = max(maxp, sell - buy)
                r+=1
            elif buy > sell:
                l=r
                r+=1

        return maxp


        