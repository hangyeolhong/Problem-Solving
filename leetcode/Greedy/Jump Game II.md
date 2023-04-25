### Python solution
```python
#1. BFS
from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        q = deque()
        visit = set()
        q.append((0, nums[0], 1))
        visit.add(0)

        while q:
            idx, n, step = q.popleft()
            if idx + n >= len(nums) - 1:
                return step
                

            for i in range(idx + 1, idx + n + 1):
                if i not in visit:
                    visit.add(i)
                    q.append((i, nums[i], step + 1))
                    
                    
#2. Greedy
class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res
```
