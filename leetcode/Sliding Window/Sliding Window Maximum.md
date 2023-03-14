### Python solution
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index, monotonically decreaing queue
        l = r = 0
        # O(n) O(n)
        while r < len(nums):
            # pop smaller values from q
            # compare top of the deque with cur value
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window (out of bound)
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

      
      
""" TLE

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()
        INF = int(1e5)
        mx = INF

        for idx, num in enumerate(nums):
            window.append(num)

            if idx < k - 1:
                continue

            if mx == INF:
                mx = max(window)
            elif num > mx:
                mx = num
            res.append(mx)

            # update
            if mx == window.popleft():
                mx = INF    # initialize

        return res
"""
```
