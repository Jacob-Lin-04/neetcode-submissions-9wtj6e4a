class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # keep track of minimum price and max profit
        min_price = 100 
        max_profit = 0
        
        for R in range(len(prices)):
            min_price = min(prices[R], min_price)

            profit = (prices[R] - min_price)

            if profit > max_profit:
                max_profit = profit
            
        return max_profit
        