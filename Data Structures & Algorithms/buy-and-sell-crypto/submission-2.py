class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest_price = prices[0]
        max_profit = 0

        """
        Now, we loop through the prices. For every single price, we ask two simple questions:
        Question A: Is this price lower than the lowest_price I've seen so far? If yes, update lowest_price.
        Question B: If I bought at my lowest_price and sold at today's price, is that profit higher than my current max_profit? If yes, update max_profit.
        """

        for price in prices:
            if price < lowest_price:
                lowest_price = price

            if (price - lowest_price ) > max_profit:
                max_profit = price - lowest_price

        return max_profit


        
        