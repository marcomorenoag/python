from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0
        # left = right = 0
        # while left < len(prices) and right < len(prices):
        #     if prices[left] > prices[right]:
        #         left += 1
        #         right = left
        #     elif prices[left] <= prices[right]:
        #         profit = max(profit, prices[right] - prices[left])
        #         right += 1

        #     if right == len(prices) and left < right:
        #         left += 1
        #         right = left
        # return profit

        profit = 0
        min_price = float("inf")
        for price in prices:
            if price < min_price:
                min_price = price
            profit = max(profit, price - min_price)
        return profit
