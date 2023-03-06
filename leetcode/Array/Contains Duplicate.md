### Python solution
```python
# Hashset
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visited = set()

        for num in nums:
            if num not in visited:
                visited.add(num)
            else:
                return True

        return False
```
