### Python solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = dict()
        for idx, num in enumerate(nums):
            if (target - num) in d:
                return [idx, d[target - num]] 
            if num not in d:
                d[num] = idx    
```
