### Python solution
```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
        
        
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        limit = nums[0]
        for i, num in enumerate(nums):
            if i > limit:
                return False
            limit = max(limit, i + num)
            if limit >= len(nums) - 1:
                return True
        return True
```
