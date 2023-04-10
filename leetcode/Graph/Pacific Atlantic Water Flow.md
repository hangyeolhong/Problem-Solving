### Python solution
```python
# list - in: O(n)
# set, dict - in: O(1) ***
# set은 hashtable 기반 자료구조이기 때문에 list처럼 선형적으로 탐색하지 않음

# O(m * n * 2 * (m + n)) = O(m * n * (m + n))

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        result = []
        pac, atl = set(), set()

        def dfs(x, y, visited, h):
            if (x, y) in visited or x < 0 or x >= m or y < 0 or y >= n or heights[x][y] < h:
                return

            visited.add((x, y))
            dfs(x + 1, y, visited, heights[x][y])
            dfs(x - 1, y, visited, heights[x][y])
            dfs(x, y + 1, visited, heights[x][y])
            dfs(x, y - 1, visited, heights[x][y])


        for c in range(n):
            dfs(0, c, pac, heights[0][c])
            dfs(m - 1, c, atl, heights[m - 1][c])
        
        for r in range(m):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, n - 1, atl, heights[r][n - 1])

        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    result.append([i, j])

        return result
```

### Explanation
- find overlap of cells that are visited by both pac and atl cells
- two visited set: pat, atl
