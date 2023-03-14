### Python solution
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.candidates = candidates

        self.candidates.sort()
        self.dfs([], 0, target)

        return self.answer


    def dfs(self, res, idx, target):

        if idx == len(self.candidates):
            return
        
        if sum(res) == target:
            self.answer.append(res)
            return
        
        for i in range(idx, len(self.candidates)):
            if sum(res) + self.candidates[i] <= target:
                self.dfs(res + [self.candidates[i]], i, target)
        
```
