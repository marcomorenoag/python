from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for today in range(1, len(prices)):
            yesterday = today - 1
            if prices[today] > prices[yesterday]:
                profit += prices[today] - prices[yesterday]
        return profit

        """
        left = right = 0
        total_profit = 0
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                delta = max(max_profit, prices[right] - prices[left])
                if delta > max_profit:
                    total_profit += delta
                    left += 1
            if prices[left] > prices[right]:
                left += 1
            right += 1
        return total_profit
        """
