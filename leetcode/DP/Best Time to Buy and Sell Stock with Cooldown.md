### Python solution
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # caching + dfs
        dp = {}

        def dfs(i, is_buying):
            if i >= len(prices):
                return 0

            if (i, is_buying) in dp:
                return dp[(i, is_buying)]

            if is_buying:
                buy = dfs(i + 1, False) - prices[i]
                cool_down = dfs(i + 1, True)
                dp[(i, is_buying)] = max(buy, cool_down)
            else:
                sell = dfs(i + 2, True) + prices[i]
                cool_down = dfs(i + 1, False)
                dp[(i, is_buying)] = max(sell, cool_down)
                
            return dp[(i, is_buying)]

        return dfs(0, True)
```

### Explanation
- after buy, we have to sell.
    - $\therefore$ ```buy = dfs(i + 1, False) - prices[i]```
- after sell, we have to buy buy. 
    - $\therefore$ ```sell = dfs(i + 2, True) + prices[i]```
