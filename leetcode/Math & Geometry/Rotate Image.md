### Python solution
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        self.n = len(matrix)
        self.transpose()
        self.reverse()
    
    def transpose(self):
        for i in range(self.n):
            for j in range(i + 1, self.n):
                self.matrix[i][j], self.matrix[j][i] = self.matrix[j][i], self.matrix[i][j]

    def reverse(self):
        for i in range(self.n):
            for j in range(self.n // 2):
                self.matrix[i][j], self.matrix[i][-1 - j] = self.matrix[i][-1 - j], self.matrix[i][j]
```
