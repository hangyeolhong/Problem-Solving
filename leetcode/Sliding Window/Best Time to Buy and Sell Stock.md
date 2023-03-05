### Python solution

```python

#1. two pointer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx_profit = 0
        left, right = 0, 1

        while right < len(prices):
            if prices[left] >= prices[right]:
                # cannot sell
                left = right
            else:
                # can sell stock, and update maximum profit
                if mx_profit < prices[right] - prices[left]:
                mx_profit = prices[right] - prices[left]
            
            right += 1

        return mx_profit
   
#2. sliding window
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res

```
