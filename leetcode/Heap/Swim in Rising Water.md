### Python solution
```python
import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # least time -> bfs
        # You can swim infinite distances in zero time.

        q = [[grid[0][0], 0, 0]]
        N = len(grid)
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        grid[0][0] = -1     # visited

        while q:
            d, x, y = heapq.heappop(q)
            # print(d, x, y)
            if x == N - 1 and y == N - 1:
                return d

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                    
                if grid[nx][ny] != -1:
                    heapq.heappush(q, [max(d, grid[nx][ny]), nx, ny])
                    grid[nx][ny] = -1     # visited

        return -1
```
