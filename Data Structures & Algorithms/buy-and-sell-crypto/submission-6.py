class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Minimum price and maxProfit
        minPrice = prices[0]
        maxProfit = 0

        #Iterate through all prices
        for i in prices:
                if i < minPrice:
                    minPrice = i
            
                currentProfit = i - minPrice
                if currentProfit > maxProfit:
                    maxProfit = currentProfit
        
        #Return max_profit
        return maxProfit
