### Python solution
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeros = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append([i, j])


        # set zeroes

        for case in zeros:
            for i in range(n):
                # row fixed
                matrix[case[0]][i] = 0
            
            for i in range(m):
                # col fixed
                matrix[i][case[1]] = 0
```
