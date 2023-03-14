### Python solution
```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.answer = []
        self.dfs(1, [], k, n)
        return self.answer
        

    def dfs(self, idx, res, k, n):
        if len(res) == k:
            if sum(res) == n:
                self.answer.append(res)
            return

        if idx == 10:
            return

        for i in range(idx, 10):
            if sum(res) + i <= n:
                self.dfs(i + 1, res + [i], k, n)
```
