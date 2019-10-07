class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = None
        ans = 0
        for price in prices:
            if min_price is None:
                min_price = price
            else:
                ans = max(ans, price - min_price)
                min_price = min(min_price, price)
        return ans
