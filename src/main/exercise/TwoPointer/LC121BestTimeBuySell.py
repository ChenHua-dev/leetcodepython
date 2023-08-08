from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            sell_price = prices[i]
            if sell_price > buy_price:
                profit = max(profit, sell_price - buy_price)
            else:
                # update the buy price when the price is lowest
                # hence whenever there is a price that is lower than
                # the initial price, then update it to be the buy price
                buy_price = sell_price
        return profit
