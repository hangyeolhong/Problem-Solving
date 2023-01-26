class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)  # dp[i]: minumum number of squares to get i

        for i in range(1, n + 1):
            mn = 1e9
            for j in range(1, int(i ** (1 / 2)) + 1):
                if mn > dp[i - j*j] + 1:
                    mn = dp[i - j*j] + 1
            dp[i] = mn

        return dp[n]
        
