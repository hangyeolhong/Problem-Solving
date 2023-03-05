### Python solution
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx, mn, ans = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x = max(mx * nums[i], nums[i], mn * nums[i])
            y = min(mx * nums[i], nums[i], mn * nums[i])

            mx, mn = x, y

            ans = max(ans, mx)

        return ans
```
