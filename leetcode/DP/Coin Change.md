### Python solution
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [2 ** 31 - 1] * (amount + 1)

        dp[0] = 0

        for i in range(amount + 1):
            # i를 만들 때 coin 몇 개를 쓸 수 있는지
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == 2 ** 31 - 1:
            return -1
        else:
            return dp[amount]
```
