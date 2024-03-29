### Python solution
```python
#1.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        self.candidates = candidates
        self.candidates.sort()

        self.dfs([], 0, target)
        return self.answer


    def dfs(self, res, idx, target):
        if sum(res) == target:
            self.answer.append(res)
            return
        
        if idx == len(self.candidates):
            return

        for i in range(idx, len(self.candidates)):
            if i > idx:
                if self.candidates[i - 1] == self.candidates[i]:
                    # 중복 방지
                    continue

            if sum(res) + self.candidates[i] <= target:
                self.dfs(res + [self.candidates[i]], i + 1, target)

#2.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        answer = []

        def dfs(res, idx):
            
            if sum(res) == target:
                answer.append(res[:])
                return

            if idx >= len(candidates):
                return

            prev = -1
            for i in range(idx, len(candidates)):
                if prev != candidates[i] and sum(res) + candidates[i] <= target:
                    dfs(res + [candidates[i]], i + 1)

                prev = candidates[i]

        dfs([], 0)
        return answer
```

### Drawing explanation
<img src="https://user-images.githubusercontent.com/59331040/219700626-4d7d1461-7ed9-4a2a-956a-ea425d54ac98.png" width="70%">
<img src="https://user-images.githubusercontent.com/59331040/219700635-64b9e3e6-7291-4ce8-9467-aeafcc500658.png" width="70%">
