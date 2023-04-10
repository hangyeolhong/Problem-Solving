### Python solution
```python
#1.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        res = []
        nums.sort()

        def dfs(idx):
            if idx >= len(nums):
                answer.append(res[::])
                return

            res.append(nums[idx])
            dfs(idx + 1)
            res.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            dfs(idx + 1)

        dfs(0)
        return answer
        
#2.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        def dfs(res, idx):
            if idx > len(nums):
                return

            answer.append(res[:])
            
            prev = -11
            for i in range(idx, len(nums)):
                if prev != nums[i]:
                    dfs(res + [nums[i]], i + 1)

                prev = nums[i]

        dfs([], 0)
        return answer
```
