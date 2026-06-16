class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        L = 0

        for R in range(len(prices)):
            profit = prices[R] - prices[L]
            bestProfit = max(bestProfit, profit)
            if prices[R] < prices[L]:
                L = R

        if bestProfit == 0: 
            return 0
        return bestProfit        