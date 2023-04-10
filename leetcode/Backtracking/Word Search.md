### Python solution
```python
# Time complexity: O(rows * cols * 4 ^(len(word)) )

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visit = set()

        def dfs(x, y, idx):
            if idx == len(word):
                return True
            if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visit or board[x][y] != word[idx]:
                return False

            visit.add((x, y))
            if dfs(x + 1, y, idx + 1) or dfs(x - 1, y, idx + 1) or dfs(x, y + 1, idx + 1) or \
                dfs(x, y - 1, idx + 1):
                return True

            visit.remove((x, y))

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
```
