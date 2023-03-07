### Python solution
```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_promising(x):
            for i in range(x):
                if col[i] == col[x] or abs(col[i] - col[x]) == abs(i - x):
                    return False
            return True

        def n_queens(x):
            if x == n:
                result.append(col[:])
                return True

            for i in range(n):
                col[x] = i
                if is_promising(x):
                    n_queens(x + 1)
            return False

        col = [0] * n
        result = []
        n_queens(0)
        r = []

        for case in result:
            tmp_r = []

            for nn in case:
                tmp = ["."] * n
                tmp[nn] = 'Q' 
                tmp_r.append(''.join(tmp))
            r.append(tmp_r)

        return r
```
