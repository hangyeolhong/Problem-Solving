# Tip: Reverse thinking is helpful. (Only A == Everything except B)
# Solving problems based on the border. 

from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])
        q = deque()

        # Capture unsurrounded regions
        for j in range(n):
            if board[0][j] == "O":
                q.append([0, j])
            if board[m - 1][j] == "O":
                q.append([m - 1, j])

        for i in range(m):
            if board[i][0] == "O": 
                q.append([i, 0])
            if board[i][n - 1] == "O":
                q.append([i, n - 1])

        
        # bfs (O -> #)
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

        while q:
            x, y = q.popleft()
            board[x][y] = '#'

            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                
                if board[nx][ny] == "O":
                    q.append([nx, ny])

        # Capture surrounded regions & Uncapture unsurrounded regions
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

        return board
