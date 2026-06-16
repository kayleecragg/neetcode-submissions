class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit, L = 0, 0

        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L = R
            profit = prices[R] - prices[L]
            bestProfit = max(bestProfit, profit)

        return bestProfit        