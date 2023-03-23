### Python solution
```python
# Sol1
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

# Sol2
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(val, res, idx):
            if val == target:
                answer.append(res[::])
                return
            if val > target:
                return

            for i in range(idx, len(candidates)):
                dfs(val + candidates[i], res + [candidates[i]], i)

        dfs(0, [], 0)
        return answer
        
# Sol3  
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def dfs(i, cur, total):
            if total == target:
                answer.append(cur[::])
                return
            if i >= len(candidates) or total > target:
                return

            dfs(i, cur + [candidates[i]], total + candidates[i])
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return answer     
```
