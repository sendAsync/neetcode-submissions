class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float("inf")
        ans =0
        for i,price in enumerate(prices):
            min_val = min(min_val, price)
            ans = max(ans, price - min_val)
        return ans

        