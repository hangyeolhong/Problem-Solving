### Python solution
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        mx_left, mx_right = height[left], height[right]

        res = 0
        while left < right:
            if mx_left <= mx_right:
                left += 1
                mx_left = max(mx_left, height[left])
                res += mx_left - height[left]
            else:
                right -= 1
                mx_right = max(mx_right, height[right])
                res += mx_right - height[right]

        return res
```
