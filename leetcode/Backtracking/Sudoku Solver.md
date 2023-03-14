### Python solution
```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def checkRow(x, row):
            for i in range(9):
                if board[row][i] == x:
                    return False
            return True


        def checkCol(x, col):
            for i in range(9):
                if board[i][col] == x:
                    return False
            return True
        

        def checkRect(x, row, col):
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] == x:
                        return False
            return True

        void = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    void.append([i, j])


        def dfs(idx):
            if idx == len(void):
                return True

            r, c = void[idx]

            for num in range(1, 10):
                if checkRow(str(num), r) and checkCol(str(num), c) and checkRect(str(num), 3 * (r // 3), 3 * (c // 3)):
                    board[r][c] = str(num)
                    if dfs(idx + 1): return True
                    board[r][c] = "."
            return False

        dfs(0)
        print(board)
```
