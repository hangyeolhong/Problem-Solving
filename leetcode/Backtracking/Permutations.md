### Python solution
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        visit = set()

        def dfs(res, idx):
            if idx == len(nums):
                answer.append(res[:])
                return

            for i in range(len(nums)):
                if i not in visit:
                    visit.add(i)
                    dfs(res + [nums[i]], idx + 1)
                    visit.remove(i)


        dfs([], 0)
        return answer
```
