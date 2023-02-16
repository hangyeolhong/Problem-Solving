from collections import deque

# Time, space complexity: O(m * n)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        q = deque()
        fresh_oranges = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    # rotten orange
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fresh_oranges += 1


        # bfs
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        time = 0

        while q and fresh_oranges:
            for _ in range(len(q)):
                x, y = q.popleft()
                
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if nx < 0 or nx >= m or ny < 0 or ny >= n:
                        continue
                    
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        q.append([nx, ny])
            time += 1

        
        return time if not fresh_oranges else -1
