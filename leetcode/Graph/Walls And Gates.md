### Python solution
```python
from collections import deque
public class Solution {
    /**
     * @param rooms: m x n 2D grid
     * @return: nothing
     */
    public void wallsAndGates(int[][] rooms) {
        // write your code here
        m, n = len(rooms), len(rooms[0])

        q = deque()
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    visited[i][j] = True

        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

        dist = 0
        while q:
            for i in range(len(q)):
                x, y = q.popleft()
                rooms[x][y] = dist

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny] or rooms[nx][ny] == -1:
                        continue
                    
                    if rooms[nx][ny] == INF:
                        visited[nx][ny]= True
                        q.append((nx, ny))
            dist += 1
    }
}
```

### Explanation
```
BFS starting at multiple starting points simultaneously
  * KEY: for loop as much as <length of q>
  * Positions in the same for loop step have the same distance.
  * Use visited 2d matrix to avoid revisiting places that have been reached from other starting points (maintaining minimum distance).
```
