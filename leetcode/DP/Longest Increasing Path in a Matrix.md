### Python solution
```python
# caching + dfs
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)]

        def dfs(x, y):
            if dp[x][y]:
                return dp[x][y]

            up = dfs(x - 1, y) if x - 1 >= 0 and matrix[x - 1][y] > matrix[x][y]  else 0
            down = dfs(x + 1, y) if x + 1 < M and matrix[x + 1][y] > matrix[x][y]  else 0
            left = dfs(x, y - 1) if y - 1 >= 0 and matrix[x][y - 1] > matrix[x][y] else 0
            right = dfs(x, y + 1) if y + 1 < N and matrix[x][y + 1] > matrix[x][y] else 0

            dp[x][y] = max(up, down, left, right) + 1

            return dp[x][y]

        res = []
        for i in range(M):
            for j in range(N):
                res.append(dfs(i, j))

        return max(res)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = {}

        def dfs(x, y, val):
            if x < 0 or x >= M or y < 0 or y >= N or matrix[x][y] <= val:
                return 0

            if (x, y) in dp:
                return dp[(x, y)]
            
            res = 1
            res = max(res, 1 + dfs(x + 1, y, matrix[x][y]))
            res = max(res, 1 + dfs(x - 1, y, matrix[x][y]))
            res = max(res, 1 + dfs(x, y + 1, matrix[x][y]))
            res = max(res, 1 + dfs(x, y - 1, matrix[x][y]))
            dp[(x, y)] = res
            return res

        for i in range(M):
            for j in range(N):
                dfs(i, j, -1)

        return max(dp.values())
"""
```
