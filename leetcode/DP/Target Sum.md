### Python solution
```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(idx, total):
            if idx == len(nums):
                return 1 if total == target else 0

            if (idx, total) in dp:
                return dp[(idx, total)]

            dp[(idx, total)] = dfs(idx + 1, total + nums[idx]) + dfs(idx + 1, total - nums[idx])

            return dp[(idx, total)]

        return dfs(0, 0)
```

### 비슷한 문제 (dfs + dp)
[백준 1520: 내리막길](https://www.acmicpc.net/problem/1520)
```python
import sys, math
from collections import deque

M, N = map(int, sys.stdin.readline().rstrip().split())
graph = []

for _ in range(M):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
dp = {}


def dfs(x, y):
    if x == M - 1 and y == N - 1:
        return 1

    if (x, y) in dp:
        return dp[(x, y)]

    path = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= M or ny < 0 or ny >= N:
            continue
        if graph[nx][ny] < graph[x][y]:
            path += dfs(nx, ny)
            
    dp[(x, y)] = path
    return dp[(x, y)]


print(dfs(0, 0))

```
