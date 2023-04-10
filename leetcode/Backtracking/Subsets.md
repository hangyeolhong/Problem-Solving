### Python solution
```python
#1.
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
        
#2.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(res, idx):
            if idx == len(nums) + 1:
                return

            answer.append(res[:])

            for i in range(idx, len(nums)):
                dfs(res + [nums[i]], i + 1)

        dfs([], 0)

        return answer
```
