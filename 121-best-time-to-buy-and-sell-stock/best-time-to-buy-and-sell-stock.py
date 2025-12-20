class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        max_diff = 0

        for i in prices:
            min_price = min(min_price, i)
            max_diff = max(max_diff, i - min_price)

        return max_diff 