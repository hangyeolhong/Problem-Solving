### Python solution
```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(cur, idx):
            if (cur, idx) in dp:
                return dp[(cur, idx)]

            # termination condition
            if idx == len(nums):
                if cur == target:
                    # possible way
                    return 1
                else:
                    # impossible way
                    return 0

            dp[(cur, idx)] = dfs(cur + nums[idx], idx + 1) + dfs(cur - nums[idx], idx + 1)

            return dp[(cur, idx)]

        answer = dfs(0, 0)
        return answer
```

### Explanation
- ```dp[cur]``` doesn't work. Key must be ```(cur, idx)```.

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
