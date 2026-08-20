class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #track 3 things; min_price, profit, max_profit

        min_price=prices[0]
        profit=0
        max_profit=0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit

        return max_profit