### Python solution
```python
# caching + dfs

#1. dict
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        d = {}

        def dfs(x, y, prev):
            if x < 0 or x >= m or y < 0 or y >=n or matrix[x][y] <= prev:
                return 0

            if (x, y) in d:
                return d[(x, y)]

            up = dfs(x - 1, y, matrix[x][y])
            down = dfs(x + 1, y, matrix[x][y])
            left = dfs(x, y - 1, matrix[x][y])
            right = dfs(x, y + 1, matrix[x][y])

            d[(x, y)] = 1 + max(up, down, left, right)
            return d[(x, y)]

        answer = 0
        for i in range(m):
            for j in range(n):
                res = dfs(i, j, -1)
                answer = max(answer, res)

        return answer
        
#2. 2d-list
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
```

### Explanation
- Dfs + dp
