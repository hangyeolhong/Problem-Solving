### Python solution
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        answer = 0
        
        while i < j:
            if height[i] <= height[j]:
                # shift left pointer to search bigger area (taller height)
                # calculate area based on i
                answer = max(answer, height[i] * (j - i))
                i += 1
            else:
                # shift right pointer to search bigger area (taller height)
                # calculate area based on j
                answer = max(answer, height[j] * (j - i))
                j -= 1   
                        
        return answer
```
