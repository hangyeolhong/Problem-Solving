# O(m * n)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        answer = 0
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '#' or grid[x][y] == 0:
                return 0

            grid[x][y] = '#'
            u = dfs(x + 1, y)
            d = dfs(x - 1, y)
            r = dfs(x, y + 1)
            l = dfs(x, y - 1)

            return u + d + r + l + 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    answer = max(answer, dfs(i, j))


        return answer
