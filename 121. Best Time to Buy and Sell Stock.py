class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        # lowest price encountered so far in interation
        least_price = prices[0]
        
        for i in range(1, len(prices)):
            # case price is less than least encountered, new least
            if prices[i] < least_price:
                least_price = prices[i]
            
            else:
                profi = prices[i] - least_price
                if profi > max_profit:
                    max_profit = profi   
            
        return max_profit
            
        