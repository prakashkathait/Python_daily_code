class Solution(object):
    def maxProfit(self, prices):
        # Initialize variables
        min_price = float('inf')  # Start with a very high price (infinity)
        max_profit = 0  # Initially, the profit is 0 (no transaction made)
        for price in prices:
            # Update the minimum price if we find a lower price
            if price < min_price:
                min_price = price
            # Calculate the profit if we sold at the current price
            profit = price - min_price
            # Update the maximum profit if the calculated profit is greater
            if profit > max_profit:
                max_profit = profit
        
        return max_profit
        return profit