class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        smallest = prices[0]

        profit = 0

        for i in prices:
            profit = max(profit, i - smallest)
            smallest = min(smallest, i)
        
        return profit