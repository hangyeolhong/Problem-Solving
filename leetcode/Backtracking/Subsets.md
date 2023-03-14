### Python solution
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        res = []

        def dfs(i):
            if i >= len(nums):
                answer.append(res[::])
                return

            # include nums[i]
            res.append(nums[i])
            dfs(i + 1)

            # not include nums[i] -> pop the element that we just appended
            res.pop()
            dfs(i + 1)

        dfs(0)

        return answer
```
