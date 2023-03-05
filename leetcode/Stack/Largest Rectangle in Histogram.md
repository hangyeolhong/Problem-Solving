### Python solution
```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []      # [index, height]

        for i, h in enumerate(heights):
            # Before adding a new building, pop the building who is taller than the new one
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                ans = max(ans, height * (i - index))
                start = index       # Extend the start index to the maximum (just before the smaller building than now)
            stack.append((start, h))  

        for i, h in stack:
            ans = max(ans, h * (len(heights) - i))

        return ans
```

### Drawing explanation
<img src="https://user-images.githubusercontent.com/59331040/222940532-94276fd2-0b78-450b-b55c-673c549d7773.PNG" width="70%"/>
