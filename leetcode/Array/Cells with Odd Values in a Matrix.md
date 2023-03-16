### Python solution
```python
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row, col = [0] * m, [0] * n
        
        for r, c in indices:
            row[r] += 1
            col[c] += 1

        cnt = 0
        for i in range(m):
            for j in range(n):
                if (row[i] + col[j]) % 2:
                    cnt += 1

        return cnt
```

### Explanation
```
Keep row and col list separately, so that time complexity becomes O(n + m + nm).
If using 2D matrix, time complexity becomes O(2*nm)
```
